#!/usr/bin/env python3
"""
module change school topics
"""


def update_topics(mongo_collection, name, topics):
    """
    changes all topics of school document
    based on name
    """
    mongo_collection.update_many(
            {"name": name},
            {"$set": {"topics": topics}}
    )