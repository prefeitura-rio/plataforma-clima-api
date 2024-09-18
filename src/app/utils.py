# -*- coding: utf-8 -*-
import base64
import os
from datetime import datetime
from pathlib import Path
from typing import List, Tuple

import cartopy.crs as ccrs
import cartopy.io.shapereader as shpreader
import fiona
import matplotlib.pyplot as plt
import numpy as np
import orjson as json
import pandas as pd
import xarray as xr
from fastapi import HTTPException
from google.cloud import bigquery
from google.cloud.bigquery.query import _AbstractQueryParameter
from google.oauth2 import service_account
from loguru import logger
from pendulum import DateTime

from app import config


def create_and_save_image(data: xr.DataArray, info: dict, variable) -> Path:
    """
    Create image from xarray ans save it as png file.
    """

    plt.figure(figsize=(10, 10))

    # Use the Geostationary projection in cartopy
    axis = plt.axes(projection=ccrs.PlateCarree())

    extent = info["extent"]
    img_extent = [extent[0], extent[2], extent[1], extent[3]]

    # Define the color scale based on the channel
    colormap = "jet"  # White to black for IR channels
    # colormap = "gray_r" # White to black for IR channels

    # Plot the image
    img = axis.imshow(data, origin="upper", extent=img_extent, cmap=colormap, alpha=0.8)

    # # Find shapefile file "Limite_Bairros_RJ.shp" across the entire file system
    # for root, dirs, files in os.walk(os.sep):
    #     if "Limite_Bairros_RJ.shp" in files:
    #         logger.info(f"[DEBUG] ROOT {root}")
    #         shapefile_dir = root
    #         break
    # else:
    #     print("File not found.")

    # Add coastlines, borders and gridlines
    shapefile_dir = Path(
        "/opt/venv/lib/python3.9/site-packages/pipelines/utils/shapefiles"
    )
    shapefile_path_neighborhood = shapefile_dir / "Limite_Bairros_RJ.shp"
    shapefile_path_state = shapefile_dir / "Limite_Estados_BR_IBGE.shp"

    logger.info("\nImporting shapefiles")
    fiona.os.environ["SHAPE_RESTORE_SHX"] = "YES"
    reader_neighborhood = shpreader.Reader(shapefile_path_neighborhood)
    reader_state = shpreader.Reader(shapefile_path_state)
    state = [record.geometry for record in reader_state.records()]
    neighborhood = [record.geometry for record in reader_neighborhood.records()]
    logger.info("\nShapefiles imported")
    axis.add_geometries(
        state, ccrs.PlateCarree(), facecolor="none", edgecolor="black", linewidth=0.7
    )
    axis.add_geometries(
        neighborhood,
        ccrs.PlateCarree(),
        facecolor="none",
        edgecolor="black",
        linewidth=0.2,
    )
    # axis.coastlines(resolution='10m', color='black', linewidth=1.0)
    # axis.add_feature(cartopy.feature.BORDERS, edgecolor='black', linewidth=1.0)
    grdln = axis.gridlines(
        crs=ccrs.PlateCarree(),
        color="gray",
        alpha=0.7,
        linestyle="--",
        linewidth=0.7,
        xlocs=np.arange(-180, 180, 1),
        ylocs=np.arange(-90, 90, 1),
        draw_labels=True,
    )
    grdln.top_labels = False
    grdln.right_labels = False

    plt.colorbar(
        img,
        label=variable.upper(),
        extend="both",
        orientation="horizontal",
        pad=0.05,
        fraction=0.05,
    )

    logger.info("\n Start saving image")
    output_image_path = Path(os.getcwd()) / "output" / "images"

    save_image_path = output_image_path / (f"{variable}_{info['datetime_save']}.png")

    if not output_image_path.exists():
        output_image_path.mkdir(parents=True, exist_ok=True)

    plt.savefig(save_image_path, bbox_inches="tight", pad_inches=0, dpi=300)
    logger.info("\n Ended saving image")
    return save_image_path


def get_bigquery_client() -> bigquery.Client:
    """Get the BigQuery client.

    Returns:
        bigquery.Client: The BigQuery client.
    """
    credentials = get_gcp_credentials()
    return bigquery.Client(credentials=credentials, project=credentials.project_id)


def get_data_from_bigquery(
    query: str,
    query_params: List[_AbstractQueryParameter] = None,
    bigquery_client: bigquery.Client = None,
) -> pd.DataFrame:
    bq_client = bigquery_client or get_bigquery_client()
    job_config = bigquery.QueryJobConfig(query_parameters=query_params)
    query_job = bq_client.query(query, job_config=job_config)
    return query_job.to_dataframe()


def get_gcp_credentials(scopes: List[str] = None) -> service_account.Credentials:
    """Get the GCP credentials.

    Args:
        scopes (List[str], optional): The scopes to use. Defaults to None.

    Returns:
        service_account.Credentials: The GCP credentials.
    """
    info: dict = json.loads(base64.b64decode(config.GCP_SERVICE_ACCOUNT_CREDENTIALS))
    creds = service_account.Credentials.from_service_account_info(info)
    if scopes:
        creds = creds.with_scopes(scopes)
    return creds


def parse_datetime_to_pendulum_datetime(datetime: datetime) -> DateTime:
    dt = DateTime.instance(datetime)
    dt = dt.in_tz(config.TIMEZONE)
    return dt


def sanity_check_time_range(
    start_time: datetime, end_time: datetime, max_allowed_range_seconds: int = None
) -> Tuple[DateTime, DateTime]:
    # Parse start_time and end_time to pendulum.DateTime
    start_time = parse_datetime_to_pendulum_datetime(start_time)
    end_time = parse_datetime_to_pendulum_datetime(end_time)

    # Assert that the start time is before the end time
    if start_time >= end_time:
        raise HTTPException(
            status_code=400, detail="The start time must be before the end time."
        )

    # Assert that both times are in the past
    now = DateTime.now(tz=config.TIMEZONE)
    if start_time >= now or end_time >= now:
        raise HTTPException(
            status_code=400, detail="Both start and end times must be in the past."
        )

    # Assert that the time range is less or equal to the allowed range
    if max_allowed_range_seconds:
        if end_time.diff(start_time).in_seconds() > max_allowed_range_seconds:
            raise HTTPException(
                status_code=400,
                detail=f"The time range is too large. Must be less than or equal to {max_allowed_range_seconds} seconds.",
            )

    return start_time, end_time
