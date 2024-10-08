# -*- coding: utf-8 -*-
from app.enums import SatelliteProductEnum

PRODUCTS_INFO = {
    SatelliteProductEnum.CAPE: {
        "product": {
            "name": "CAPE (Convective Available Potential Energy)",
            "description": "CAPE é a quantidade de energia potencial disponível para a convecção em uma parcela de ar. Ela mede a instabilidade atmosférica e é usada para prever a formação de tempestades convectivas.",
            "unit": "J/kg",
            "source": "Satélite GOES-16",
            "frequency": "10 Min",
        },
        "values_range": {"min": 0, "max": 5000},
        "legend": {
            "title": "Energia Potencial Convectiva (CAPE)",
            "colors": [
                {"value": 0, "color": "#0000FF"},
                {"value": 500, "color": "#00FFFF"},
                {"value": 1000, "color": "#00FF00"},
                {"value": 1500, "color": "#FFFF00"},
                {"value": 2000, "color": "#FFA500"},
                {"value": 3000, "color": "#FF4500"},
                {"value": 4000, "color": "#FF0000"},
                {"value": 5000, "color": "#8B0000"},
            ],
            "opacity": 0.1,
        },
        "map": {
            "type": "Heat map",
            "projection": "Geographical",
            "update_frequency": "Hourly",
            "spatial_resolution": "4 km x 4 km",
            "interpolation_method": "mean",
            "additional_layers": [
                {
                    "type": "Topography",
                    "description": "Topography added for geographical context",
                }
            ],
        },
    },
    SatelliteProductEnum.K_INDEX: {
        "product": {
            "name": "KI (K-Index)",
            "description": "O KI (K-Index) é um índice utilizado para avaliar o potencial de tempestades e a instabilidade atmosférica. Ele é derivado de medições de temperatura e umidade em diferentes níveis da atmosfera e ajuda a identificar áreas propensas à formação de tempestades.",
            "unit": "Unidade",
            "source": "Satélite GOES-16",
            "frequency": "10 Min",
        },
        "values_range": {"min": 0, "max": 60},
        "legend": {
            "title": "Índice K (KI)",
            "colors": [
                {"value": 0, "color": "#00FFFF"},
                {"value": 10, "color": "#00FF00"},
                {"value": 20, "color": "#FFFF00"},
                {"value": 30, "color": "#FFA500"},
                {"value": 40, "color": "#FF4500"},
                {"value": 50, "color": "#FF0000"},
                {"value": 60, "color": "#FF0000"},
            ],
            "opacity": 0.1,
        },
        "map": {
            "type": "Heat map",
            "projection": "Geographical",
            "update_frequency": "Hourly",
            "spatial_resolution": "4 km x 4 km",
            "interpolation_method": "mean",
            "additional_layers": [
                {
                    "type": "Topography",
                    "description": "Topografia adicionada para contexto geográfico",
                }
            ],
        },
    },
    SatelliteProductEnum.SHOWALTER_INDEX: {
        "product": {
            "name": "SI (Showalter Index)",
            "description": "O SI (Showalter Index) é um índice de estabilidade atmosférica que avalia o potencial de tempestades a partir da comparação da temperatura de uma parcela de ar levantada do nível de 850 hPa até 500 hPa. Quanto mais negativo o valor, maior a instabilidade e a possibilidade de tempestades severas.",
            "unit": "°C",
            "source": "Satélite GOES-16",
            "frequency": "10 Min",
        },
        "values_range": {"min": -20, "max": 20},
        "legend": {
            "title": "Índice de Showalter (SI)",
            "colors": [
                {"value": -20, "color": "#FF0000"},
                {"value": -15, "color": "#FF4500"},
                {"value": -10, "color": "#FF0000"},
                {"value": -5, "color": "#FF4500"},
                {"value": 0, "color": "#FFFF00"},
                {"value": 5, "color": "#00FF00"},
                {"value": 10, "color": "#0000FF"},
                {"value": 15, "color": "#00FF00"},
                {"value": 20, "color": "#0000FF"},
            ],
            "opacity": 0.1,
        },
        "map": {
            "type": "Heat map",
            "projection": "Geographical",
            "update_frequency": "Hourly",
            "spatial_resolution": "4 km x 4 km",
            "interpolation_method": "mean",
            "additional_layers": [
                {
                    "type": "Topography",
                    "description": "Topografia adicionada para contexto geográfico",
                }
            ],
        },
    },
    SatelliteProductEnum.LIFTED_INDEX: {
        "product": {
            "name": "LI (Lifted Index)",
            "description": "O LI (Lifted Index) é uma medida de instabilidade atmosférica que compara a temperatura de uma parcela de ar com a temperatura ambiente ao nível de 500 hPa. Valores negativos indicam maior probabilidade de tempestades convectivas.",
            "unit": "°C",
            "source": "Satélite GOES-16",
            "frequency": "10 Min",
        },
        "values_range": {"min": -20, "max": 20},
        "legend": {
            "title": "Índice de Elevação (LI)",
            "colors": [
                {"value": -20, "color": "#FF0000"},
                {"value": -15, "color": "#FF4500"},
                {"value": -10, "color": "#FF0000"},
                {"value": -5, "color": "#FF4500"},
                {"value": 0, "color": "#FFFF00"},
                {"value": 5, "color": "#00FF00"},
                {"value": 10, "color": "#0000FF"},
                {"value": 15, "color": "#00FF00"},
                {"value": 20, "color": "#0000FF"},
            ],
            "opacity": 0.1,
        },
        "map": {
            "type": "Heat map",
            "projection": "Geographical",
            "update_frequency": "Hourly",
            "spatial_resolution": "4 km x 4 km",
            "interpolation_method": "mean",
            "additional_layers": [
                {
                    "type": "Topography",
                    "description": "Topografia adicionada para contexto geográfico",
                }
            ],
        },
    },
    SatelliteProductEnum.TOTALS_TOTALS_INDEX: {
        "product": {
            "name": "TT (Total Totals Index)",
            "description": "O TT (Total Totals Index) é um índice de instabilidade atmosférica usado para prever a ocorrência de tempestades convectivas severas. Ele combina a temperatura no nível de 850 hPa com a diferença entre a temperatura e o ponto de orvalho no nível de 850 hPa, e a temperatura no nível de 500 hPa.",
            "unit": "Índice",
            "source": "Satélite GOES-16",
            "frequency": "10 Min",
        },
        "values_range": {"min": 10, "max": 70},
        "legend": {
            "title": "Índice Total Totals (TT)",
            "colors": [
                {"value": 10, "color": "#0000FF"},
                {"value": 20, "color": "#0000FF"},
                {"value": 30, "color": "#00FFFF"},
                {"value": 40, "color": "#00FF00"},
                {"value": 50, "color": "#FFFF00"},
                {"value": 60, "color": "#FFA500"},
                {"value": 70, "color": "#FF4500"},
            ],
            "opacity": 0.1,
        },
        "map": {
            "type": "Heat map",
            "projection": "Geographical",
            "update_frequency": "Hourly",
            "spatial_resolution": "4 km x 4 km",
            "interpolation_method": "mean",
            "additional_layers": [
                {
                    "type": "Topography",
                    "description": "Topografia adicionada para contexto geográfico",
                }
            ],
        },
    },
}
