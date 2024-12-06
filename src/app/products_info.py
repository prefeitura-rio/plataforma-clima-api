# -*- coding: utf-8 -*-
from app.enums import (
    ImpaModelProductEnum,
    RadarProductEnum,
    RionowcastModelProductEnum,
    SatelliteProductEnum,
)

# alertario_precipitation_colors = [
#     {"value": 0, "color": "#63bbff"},
#     {"value": 5, "color": "#91ccab"},
#     {"value": 10, "color": "#bfdd56"},
#     {"value": 15, "color": "#eeee01"},
#     {"value": 20, "color": "#ffd163"},
#     {"value": 25, "color": "#ffb421"},
#     {"value": 30, "color": "#ff9700"},
#     {"value": 35, "color": "#f57000"},
#     {"value": 40, "color": "#ee5500"},
#     {"value": 45, "color": "#ee2a00"},
#     {"value": 50, "color": "#ED0000"},
#     {"value": 55, "color": "#d40000"},
# {"value": 60, "color": "#bc0000"},
# {"value": 65, "color": "#a30000"},
# {"value": 70, "color": "#8A0000"},
# {"value": 75, "color": "#6e0000"},
# {"value": 80, "color": "#530000"},
# {"value": 85, "color": "#380000"},
#     {"value": 90, "color": "#1C0000"},
# ]
alertario_precipitation_colors = [
    {"value": 0.01, "color": "#63bbff"},
    {"value": 15.05, "color": "#eeee00"},
    {"value": 27.55, "color": "#ffa500"},
    {"value": 50, "color": "#ed0000"},
    {"value": 70, "color": "#8a0000"},
    {"value": 90, "color": "#1c0000"},
]

