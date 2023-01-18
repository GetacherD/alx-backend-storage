#!/usr/bin/env python3
"""
insert data with pymongo
"""


def insert_school(mongo_collection, **kwargs):
    """ insert all data passed as kwargs"""
    mongo_collection.insert_one(kwargs)
    res = mongo_collection.find().sort("_id", -1).limit(1)
    return list(res)[0]["_id"]
