#!/usr/bin/python3
"""
task #2. Export to Json
Using what you did in task #0,
extend your Python script to export data in the JSON format.
"""
import json
import requests
import sys

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
    todo_all_employees = {}
    for todo in todos_data:
        todo_all_employees[todo.get("userId")] = [{
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": user_data.get("username")
        }]
        with open("todo_all_employees.json", "w") as f:
            json.dump(todo_all_employees, f)
            f.close()
    