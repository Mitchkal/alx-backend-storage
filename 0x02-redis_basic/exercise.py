#!/usr/bin/env python3
"""
module exercise
classes and writing strings to Redis
"""

import uuid
import redis
from functools import wraps
from typing import Union, Callable, Any


def count_calls(method: Callable) -> Callable:
    """
    count number of calls to cache calls methods
    """
    @wraps(method)
    def wrapper(self, *args, **kwds):
        """
        wraps a method
        """

        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwds)

    return wrapper


def call_history(method: Callable) -> Callable:
    """
    stores history of inputs and outputs for function
    """
    key = method.__qualname__
    inputs = key + ":inputs"
    outputs = key + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        The wrapper function
        """
        self._redis.rpush(inputs, str(args))
        data = method(self, *args, **kwargs)
        self._redis.rpush(outputs, str(data))
        return data

    return wrapper


def replay(method: Callable) -> None:
    """
    displays history of calls for given function
    """
    name = method.__qualname__

    cache = redis.Redis()
    calls = cache.get(name).decode('utf-8')
    print(f"{name} was called {calls} times:")

    inputs = cache.lrange(name + ":inputs", 0, -1)
    outputs = cache.lrange(name + ":outputs", 0, -1)

    for i, o in zip(inputs, outputs):
        print(f"{name}(*{i.decode('utf-8')}) -> {o.decode('utf-8')}")


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

    @count_calls
    @call_history
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
