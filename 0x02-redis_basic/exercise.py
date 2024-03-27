#!/usr/bin/env python3
"""
module exercise
classes and writing strings to Redis
"""

import uuid
import redis
from typing import Union, Callable, Any


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

    def get(self, key: str, fn: Callable[[bytes], Any] = None) -> Any:
        """
        converts redis data back to desired format
        """
        data = self._redis.get(key)
        if data is not None and fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """
        gets a string data from redis storage
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """
        gets an integer data from redis storage
        """
        return self.get(key, fn=int)
