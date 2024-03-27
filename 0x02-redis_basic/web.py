#!/usr/bin/env python3
"""
module for get page function
"""

import redis
from requests import get
from functools import wraps
from typing import Callable


cache = redis.Redis()


def track_url(method: Callable) -> Callable:
    """
    count decorator
    """
    @wraps(method)
    def wrapper(url: str) -> str:
        key = f"count:{url}"

        cache.incr(key)
        cache_content = cache.get(key)

        if cache_content:
            return cache_content.decode('utf-8')

        html = method(url)
        cache.setex(key, 10, html)
        return html
    return wrapper


@track_url
def get_page(url: str) -> str:
    data = get(url)
    return data.text
