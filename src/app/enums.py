# -*- coding: utf-8 -*-
from enum import Enum


class SatelliteProductEnum(str, Enum):
    CAPE = "cp"
    K_INDEX = "ki"
    SHOWALTER_INDEX = "si"
    LIFTED_INDEX = "li"
    TOTALS_TOTALS_INDEX = "tt"
    RAIN_RATE = "rrqpe"
    OCEAN_TEMPERATURE = "sst"
    TOTAL_PRECIPITABLE_WATER = "tpw"


class ImpaModelProductEnum(str, Enum):
    PYSTEPS = "pysteps"
    UNET = "unet"
    NOWCASTNET = "nowcastnet"
    METNET3 = "metnet3"
    MAMBA = "mamba"


class RionowcastModelProductEnum(str, Enum):
    V1 = "v1"
    V2 = "v2"
