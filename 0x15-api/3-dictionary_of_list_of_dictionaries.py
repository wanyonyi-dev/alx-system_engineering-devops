#!/usr/bin/python3

"""
a script that uses restul API to return the
info of an employee about his TODO list progress
"""
import json
import requests


def todolistGet():
    """function that defines the endpoints and retrieves data"""

    # url
    url = "https://jsonplaceholder.typicode.com"

    # endpoint to get users
    users_endpoint = "{}/users".format(url)

    # get the data. making the request using get method and specified
    # format to be used
    users_response = requests.get(users_endpoint)
    users_data = users_response.json()

    # exporting to json
    to_json = {}
    for user in users_data:
        to_json[user.get("id")] = []
        todo_endpoint = "{}/todos?userId={}".format(url, user.get("id"))
        todo_response = requests.get(todo_endpoint)
        todo_data = todo_response.json()
        for task in todo_data:
            to_json[user.get("id")].append(
                {
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": user.get("username"),
                }
            )

    with open("todo_all_employees.json", "w", encoding="utf8") as file:
        json.dump(to_json, file)


if __name__ == "__main__":
    todolistGet()
