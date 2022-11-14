#!/usr/bin/python3
"""This module contains a Python script that, using this REST API,
for a given employee ID, returns information about
his/her TODO list progress.
"""

if __name__ == "__main__":
    import json
    import requests
    import sys

    response_API = requests.get('https://jsonplaceholder.typicode.com/todos')
    response_emp_API = \
        requests.get('https://jsonplaceholder.typicode.com/users')
    employee_id = int(sys.argv[1])
    number_of_done_tasks = 0
    total_number_of_tasks = 0

    data = response_API.text
    emp_data = response_emp_API.text

    parse_json = json.loads(data)
    parse_emp_json = json.loads(emp_data)

    for i in range(len(parse_json)):
        if parse_json[i]['userId'] == employee_id:
            if parse_json[i]['completed']:
                number_of_done_tasks += 1
                total_number_of_tasks += 1
            if not parse_json[i]['completed']:
                total_number_of_tasks += 1

    for i in range(len(parse_emp_json)):
        if parse_emp_json[i]['id'] == employee_id:
            print('Employee {} is done with tasks({}/{}):'.
                  format(parse_emp_json[i]['name'],
                         number_of_done_tasks,
                         total_number_of_tasks))

    for i in range(len(parse_json)):
        if parse_json[i]['userId'] == employee_id:
            if parse_json[i]['completed']:
                print('\t{}'.format(parse_json[i]['title']))
