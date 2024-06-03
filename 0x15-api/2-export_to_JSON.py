#!/usr/bin/python3

"""
a script that uses restul API to return the
info of an employee about his TODO list progress
"""
import json
from sys import argv
import requests


def todolistGet(id):
    """function that defines the endpoints and retrieves data"""

    # url
    url = "https://jsonplaceholder.typicode.com"

    # endpoints
    user = "{}/users/{}".format(url, str(id))
    todo = "{}/todos".format(url)

    # get the data. making the request using get method and
    # specified format to be used
    user_response = requests.get(user)
    todo_response = requests.get(todo, params={"userId": id})

    if user_response.status_code == 200 and todo_response.status_code == 200:
        user_data = user_response.json()
        todo_data = todo_response.json()

        # exporting to json
        to_json = {}
        to_json[id] = []
        for task in todo_data:
            to_json[id].append(
                {
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": user_data.get("username"),
                }
            )
        with open(str(id) + ".json", "w", encoding="utf8") as file:
            json.dump(to_json, file)
    else:
        print("Error: Failed to retrieve data")


if __name__ == "__main__":
    todolistGet(argv[1])
