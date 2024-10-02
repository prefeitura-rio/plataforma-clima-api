# -*- coding: utf-8 -*-
from os import getenv
from typing import List

from infisical import InfisicalClient
from loguru import logger

from app.enums import SatelliteProductEnum


def getenv_or_action(
    env_name: str, *, action: str = "raise", default: str = None
) -> str:
    """Get an environment variable or raise an exception.

    Args:
        env_name (str): The name of the environment variable.
        action (str, optional): The action to take if the environment variable is not set.
            Defaults to "raise".
        default (str, optional): The default value to return if the environment variable is not set.
            Defaults to None.

    Raises:
        ValueError: If the action is not one of "raise", "warn", or "ignore".

    Returns:
        str: The value of the environment variable, or the default value if the environment variable
            is not set.
    """
    if action not in ["raise", "warn", "ignore"]:
        raise ValueError("action must be one of 'raise', 'warn', or 'ignore'")

    value = getenv(env_name, default)
    if value is None:
        if action == "raise":
            raise EnvironmentError(f"Environment variable {env_name} is not set.")
        elif action == "warn":
            logger.warning(f"Warning: Environment variable {env_name} is not set.")
    return value


def getenv_list_or_action(
    env_name: str, *, action: str = "raise", default: str = None
) -> List[str]:
    """Get an environment variable or raise an exception.

    Args:
        env_name (str): The name of the environment variable.
        action (str, optional): The action to take if the environment variable is not set.
            Defaults to "raise".
        default (str, optional): The default value to return if the environment variable is not set.
            Defaults to None.

    Raises:
        ValueError: If the action is not one of "raise", "warn", or "ignore".

    Returns:
        str: The value of the environment variable, or the default value if the environment variable
            is not set.
    """
    value = getenv_or_action(env_name, action=action, default=default)
    if value is not None:
        if isinstance(value, str):
            return value.split(",")
        elif isinstance(value, list):
            return value
        else:
            raise TypeError("value must be a string or a list")
    return []


def inject_environment_variables(environment: str):
    """Inject environment variables from Infisical."""
    site_url = getenv_or_action("INFISICAL_ADDRESS", action="raise")
    token = getenv_or_action("INFISICAL_TOKEN", action="raise")
    infisical_client = InfisicalClient(
        token=token,
        site_url=site_url,
    )
    secrets = infisical_client.get_all_secrets(
        environment=environment, attach_to_os_environ=True
    )
    logger.info(f"Injecting {len(secrets)} environment variables from Infisical:")
    for secret in secrets:
        logger.info(f" - {secret.secret_name}: {mask_string(secret.secret_value)}")


def mask_string(string: str, *, mask: str = "*") -> str:
    """Mask a string with a specified character, but keep some characters visible so we can
    identify the string when we know what it should be. If the length of the string is less than
    3, only the last character is masked.

    Args:
        string (str): The string to mask.
        mask (str, optional): The character to use for masking. Defaults to "*".

    Returns:
        str: The masked string.
    """
    if len(string) < 3:
        return string[:-1] + mask
    return string[0] + mask * (len(string) - 2) + string[-1]


environment = getenv_or_action("ENVIRONMENT", action="warn", default="dev")
if environment not in ["dev", "staging", "prod"]:
    raise ValueError("ENVIRONMENT must be one of 'dev', 'staging' or 'prod'")

inject_environment_variables(environment=environment)

# Actual configs
ALLOW_CREDENTIALS = (
    getenv_or_action("ALLOW_CREDENTIALS", default="true").lower() == "true"
)
ALLOWED_HEADERS = getenv_list_or_action("ALLOWED_HEADERS", default="*")
ALLOWED_METHODS = getenv_list_or_action("ALLOWED_METHODS", default="*")
ALLOWED_ORIGINS = getenv_list_or_action("ALLOWED_ORIGINS", default="*")
ALLOWED_ORIGINS_REGEX = getenv_or_action("ALLOWED_ORIGINS_REGEX", action="ignore")
BIGQUERY_TABLE_INDICE_ESTABILIDADE = getenv_or_action(
    "BIGQUERY_TABLE_INDICE_ESTABILIDADE"
)
BIGQUERY_TABLE_METRICAS_GEOESPACIAIS = getenv_or_action(
    "BIGQUERY_TABLE_METRICAS_GEOESPACIAIS"
)
BIGQUERY_TABLE_TAXA_PRECIPITACAO = getenv_or_action("BIGQUERY_TABLE_TAXA_PRECIPITACAO")
BIGQUERY_TABLE_TEMPERATURA_OCEANO = getenv_or_action(
    "BIGQUERY_TABLE_TEMPERATURA_OCEANO"
)
GCP_SERVICE_ACCOUNT_CREDENTIALS = getenv_or_action("GCP_SERVICE_ACCOUNT_CREDENTIALS")
GOOGLE_BIGQUERY_PAGE_SIZE = int(
    getenv_or_action("GOOGLE_BIGQUERY_PAGE_SIZE", default="10000")
)
LOG_LEVEL = getenv_or_action("LOG_LEVEL", default="INFO")
RADAR_DATA_MAX_ALLOWED_RANGE_SECONDS = int(
    getenv_or_action("RADAR_DATA_MAX_ALLOWED_RANGE_SECONDS", default="86400")
)
REDIS_HOST = getenv_or_action("REDIS_HOST", default="localhost")
REDIS_PORT = int(getenv_or_action("REDIS_PORT", default="6379"))
REDIS_DB = int(getenv_or_action("REDIS_DB", default="0"))
REDIS_PASSWORD = getenv_or_action("REDIS_PASSWORD", action="ignore")
SATELLITE_GIF_MAX_ALLOWED_RANGE_SECONDS = int(
    getenv_or_action("SATELLITE_GIF_MAX_ALLOWED_RANGE_SECONDS", default="86400")
)
SATELLITE_PRODUCTS_MAPPING = {
    SatelliteProductEnum.CAPE: {
        "column": "cape",
        "gcs_prefix": "CAPE",
    },
    SatelliteProductEnum.K_INDEX: {
        "column": "ki",
        "gcs_prefix": "KI",
    },
    SatelliteProductEnum.SHOWALTER_INDEX: {
        "column": "si",
        "gcs_prefix": "SI",
    },
    SatelliteProductEnum.LIFTED_INDEX: {
        "column": "li",
        "gcs_prefix": "LI",
    },
    SatelliteProductEnum.TOTALS_TOTALS_INDEX: {
        "column": "tt",
        "gcs_prefix": "TT",
    },
    SatelliteProductEnum.RAIN_RATE: {
        "column": "rr",
        "gcs_prefix": "RR",
    },
    SatelliteProductEnum.OCEAN_TEMPERATURE: {
        "column": "sst",
        "gcs_prefix": "SST",
    },
}
SENTRY_ENABLE = getenv_or_action("SENTRY_ENABLE", default="false").lower() == "true"
TIMEZONE = getenv_or_action("TIMEZONE", default="America/Sao_Paulo")
if SENTRY_ENABLE:
    SENTRY_DSN = getenv_or_action("SENTRY_DSN")
    SENTRY_ENVIRONMENT = getenv_or_action("SENTRY_ENVIRONMENT")
else:
    SENTRY_DSN = None
    SENTRY_ENVIRONMENT = None
