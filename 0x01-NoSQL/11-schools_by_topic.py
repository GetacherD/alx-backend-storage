#!/usr/bin/env python3
"""
Get list of records
"""


def schools_by_topic(mongo_collection, topic):
    """ Get List of records"""
    return list(mongo_collection.find({"topics": topic}))
