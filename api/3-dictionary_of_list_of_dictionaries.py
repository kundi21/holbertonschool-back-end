#!/usr/bin/python3
"""
task #3. Dictionary of list of dictionaries
Using what you did in task #0,
extend your Python script to export data in the JSON format.
"""
import json
import requests
import sys

if __name__ == "__main__":
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    users_url = "https://jsonplaceholder.typicode.com/users"

    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()
    users_response = requests.get(users_url)
    users_data = users_response.json()

    all_employee_tasks = {}

    for user in users_data:
        user_id = user["id"]
        username = user["username"]
        user_tasks = []

        for todo in todos_data:
            if todo["userId"] == user_id:
                user_tasks.append({
                    "task": todo["title"],
                    "completed": todo["completed"],
                    "username": username
                })

        all_employee_tasks[str(user_id)] = user_tasks

    filename = "todo_all_employees.json"

    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(all_employee_tasks, f, indent=4)