PRODUCTS_INFO = {
    SatelliteProductEnum.CAPE: {
        "product": {
            "name": "CAPE (Convective Available Potential Energy)",
            "description": "CAPE é a quantidade de energia potencial disponível para a convecção em uma parcela de ar. Ela mede a instabilidade atmosférica e é usada para prever a formação de tempestades convectivas.",
            "unit": "J/kg",
            "source": "Satélite GOES-16",
            "frequency": "10 Min",
        },
        "values_range": {"min": 0, "max": 8000},
        "legend": {
            "title": "Energia Potencial Convectiva (CAPE)",
            "colors": [
                {"value": 0, "color": "#000080"},
                {"value": 1000, "color": "#0000FF"},
                {"value": 2000, "color": "#00FFFF"},
                {"value": 3000, "color": "#00FF00"},
                {"value": 4000, "color": "#FFFF00"},
                {"value": 5000, "color": "#FFA500"},
                {"value": 6000, "color": "#FF4500"},
                {"value": 7000, "color": "#FF0000"},
                {"value": 8000, "color": "#800000"},
            ],
            "opacity": 0.1,
        },
        "map": {
            "type": "Heat map",
            "projection": "Geographical",
            "update_frequency": "Hourly",
            "spatial_resolution": "4 km x 4 km",
            "interpolation_method": "None",
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
                {"value": 0, "color": "#0000FF"},
                {"value": 10, "color": "#00FFFF"},
                {"value": 20, "color": "#00FF00"},
                {"value": 30, "color": "#FFFF00"},
                {"value": 40, "color": "#FFA500"},
                {"value": 50, "color": "#FF0000"},
                {"value": 60, "color": "#800000"},
            ],
            "opacity": 0.1,
        },
        "map": {
            "type": "Heat map",
            "projection": "Geographical",
            "update_frequency": "Hourly",
            "spatial_resolution": "4 km x 4 km",
            "interpolation_method": "None",
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
                {"value": -20, "color": "#000080"},
                {"value": -15, "color": "#0000FF"},
                {"value": -10, "color": "#00FFFF"},
                {"value": -5, "color": "#00FF00"},
                {"value": 0, "color": "#FFFF00"},
                {"value": 5, "color": "#FFA500"},
                {"value": 10, "color": "#FF4500"},
                {"value": 15, "color": "#FF0000"},
                {"value": 20, "color": "#800000"},
            ],
            "opacity": 0.1,
        },
        "map": {
            "type": "Heat map",
            "projection": "Geographical",
            "update_frequency": "Hourly",
            "spatial_resolution": "4 km x 4 km",
            "interpolation_method": "None",
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
                {"value": -20, "color": "#000080"},
                {"value": -15, "color": "#0000FF"},
                {"value": -10, "color": "#00FFFF"},
                {"value": -5, "color": "#00FF00"},
                {"value": 0, "color": "#FFFF00"},
                {"value": 5, "color": "#FFA500"},
                {"value": 10, "color": "#FF4500"},
                {"value": 15, "color": "#FF0000"},
                {"value": 20, "color": "#800000"},
            ],
            "opacity": 0.1,
        },
        "map": {
            "type": "Heat map",
            "projection": "Geographical",
            "update_frequency": "Hourly",
            "spatial_resolution": "4 km x 4 km",
            "interpolation_method": "None",
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
                {"value": 20, "color": "#00FFFF"},
                {"value": 30, "color": "#00FF00"},
                {"value": 40, "color": "#FFFF00"},
                {"value": 50, "color": "#FFA500"},
                {"value": 60, "color": "#FF0000"},
                {"value": 70, "color": "#800000"},
            ],
            "opacity": 0.1,
        },
        "map": {
            "type": "Heat map",
            "projection": "Geographical",
            "update_frequency": "Hourly",
            "spatial_resolution": "4 km x 4 km",
            "interpolation_method": "None",
            "additional_layers": [
                {
                    "type": "Topography",
                    "description": "Topografia adicionada para contexto geográfico",
                }
            ],
        },
    },
    SatelliteProductEnum.RAIN_RATE: {
        "product": {
            "name": "RRQPE (Rainfall Rate Quantitative Precipitation Estimate)",
            "description": "A taxa de chuva (Rainfall Rate Quantitative Precipitation Estimate - RRQPE) é uma medida da intensidade da precipitação, expressa em milímetros por hora (mm/h). Ela indica a quantidade de chuva que cai em uma determinada área dentro de um período de tempo. Valores mais altos representam chuvas mais intensas, enquanto valores baixos indicam precipitação leve ou inexistente.",
            "unit": "mm/h",
            "source": "Satélite GOES-16",
            "frequency": "10 Min",
        },
        "values_range": {"min": 0, "max": 50},
        "legend": {
            "title": "Taxa de Precipitação Estimada (RRQPE)",
            "colors": [
                {"value": 0, "color": "#0000FF"},
                {"value": 5, "color": "#00FFFF"},
                {"value": 10, "color": "#00FF00"},
                {"value": 20, "color": "#FFFF00"},
                {"value": 30, "color": "#FFA500"},
                {"value": 40, "color": "#FF0000"},
                {"value": 50, "color": "#800000"},
            ],
            "opacity": 0.1,
        },
        "map": {
            "type": "Heat map",
            "projection": "Geographical",
            "update_frequency": "Hourly",
            "spatial_resolution": "4 km x 4 km",
            "interpolation_method": "None",
            "additional_layers": [
                {
                    "type": "Topography",
                    "description": "Topografia adicionada para contexto geográfico",
                }
            ],
        },
    },
    SatelliteProductEnum.OCEAN_TEMPERATURE: {
        "product": {
            "name": "SST (Sea Surface Temperature)",
            "description": "A Temperatura da Superfície do Mar (SST) é uma medida da temperatura da água na superfície dos oceanos.",
            "unit": "K",
            "source": "Satélite GOES-16",
            "frequency": "10 Min",
        },
        "values_range": {"min": -5, "max": 35},
        "legend": {
            "title": "Temperatura da Superfície do Mar (SST)",
            "colors": [
                {"value": -5, "color": "#00008B"},
                {"value": 0, "color": "#0000FF"},
                {"value": 5, "color": "#00BFFF"},
                {"value": 10, "color": "#87CEEB"},
                {"value": 15, "color": "#00FF00"},
                {"value": 20, "color": "#FFFF00"},
                {"value": 25, "color": "#FFA500"},
                {"value": 30, "color": "#FF4500"},
                {"value": 35, "color": "#800000"},
            ],
            "opacity": 0.1,
        },
        "map": {
            "type": "Heat map",
            "projection": "Geographical",
            "update_frequency": "Hourly",
            "spatial_resolution": "4 km x 4 km",
            "interpolation_method": "None",
            "additional_layers": [
                {
                    "type": "Topography",
                    "description": "Topografia adicionada para contexto geográfico",
                }
            ],
        },
    },
    SatelliteProductEnum.TOTAL_PRECIPITABLE_WATER: {
        "product": {
            "name": "TPW (Total Precipitable Water)",
            "description": "A Água Precipitada Total (TPW) é uma medida da quantidade total de vapor d'água presente na coluna de ar acima de um ponto específico.",
            "unit": "mm",
            "source": "Satélite GOES-16",
            "frequency": "10 Min",
        },
        "values_range": {"min": 0, "max": 60},
        "legend": {
            "title": "Água Precipitada Total (TPW)",
            "colors": [
                {"value": 0, "color": "#00008B"},
                {"value": 5, "color": "#0000FF"},
                {"value": 10, "color": "#00BFFF"},
                {"value": 20, "color": "#87CEEB"},
                {"value": 30, "color": "#00FF00"},
                {"value": 40, "color": "#FFFF00"},
                {"value": 50, "color": "#FFA500"},
                {"value": 55, "color": "#FF4500"},
                {"value": 60, "color": "#800000"},
            ],
            "opacity": 0.1,
        },
        "map": {
            "type": "Heat map",
            "projection": "Geographical",
            "update_frequency": "Hourly",
            "spatial_resolution": "4 km x 4 km",
            "interpolation_method": "None",
            "additional_layers": [
                {
                    "type": "Topography",
                    "description": "Topografia adicionada para contexto geográfico",
                }
            ],
        },
    },
    RionowcastModelProductEnum.V1: {
        "product": {
            "name": "Modelo de Previsão de Chuva criado pelo grupo Rionowcast (v1).",
            "description": "Modelo de Previsão de Chuva criado pelo grupo Rionowcast utilizando dados dos pluviômetros do Alertario e dos radares do Mendanha e Guaratiba.",
            "unit": "mm/h",
            "source": "Pluviômetros Alertario e radares do Mendanha e Guaratiba",
            "frequency": "60 Min",
        },
        "values_range": {"min": 0, "max": 100},
        "legend": {
            "title": "Modelo Rionowcast (v1)",
            "colors": alertario_precipitation_colors,
            "opacity": 0.1,
        },
        "map": {
            "type": "Heat map",
            "projection": "Geographical",
            "update_frequency": "Hourly",
            "spatial_resolution": "4 km x 4 km",
            "interpolation_method": "None",
            "additional_layers": [
                {
                    "type": "Topography",
                    "description": "Topografia adicionada para contexto geográfico",
                }
            ],
        },
    },
    RionowcastModelProductEnum.V2: {
        "product": {
            "name": "Modelo de Previsão de Chuva criado pelo grupo Rionowcast (v2).",
            "description": "Modelo de Previsão de Chuva criado pelo grupo Rionowcast utilizando dados do satélite GOES-16.",
            "unit": "mm/h",
            "source": "GOES-16",
            "frequency": "60 Min",
        },
        "values_range": {"min": 0, "max": 100},
        "legend": {
            "title": "Modelo Rionowcast (v2)",
            "colors": alertario_precipitation_colors,
            "opacity": 0.1,
        },
        "map": {
            "type": "Heat map",
            "projection": "Geographical",
            "update_frequency": "Hourly",
            "spatial_resolution": "4 km x 4 km",
            "interpolation_method": "None",
            "additional_layers": [
                {
                    "type": "Topography",
                    "description": "Topografia adicionada para contexto geográfico",
                }
            ],
        },
    },
    ImpaModelProductEnum.NOWCASTNET: {
        "product": {
            "name": "Modelo de Previsão de Chuva NOWCASTNET (v1).",
            "description": "Modelo de Previsão de Chuva usando a rede NOWCASTNET criado pelo grupo Centro Pi utilizando dados do satélite GOES-16.",
            "unit": "mm/h",
            "source": "Satélite GOES-16",
            "frequency": "60 Min",
        },
        "values_range": {"min": 0, "max": 100},
        "legend": {
            "title": "Modelo NowcastNet",
            "colors": alertario_precipitation_colors,
            "opacity": 0.1,
        },
        "map": {
            "type": "Heat map",
            "projection": "Geographical",
            "update_frequency": "Hourly",
            "spatial_resolution": "4 km x 4 km",
            "interpolation_method": "None",
            "additional_layers": [
                {
                    "type": "Topography",
                    "description": "Topografia adicionada para contexto geográfico",
                }
            ],
        },
    },
    ImpaModelProductEnum.PYSTEPS: {
        "product": {
            "name": "Modelo de Previsão de Chuva PySteps (v1).",
            "description": "Modelo de Previsão de Chuva usando Pysteps criado pelo grupo Centro Pi utilizando dados do satélite GOES-16.",
            "unit": "mm/h",
            "source": "Satélite GOES-16",
            "frequency": "60 Min",
        },
        "values_range": {"min": 0, "max": 100},
        "legend": {
            "title": "Modelo Pysteps",
            "colors": alertario_precipitation_colors,
            "opacity": 0.1,
        },
        "map": {
            "type": "Heat map",
            "projection": "Geographical",
            "update_frequency": "Hourly",
            "spatial_resolution": "4 km x 4 km",
            "interpolation_method": "None",
            "additional_layers": [
                {
                    "type": "Topography",
                    "description": "Topografia adicionada para contexto geográfico",
                }
            ],
        },
    },
    ImpaModelProductEnum.UNET: {
        "product": {
            "name": "Modelo de Previsão de Chuva UNET (v1).",
            "description": "Modelo de Previsão de Chuva usando a rede UNET criado pelo grupo Centro Pi utilizando dados do satélite GOES-16.",
            "unit": "mm/h",
            "source": "Satélite GOES-16",
            "frequency": "60 Min",
        },
        "values_range": {"min": 0, "max": 100},
        "legend": {
            "title": "Modelo Unet",
            "colors": alertario_precipitation_colors,
            "opacity": 0.1,
        },
        "map": {
            "type": "Heat map",
            "projection": "Geographical",
            "update_frequency": "Hourly",
            "spatial_resolution": "4 km x 4 km",
            "interpolation_method": "None",
            "additional_layers": [
                {
                    "type": "Topography",
                    "description": "Topografia adicionada para contexto geográfico",
                }
            ],
        },
    },
    ImpaModelProductEnum.METNET3: {
        "product": {
            "name": "Modelo de Previsão de Chuva METNET3 (v1).",
            "description": "Modelo de Previsão de Chuva usando a rede METNET3 criado pelo grupo Centro Pi utilizando dados do satélite GOES-16.",
            "unit": "mm/h",
            "source": "Satélite GOES-16",
            "frequency": "60 Min",
        },
        "values_range": {"min": 0, "max": 100},
        "legend": {
            "title": "Modelo MetNet3",
            "colors": alertario_precipitation_colors,
            "opacity": 0.1,
        },
        "map": {
            "type": "Heat map",
            "projection": "Geographical",
            "update_frequency": "Hourly",
            "spatial_resolution": "4 km x 4 km",
            "interpolation_method": "None",
            "additional_layers": [
                {
                    "type": "Topography",
                    "description": "Topografia adicionada para contexto geográfico",
                }
            ],
        },
    },
    ImpaModelProductEnum.MAMBA: {
        "product": {
            "name": "Modelo de Previsão de Chuva MAMBA (v1).",
            "description": "Modelo de Previsão de Chuva usando a rede MAMBA criado pelo grupo Centro Pi utilizando dados do satélite GOES-16.",
            "unit": "mm/h",
            "source": "Satélite GOES-16",
            "frequency": "60 Min",
        },
        "values_range": {"min": 0, "max": 100},
        "legend": {
            "title": "Modelo Mamba",
            "colors": alertario_precipitation_colors,
            "opacity": 0.1,
        },
        "map": {
            "type": "Heat map",
            "projection": "Geographical",
            "update_frequency": "Hourly",
            "spatial_resolution": "4 km x 4 km",
            "interpolation_method": "None",
            "additional_layers": [
                {
                    "type": "Topography",
                    "description": "Topografia adicionada para contexto geográfico",
                }
            ],
        },
    },
    RadarProductEnum.REFLECTIVITY: {
        "product": {
            "name": "Refletividade Horizontal - Radar do Mendanha",
            "description": "Produto gerado pelo radar meteorológico para medir a intensidade da precipitação, representando a quantidade de energia refletida por partículas de água presentes na atmosfera.",
            "unit": "dBZ",
            "source": "Radar Mete15orológico",
            "frequency": "5 Min",
        },
        "values_range": {"min": 15, "max": 50},
        "legend": {
            "title": "Refletividade de Radar",
            "colors": [
                {"value": 15, "color": "#5870f6"},
                {"value": 20, "color": "#069008"},
                {"value": 25, "color": "#0c6b11"},
                {"value": 30, "color": "#004803"},
                {"value": 35, "color": "#c3d500"},
                {"value": 40, "color": "#ff7800"},
                {"value": 45, "color": "#f61c00"},
                {"value": 50, "color": "#d11fcc"},
            ],
            "opacity": 0.8,
        },
        "map": {
            "type": "Heat map",
            "projection": "Geographical",
            "update_frequency": "5 Min",
            "interpolation_method": "Linear",
            "additional_layers": [
                {
                    "type": "Topography",
                    "description": "Topografia adicionada para contexto geográfico.",
                }
            ],
        },
    },
}
