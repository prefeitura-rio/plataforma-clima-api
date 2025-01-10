# -*- coding: utf-8 -*-
# flake8: noqa: E501
import json
import pickle
from typing import List

from fastapi import HTTPException
from loguru import logger
from redis.asyncio import Redis

from app import config


class Cache:
    def __init__(self) -> None:
        self._cache = Redis(
            host=config.REDIS_HOST,
            port=config.REDIS_PORT,
            db=config.REDIS_DB,
            password=config.REDIS_PASSWORD,
        )

    async def get_data_from_redis(
        self,
        key: str,
    ) -> bytes:
        """
        Retrieves data from Redis for a given key.

        This method attempts to fetch data from Redis using the provided key.
        If the data is not found, it raises an HTTPException with a status
        code of 404.

        Args:
            key (str): The key to use for retrieving data from Redis.

        Returns:
            bytes: The data retrieved from Redis.

        Raises:
            HTTPException: If no data is found for the given key.
        """
        redis_data = await self._cache.get(key)
        if redis_data is None:
            raise HTTPException(status_code=404, detail=f"No data found for key {key}")
        return redis_data

    async def process_redis_data(self, key: str) -> List:
        """
        Processes data retrieved from Redis for a given key.

        This method attempts to decode and return the data from Redis using
        the provided key. It first tries to decode the data using pickle,
        and if that fails, it attempts to decode the data as JSON. If both
        attempts fail, it raises a ValueError.

        Args:
            key (str): The key to use for retrieving data from Redis.

        Returns:
            List: The decoded data from Redis.

        Raises:
            ValueError: If the data cannot be decoded from Redis.
        """
        redis_data = await self.get_data_from_redis(key)

        logger.info(f"Accessed redis key: {key}")
        logger.info(f"Type returned: {type(redis_data)}")
        logger.info(f"Values from redis: {redis_data}")

        try:
            return pickle.loads(redis_data)
        except (pickle.UnpicklingError, TypeError, EOFError):
            try:
                return json.loads(redis_data.decode("utf-8").replace("NaN", "null"))
            except (json.JSONDecodeError, UnicodeDecodeError):
                raise ValueError("Unable to decode data from Redis")


cache = Cache()
