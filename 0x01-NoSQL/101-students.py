#!/usr/bin/env python3
"""
sort demo
"""


def top_students(mongo_collection):
    """ get sorted top records """
    data = list(mongo_collection.aggregate(
        [{"$unwind": "$topics"}, {"$group": {
            "_id": "$name",  "averageScore": {
                "$avg": "$topics.score"}}}, {
                    "$sort": {"averageScore": -1}}]))
    ls = [{"_id": list(mongo_collection.find(
        {"name": i["_id"]}, {"_id": 1}))[0].get("_id"),
        "name": i["_id"], "averageScore":i["averageScore"]} for i in data]
    return ls
