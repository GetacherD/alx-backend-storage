#!/usr/bin/env python3
"""
redis basics demo
"""
import redis
from typing import Union, Callable, Optional
from uuid import uuid4
import json
from functools import wraps


def call_history(method: Callable) -> Callable:
    """store history of function input and out put"""
    key = method.__qualname__
    inputs = key + ":inputs"
    outputs = key + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper function"""
        self._redis.rpush(inputs, str(args))
        data = method(self, *args, **kwargs)
        self._redis.rpush(outputs, str(data))
        return data
    return wrapper


def count_calls(method: Callable) -> Callable:
    """ Count number of calls of a function"""
    key = method.__qualname__

    @wraps(method)
    def wrappers(self, *args, **kwargs):
        "wrapped function"
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrappers


class Cache:
    """ cache objects blue print"""

    def __init__(self):
        """initializee"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ store cache object  """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: Optional,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """ get value associated with the key"""
        val = self._redis.get(key)
        if fn:
            return fn(val)
        return val

    def get_str(self, key: str) -> str:
        """ get str """
        val = self._redis.get(key)
        return val.decode("utf-8")

    def get_int(self, key: str) -> int:
        """ get int """
        val = self._redis.get(key)
        try:
            data = int(val)
        except Exception:
            data = 0
        return data
