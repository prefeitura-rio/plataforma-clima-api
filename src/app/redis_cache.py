# -*- coding: utf-8 -*-
from typing import List

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

    async def get_satellite_product_last_values(
        self,
        satellite_product: str,
    ) -> List:
        """
        Retrieves the last values for a given satellite product from Redis.

        Args:
            satellite_product (str): The name of the satellite product to
            retrieve values for.

        Returns:
            List: A list of the last values for the specified product.
        """
        return await self._cache.get(satellite_product.lower())


cache = Cache()
