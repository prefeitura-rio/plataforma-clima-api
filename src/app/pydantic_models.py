# -*- coding: utf-8 -*-
from datetime import datetime

from pydantic import BaseModel


class HealthCheck(BaseModel):
    status: str


class ImageSliderOut(BaseModel):
    timestamp: datetime
    image_url: str


class SatelliteChartDataOut(BaseModel):
    timestamp: datetime
    value: float
