#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
from sys import argv


if __name__ == "__main__":
    id = int(argv[1])
    name = str
    total_tasks = 0
    completed_tasks = 0
    completed_tasks_titles = []

    response = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(id)
    )
    if response.status_code == 200:
        json_data = response.json()
        name = json_data['name']
    else:
        print("Error:", response.status_code)

    response = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(id)
    )
    if response.status_code == 200:
        json_data = response.json()
        for todo in json_data:
            if todo['completed']:
                completed_tasks += 1
                completed_tasks_titles.append(todo['title'])
            total_tasks += 1
    else:
        print("Error:", response.status_code)

    print(
        "Employee",
        name,
        f"is done with tasks ({completed_tasks}/{total_tasks}):"
    )
    for title in completed_tasks_titles:
        print("\t" + title)
