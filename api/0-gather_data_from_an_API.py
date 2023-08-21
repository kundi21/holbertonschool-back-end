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
    url = "https://jsonplaceholder.typicode.com/todos"
    user_id = int(sys.argv[1])
    response = requests.get(url)
    todos = response.json()
    completed_tasks = 0
    count_tasks = 0

    for todo in todos:
        if todo.get('userId') == int(user_id):
            count_tasks += 1
            if todo.get('completed') is True:
                completed_tasks += 1
                print("\t {}".format(todo.get('title')))

    print("Employee {} is done with tasks ({}/{})".format
          (user_id, completed_tasks, count_tasks))
