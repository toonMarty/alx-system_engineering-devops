#!/usr/bin/python3
"""
 This module contains a script that exports
 data in the JSON format.
"""

if __name__ == "__main__":
    import json
    import requests
    import sys

    employee_id = sys.argv[1]
    resource = "https://jsonplaceholder.typicode.com/"
    user = requests.get(resource + "users/{}".format(employee_id)).json()
    username = user.get("username")

    todos = requests.get(resource + "todos",
                         params={"userId": employee_id}).json()

    with open("{}.json".format(employee_id), "w") as jsonfile:
        json.dump({employee_id: [{"task": t.get("title"),
                                  "completed": t.get("completed"),
                                  "username": username}
                                 for t in todos]}, jsonfile)
