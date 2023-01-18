#!/usr/bin/env python3
"""
insert data with pymongo
"""


def insert_school(mongo_collection, **kwargs):
    """ insert all data passed as kwargs"""
    data = [{key: value} for key, value in kwargs.items()]
    mongo_collection.insert_many(data)
