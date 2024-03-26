#!/usr/bin/env python3
"""
module log stats
"""


from pymongo import MongoClient


def nginx_logs_status():
    """
    nginx log stats
    """
    client = MongoClient("mongodb://127.0.0.1:27017/")
    db = client["logs"]
    collection = db["nginx"]

    print(f"{collection.count_documents({})} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print("Methods:")
    for method in methods:
        method_count = collection.count_documents({"method": method})
        print(f"    method {method}: {method_count}")

    stats = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{stats} status check")


if __name__ == "__main__":
    """
    run
    """
    nginx_logs_status()
