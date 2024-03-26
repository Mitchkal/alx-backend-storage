#!/usr/bin/env python3
"""
module insert document to mongodb python
"""


def insert_school(mongo_collection, **kwargs):
    """
    inserts new document in collection
    based on kwrgs and returns _id
    """
    result = mongo_collection.insert_one(kwargs)

    return result.inserted_id
