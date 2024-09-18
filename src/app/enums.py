# -*- coding: utf-8 -*-
from enum import Enum


class SatelliteProductEnum(str, Enum):
    CAPE = "cp"
    K_INDEX = "ki"
    SHOWALTER_INDEX = "si"
    LIFTED_INDEX = "li"
    TOTALS_TOTALS_INDEX = "tt"
    RAIN_RATE = "rr"
    OCEAN_TEMPERATURE = "sst"
