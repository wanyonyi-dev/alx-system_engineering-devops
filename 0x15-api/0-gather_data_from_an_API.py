#!/usr/bin/python3
"""
a script that uses restul API to return the
info of an employee about his TODO list progress
"""
import requests
from sys import argv


def todolistGet(id):
    """function that defines the endpoints and retrieves data"""
    # url
    url = "https://jsonplaceholder.typicode.com"

    # endpoints
    user = f"{url}/users/{id}"
    todo = f"{url}/todos?userId={id}"
    task_done = f"{url}/todos?userId={id}&completed=true"

    # get the data
    user_data = requests.get(user).json()
    todo_data = requests.get(todo).json()
    task_done_data = requests.get(task_done).json()

    lentodo = len(todo_data)
    lentask = len(task_done_data)

    print(
        "Employee {} is done with tasks({}/{}):".format(
            user_data.get("name"), lentask, lentodo
        )
    )
    # printing the titles of the completed tasks
    for task in task_done_data:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    todolistGet(argv[1])
