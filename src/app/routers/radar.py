# -*- coding: utf-8 -*-
from datetime import datetime
from typing import List

from fastapi import APIRouter, HTTPException

from app import config
from app.pydantic_models import ImageSliderOut
from app.utils import sanity_check_time_range

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
    latitude_min: float = None,
    latitude_max: float = None,
    longitude_min: float = None,
    longitude_max: float = None,
):
    start_time, end_time = sanity_check_time_range(
        start_time,
        end_time,
        max_allowed_range_seconds=config.RADAR_DATA_MAX_ALLOWED_RANGE_SECONDS,
    )
    raise HTTPException(status_code=501, detail="This is not implemented yet.")
