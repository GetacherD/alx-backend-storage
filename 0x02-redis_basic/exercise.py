#!/usr/bin/env python3
"""
redis basics demo
"""
import redis
from typing import Union
from uuid import uuid4


class Cache:
    """ cache objects blue print"""

    def __init__(self):
        """initializee"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[bytes, float, int, str]) -> str:
        """ store cache object  """
        key = str(uuid4())
        if type(data) not in [bytes, str, int, float]:
            return ""
        self._redis.set(key, data)
        return key
