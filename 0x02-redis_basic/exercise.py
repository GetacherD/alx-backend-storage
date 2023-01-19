#!/usr/bin/env python3
"""
redis basics demo
"""
from redis import Redis
from typing import Union, Callable, Optional
from uuid import uuid4
import json


class Cache:
    """ cache objects blue print"""

    def __init__(self):
        """initializee"""
        self._redis = Redis()
        self._redis.flushdb()

    def store(self, data: Union[bytes, float, int, str]) -> str:
        """ store cache object  """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable]) -> Union[str, bytes, int, float, None]:
        """ get value associated with the key"""
        val = self._redis.get(key)
        if (fn and val):
            return fn(val)
        return val

    def get_str(self, key: str) -> str:
        """ get str """
        val = self._redis.get(key)
        return str(val)

    def get_int(self, key: str) -> int:
        """ get int """
        val = self._redis.get(key)
        if (val):
            return int(val)
        return -1
