# -*- coding: utf-8 -*-
from datetime import datetime
from typing import List

from fastapi import APIRouter, HTTPException
from pendulum import DateTime

from app import config
from app.enums import RadarProductEnum
from app.pydantic_models import ImageSliderOut
from app.products_info import PRODUCTS_INFO
from app.utils import get_matching_blobs, sanity_check_time_range

router = APIRouter(
    prefix="/radar",
    tags=["Radar data"],
    responses={
        429: {"error": "Rate limit exceeded"},
    },
)


@router.get(
    "/mendanha/{product}",
    summary="Get GIF from Mendanha Radar",
    response_model=List[ImageSliderOut],
)
async def get_mendanha_radar_data(
    product: RadarProductEnum,
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
    mapping = config.RADAR_PRODUCTS_MAPPING.get(product, None)
    if not mapping:
        raise HTTPException(status_code=400, detail="Invalid product")
    gcs_product_prefix = mapping.get("gcs_prefix")
    if not gcs_product_prefix:
        raise HTTPException(
            status_code=501, detail="This product is not implemented yet."
        )

    # Get blob URLs list
    path_prefix = f"cor-clima-imagens/radar/mendanha/{gcs_product_prefix}/without_background/without_colorbar/"
    return get_matching_blobs(
        start_time=start_time,
        end_time=end_time,
        path_prefix=path_prefix,
    )


@router.get(
    "/info/{product}",
    summary="Get information about a radar product",
    response_model=dict,
)
async def get_radar_info(product: RadarProductEnum):
    mapping = config.RADAR_PRODUCTS_MAPPING.get(product, None)
    if not mapping:
        raise HTTPException(status_code=400, detail="Invalid product")
    product_info = PRODUCTS_INFO.get(product, None)
    if not product_info:
        raise HTTPException(
            status_code=501, detail="This product is not implemented yet."
        )
    return product_info
