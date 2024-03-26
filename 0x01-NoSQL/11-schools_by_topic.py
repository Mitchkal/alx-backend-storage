#!/usr/bin/env python3
"""
module list of schools by topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    return list of schools by topic
    """
    return [item for item in mongo_collection.find({"topics": topic})]
