# -*- coding: utf-8 -*-
from datetime import datetime

# from math import isnan
from typing import List

from fastapi import APIRouter, HTTPException

# from google.cloud import bigquery
# from loguru import logger
from pendulum import DateTime, parse as pendulum_parse

from app import config
from app.enums import RionowcastModelProductEnum
from app.pydantic_models import ImageSliderOut  # , SatelliteChartDataOut
from app.products_info import PRODUCTS_INFO
from app.utils import (
    # get_data_from_bigquery,
    get_matching_blobs,
    sanity_check_time_range,
)

router = APIRouter(
    prefix="/nowcasting_models",
    tags=["Nowcasting models"],
    responses={
        429: {"error": "Rate limit exceeded"},
    },
)


@router.get(
    "/rionowcast/gif/{product}/{time_horizon}",
    summary="Get GIF from Rionowcast models",
    response_model=List[ImageSliderOut],
)
async def get_rionowcast_models_gif(
    product: RionowcastModelProductEnum,
    time_horizon: str,
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
    mapping = config.RIONOWCAST_PRODUCTS_MAPPING.get(product, None)
    if not mapping:
        raise HTTPException(status_code=400, detail="Invalid product")
    gcs_product_prefix = mapping.get("gcs_prefix")
    if not gcs_product_prefix:
        raise HTTPException(
            status_code=501, detail="This product is not implemented yet."
        )
    # permited_time_horizon = mapping.get("time_horizon")
    # if not permited_time_horizon:
    #     raise HTTPException(
    #         status_code=501, detail="This time horizon prediction is not implemented yet."
    #     )

    path_prefix = f"cor-clima-imagens/predicao_precipitacao/rionowcast/{gcs_product_prefix}/{time_horizon}/without_background"
    # TODO: modify to get other hours prediction
    return get_matching_blobs(
        start_time=start_time,
        end_time=end_time,
        path_prefix=path_prefix,
    )


@router.get(
    "/info/{product}",
    summary="Get information about a product",
    response_model=dict,
)
async def get_model_info(product: RionowcastModelProductEnum):
    mapping = config.RIONOWCAST_PRODUCTS_MAPPING.get(product, None)
    if not mapping:
        raise HTTPException(status_code=400, detail="Invalid product")
    product_info = PRODUCTS_INFO.get(product, None)
    if not product_info:
        raise HTTPException(
            status_code=501, detail="This product is not implemented yet."
        )
    return product_info
