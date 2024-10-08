# -*- coding: utf-8 -*-
from datetime import datetime
from math import isnan
from typing import List

from fastapi import APIRouter, HTTPException
from google.cloud import bigquery
from loguru import logger
from pendulum import DateTime, parse as pendulum_parse

from app import config
from app.enums import SatelliteProductEnum
from app.pydantic_models import ImageSliderOut, SatelliteChartDataOut
from app.products_info import PRODUCTS_INFO
from app.utils import (
    get_data_from_bigquery,
    get_matching_blobs,
    sanity_check_time_range,
)

router = APIRouter(
    prefix="/satellite",
    tags=["Satellite data"],
    responses={
        429: {"error": "Rate limit exceeded"},
    },
)


@router.get(
    "/goes16/chart/{product}",
    summary="Get chart data from GOES16",
    response_model=List[SatelliteChartDataOut],
)
async def get_satellite_chart(
    product: SatelliteProductEnum,
    start_time: datetime,
    end_time: datetime,
):
    def map_to_models(row):
        return SatelliteChartDataOut(
            timestamp=pendulum_parse(row["data_medicao"], tz="America/Sao_Paulo"),
            value=row["valor"]
            if row["valor"] and not isnan(float(row["valor"]))
            else None,
        )

    # Sanity checks
    start_time, end_time = sanity_check_time_range(
        start_time,
        end_time,
        max_allowed_range_seconds=config.SATELLITE_GIF_MAX_ALLOWED_RANGE_SECONDS,
    )

    # Parse start_time and end_time to pendulum.DateTime
    start_time = DateTime.instance(start_time, tz=config.TIMEZONE)
    start_time = start_time.in_tz(config.TIMEZONE)
    end_time = DateTime.instance(end_time, tz=config.TIMEZONE)
    end_time = end_time.in_tz(config.TIMEZONE)

    # If it's RR or SST, we still got no data
    if product in [
        SatelliteProductEnum.RAIN_RATE,
        SatelliteProductEnum.OCEAN_TEMPERATURE,
    ]:
        raise HTTPException(
            status_code=501, detail="This product is not implemented yet."
        )

    table = config.BIGQUERY_TABLE_METRICAS_GEOESPACIAIS
    mapping = config.SATELLITE_PRODUCTS_MAPPING.get(product, None)
    if not mapping:
        raise HTTPException(status_code=400, detail="Invalid product")
    column = mapping.get("column")
    if not column:
        raise HTTPException(
            status_code=501, detail="This product is not implemented yet."
        )
    query = f"""
    SELECT
        data_medicao,
        valor
    FROM {table}
    WHERE
        data_medicao BETWEEN @start_time AND @end_time
        AND produto_satelite = @column
    """
    query_params = [
        bigquery.ScalarQueryParameter(
            "start_time", "STRING", start_time.format("YYYY-MM-DD HH:mm:ss")
        ),
        bigquery.ScalarQueryParameter(
            "end_time", "STRING", end_time.format("YYYY-MM-DD HH:mm:ss")
        ),
        bigquery.ScalarQueryParameter("column", "STRING", column),
    ]
    logger.debug(f"Query: {query}")
    logger.debug(f"Query Params: {query_params}")
    data = get_data_from_bigquery(query=query, query_params=query_params)
    data.drop_duplicates(inplace=True)

    logger.debug(f"Data:\n{data}")

    return data.apply(map_to_models, axis=1).tolist()


@router.get(
    "/goes16/gif/{product}",
    summary="Get GIF from GOES16",
    response_model=List[ImageSliderOut],
)
async def get_satellite_gif(
    product: SatelliteProductEnum,
    start_time: datetime,
    end_time: datetime,
):
    # Sanity checks
    start_time, end_time = sanity_check_time_range(
        start_time,
        end_time,
        max_allowed_range_seconds=config.SATELLITE_GIF_MAX_ALLOWED_RANGE_SECONDS,
    )

    # Parse start_time and end_time to pendulum.DateTime
    start_time = DateTime.instance(start_time, tz=config.TIMEZONE)
    start_time = start_time.in_tz(config.TIMEZONE)
    end_time = DateTime.instance(end_time, tz=config.TIMEZONE)
    end_time = end_time.in_tz(config.TIMEZONE)

    # Get blob URLs list
    mapping = config.SATELLITE_PRODUCTS_MAPPING.get(product, None)
    if not mapping:
        raise HTTPException(status_code=400, detail="Invalid product")
    gcs_product_prefix = mapping.get("gcs_prefix")
    if not gcs_product_prefix:
        raise HTTPException(
            status_code=501, detail="This product is not implemented yet."
        )
    path_prefix = "cor-clima-imagens/satelite/goes16/without_background/"
    blob_name_prefix = f"{gcs_product_prefix}_"
    return get_matching_blobs(
        start_time=start_time,
        end_time=end_time,
        path_prefix=path_prefix,
        blob_name_prefix=blob_name_prefix,
    )


@router.get(
    "/info/{product}",
    summary="Get information about a satellite product",
    response_model=dict,
)
async def get_satellite_info(product: SatelliteProductEnum):
    mapping = config.SATELLITE_PRODUCTS_MAPPING.get(product, None)
    if not mapping:
        raise HTTPException(status_code=400, detail="Invalid product")
    product_info = PRODUCTS_INFO.get(product, None)
    if not product_info:
        raise HTTPException(
            status_code=501, detail="This product is not implemented yet."
        )
    return product_info
