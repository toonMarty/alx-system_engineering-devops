#!/usr/bin/python3
"""
This python script Records all tasks from all employees
"""
if __name__ == "__main__":
    import json
    import requests

    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            u.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u.get("username")
            } for t in requests.get(url + "todos",
                                    params={"userId": u.get("id")}).json()]
            for u in user}, jsonfile)
