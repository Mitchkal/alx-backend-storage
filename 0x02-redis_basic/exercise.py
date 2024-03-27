#!/usr/bin/env python3
"""
module exercise
classes and writing strings to Redis
"""

import uuid
import redis


class Cache:
    """
    class definition for cache
    """

    def __init__(self) -> None:
        """
        store instance of redis clien
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: str | bytes | int | float) -> str:
        """
        takes a data argument and returns a string
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
