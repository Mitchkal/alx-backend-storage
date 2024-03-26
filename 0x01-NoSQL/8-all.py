#!/usr/bin/env python3
"""
module list mongo documents
"""


def list_all(mongo_collection):
    """
    lists all documents in a collection
    or returns an empty list if not in
    collection
    """
    return [item for item in mongo_collection.find()]
