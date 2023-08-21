#!/usr/bin/python3
"""
Gather data from an API.
Script that using jsonplaceholder.typicode.com API,
for a given employee ID,returns information about
his/her TODO list progress.
"""
import sys
import json
import urllib
import requests

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    url = "https://jsonplaceholder.typicode.com/todos"
    user_id = int(sys.argv[1])
    response = requests.get(url)
    todos_data = response.json()
    completed_tasks = 0
    total_tasks = len(todos_data)
    count_tasks = 0

    for todo in todos_data:
        if todo["userId"] == user_id:
            count_tasks += 1
            if todo["completed"] is True:
                completed_tasks += 1
    print("Employee {} is done with tasks({}/{}):"
          .format(user_id, completed_tasks, count_tasks))

    for todo in todos_data:
        if todo["userId"] == user_id and todo["completed"] is True:
            print("\t {}".format(todo["title"]))

