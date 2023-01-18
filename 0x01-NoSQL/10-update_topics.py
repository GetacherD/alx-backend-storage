#!/usr/bin/env python3
"""
update in pymongo
"""


def update_topics(mongo_collection, name, topics):
    """ update record"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
