#!/usr/bin/env python3
"""
List all data with pymongo
"""


def list_all(mongo_collection):
    """ get all data from mongo_collection"""
    return list(mongo_collection.find())
