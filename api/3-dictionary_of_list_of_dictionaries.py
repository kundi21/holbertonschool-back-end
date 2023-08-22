#!/usr/bin/python3
"""
task #2. Using what you did in the task #0, extend your
Python script to export data in the JSON format.
"""
import csv
import json
import requests
import sys
import urllib.request

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
    completed_tasks = 0
    total_tasks = 0
    count_tasks = 0
    employee_name = user_data.get("name")

    todo_all_employees,jsonfile = {}, {}
    file_name= open(f"{user_id}.json", "w")
    new_dict = {user_id: []}
    for todo in todos_data:
        if todo["userId"] == user_id:
            new_dict[user_id].append({user_id: todo["userId"],
                                      "username": employee_name,
                                      "task": todo["title"],
                                      "completed": todo["completed"]})    
            if todo["completed"] is True:
                completed_tasks += 1
                new_dict[user_id].append{user_id: todo["userId"],
                                          "username": employee_name['username'],
                                          "task": todo["title"],
                                          "completed": todo["completed"],
                                          "username": employee_name['username'],
                                          "task": todo["title"],
                                          "completed": todo["completed"],
                                          "username": employee_name['username'],
                                          "task": todo["title"],
                                          "completed": todo["completed"],
                                          "username": employee_name['username'],
                                          "task": todo["title"],
                                          "completed": todo["completed"]
                                          }
                todo_all_employees[user_id] = new_dict[user_id]
                json.dump(todo_all_employees, file_name)
                file_name.close()
                print(todo_all_employees)

                