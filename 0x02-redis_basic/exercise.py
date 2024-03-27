#!/usr/bin/env python3
"""
module exercise
classes and writing strings to Redis
"""

import uuid
import redis
from typing import Union


class Cache:
    """
    class definition for cache
    """

    def __init__(self) -> None:
        """
        cache intitialization
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        takes a data argument and returns a string
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
