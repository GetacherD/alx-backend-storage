#!/usr/bin/env python3
"""
redis basics demo
"""
from redis import Redis
from typing import Union
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
