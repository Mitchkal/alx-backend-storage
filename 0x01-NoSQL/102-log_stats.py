#!/usr/bin/env python3
"""
module log stats
with aggreagate pipeline
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
        print(f"\tmethod {method}: {method_count}")

    stats = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{stats} status check")

    pipeline = [
            {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
            {"$sort": {"count": -1}},
            {"$limit": 10}
    ]
    top_ips = collection.aggregate(pipeline)
    print("IPs:")

    for index, ip in enumerate(top_ips, start=1):
        print(f"\t{ip['_id']}: {ip['count']}")


if __name__ == "__main__":
    """
    run
    """
    nginx_logs_status()
