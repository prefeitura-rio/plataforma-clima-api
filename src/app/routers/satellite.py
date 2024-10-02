# -*- coding: utf-8 -*-
from datetime import datetime
from typing import List

from fastapi import APIRouter, HTTPException
from pendulum import DateTime

from app import config
from app.enums import SatelliteProductEnum
from app.pydantic_models import ImageSliderOut, SatelliteChartDataOut
from app.utils import (
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
    # Sanity checks
    start_time, end_time = sanity_check_time_range(
        start_time,
        end_time,
        max_allowed_range_seconds=config.SATELLITE_GIF_MAX_ALLOWED_RANGE_SECONDS,
    )
    raise HTTPException(status_code=501, detail="This is not implemented yet.")


@router.get(
    "/goes16/gif/{product}",
    summary="Get GIF from GOES16",
    response_model=List[ImageSliderOut],
)
async def get_satellite_gif(
    product: SatelliteProductEnum,
    start_time: datetime,
    end_time: datetime,
    latitude_min: float = None,
    latitude_max: float = None,
    longitude_min: float = None,
    longitude_max: float = None,
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

    return get_matching_blobs(product=product, start_time=start_time, end_time=end_time)

    raise HTTPException(status_code=501, detail="This is not implemented yet.")
    # query = """
    # SELECT
    #     latitude,
    #     longitude,
    #     data_particao,
    #     horario,
    #     @column AS value
    # FROM @table
    # WHERE
    #     data_particao BETWEEN @start_date AND @end_date
    #     AND horario BETWEEN @start_time AND @end_time
    # """.replace("@table", table).replace("@column", column)
    # # TODO: handle timezones. data is in America/Sao_Paulo timezone
    # query_params = [
    #     bigquery.ScalarQueryParameter(
    #         "start_date", "STRING", start_time.strftime("%Y-%m-%d")
    #     ),
    #     bigquery.ScalarQueryParameter(
    #         "end_date", "STRING", end_time.strftime("%Y-%m-%d")
    #     ),
    #     bigquery.ScalarQueryParameter(
    #         "start_time", "STRING", start_time.strftime("%H:%M:%S")
    #     ),
    #     bigquery.ScalarQueryParameter(
    #         "end_time", "STRING", end_time.strftime("%H:%M:%S")
    #     ),
    # ]
    # if latitude_min is not None:
    #     query += " AND latitude >= @latitude_min"
    #     query_params.append(
    #         bigquery.ScalarQueryParameter("latitude_min", "STRING", latitude_min)
    #     )
    # if latitude_max is not None:
    #     query += " AND latitude <= @latitude_max"
    #     query_params.append(
    #         bigquery.ScalarQueryParameter("latitude_max", "STRING", latitude_max)
    #     )
    # if longitude_min is not None:
    #     query += " AND longitude >= @longitude_min"
    #     query_params.append(
    #         bigquery.ScalarQueryParameter("longitude_min", "STRING", longitude_min)
    #     )
    # if longitude_max is not None:
    #     query += " AND longitude <= @longitude_max"
    #     query_params.append(
    #         bigquery.ScalarQueryParameter("longitude_max", "STRING", longitude_max)
    #     )
    # logger.debug(f"Query: {query}")
    # logger.debug(f"Query Params: {query_params}")
    # data = get_data_from_bigquery(query=query, query_params=query_params)
    # logger.debug(f"Data:\n{data}")

    # raise HTTPException(status_code=501, detail="This is not implemented yet.")
