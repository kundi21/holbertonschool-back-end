#!/usr/bin/python3
"""
task #1. Export to CSV
Using what you did in the task #0,
extend your Python script to export data in the CSV format.
"""
import csv
import json
import requests
import sys
import urllib

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    user_id = int(sys.argv[1])
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()
    user_response = requests.get(user_url)
    user_data = user_response.json()

    with open(f"{user_id}.csv", "w") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for todo in todos_data:
            if todo["userId"] == user_id:
                writer.writerow([user_id,
                                 user_data.get("username"),
                                 todo["completed"],
                                 todo["title"]])
