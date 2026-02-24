#!/usr/bin/python3
"""Export employee TODO data to JSON format."""
import json
import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    user = requests.get("{}/users/{}".format(base_url, employee_id)).json()
    todos = requests.get(
        "{}/todos?userId={}".format(base_url, employee_id)).json()

    username = user.get("username")
    filename = "{}.json".format(employee_id)

    tasks = []
    for task in todos:
        tasks.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    data = {str(employee_id): tasks}

    with open(filename, "w") as jsonfile:
        json.dump(data, jsonfile)