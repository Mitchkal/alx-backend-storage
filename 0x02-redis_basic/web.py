#!/usr/bin/env python3
"""
module for get page function
"""
from functools import wraps
import redis
from requests import get
from typing import Callable


cache = redis.Redis()


def track_url(method: Callable) -> Callable:
    """
    count decorator
    """
    @wraps(method)
    def wrapper(url: str) -> str:
        """
        wrapper function
        """
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
    """
    gets a url page and returns the html
    """
    data = get(url)
    return data.text
