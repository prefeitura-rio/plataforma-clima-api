# -*- coding: utf-8 -*-
from datetime import datetime
from typing import List

from fastapi import APIRouter
from pendulum import DateTime

from app import config
from app.pydantic_models import ImageSliderOut
from app.utils import get_matching_blobs, sanity_check_time_range

router = APIRouter(
    prefix="/radar",
    tags=["Radar data"],
    responses={
        429: {"error": "Rate limit exceeded"},
    },
)


@router.get(
    "/mendanha",
    summary="Get GIF from Mendanha Radar",
    response_model=List[ImageSliderOut],
)
async def get_mendanha_radar_data(
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
    path_prefix = "cor-clima-imagens/radar/mendanha/refletividade_horizontal/without_background/without_colorbar/"
    return get_matching_blobs(
        start_time=start_time,
        end_time=end_time,
        path_prefix=path_prefix,
        timestamp_format="YYYY-MM-DD-HH-mm-ss",  # TODO: Modify this when the new format is set
    )
