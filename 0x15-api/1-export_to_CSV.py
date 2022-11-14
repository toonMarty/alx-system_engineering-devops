#!/usr/bin/python3
"""This module exports API data
   to a CSV file
"""

if __name__ == "__main__":
    import csv
    import requests
    import sys

    emp_id = sys.argv[1]
    resource = "https://jsonplaceholder.typicode.com/"
    user = requests.get(resource + "users/{}".format(emp_id)).json()
    username = user.get("username")
    todos = requests.get(resource + "todos", params={"userId": emp_id}).json()

    with open("{}.csv".format(emp_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [emp_id, username, t.get("completed"), t.get("title")])
            for t in todos]
