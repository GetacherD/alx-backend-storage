#!/usr/bin/env python3
"""
redis basics demo
"""
import redis
from typing import Any
from uuid import uuid4


class Cache:
    """ cache objects blue print"""

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Any) -> str:
        """ store cache object """
        key = str(uuid4())
        self._redis.set(key, data)
        return key
