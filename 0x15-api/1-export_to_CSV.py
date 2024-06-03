#!/usr/bin/python3

"""
a script that uses restul API to return the
info of an employee about his TODO list progress
"""
import csv
import json
import requests
import sys


class CustomDialect(csv.excel):
    quoting = csv.QUOTE_ALL


def todolistGet(id):
    """function that defines the endpoints and retrieves data"""

    # url
    url = "https://jsonplaceholder.typicode.com"

    # endpoints
    user_url = "{}/users/{}".format(url, str(id))
    todo_url = "{}/todos".format(user_url)

    # get the data
    user_response = requests.get(user_url)
    user = user_response.json()
    todo_response = requests.get(todo_url)
    todo = todo_response.json()

    # exporting to csv
    with open(str(id) + ".csv", "w", encoding="utf8") as file:
        exporter = csv.writer(file, delimiter=",", quotechar="'")
        for task in todo:
            task_completed = "True" if task.get("completed") else "False"
            exporter.writerow(
                [
                    json.dumps(id),
                    json.dumps(user.get("username")),
                    json.dumps(task_completed),
                    json.dumps(task.get("title")),
                ]
            )


if __name__ == "__main__":
    employee_id = sys.argv[1]
    todolistGet(employee_id)
