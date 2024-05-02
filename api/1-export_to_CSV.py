#!/usr/bin/python3
"""
Python script to export data in the CSV format.
"""
import csv
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
        name = json_data['username']
    else:
        print("Error:", response.status_code)

    response = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(id)
    )
    if response.status_code == 200:
        json_data = response.json()
    else:
        print("Error:", response.status_code)


# Exportar los datos a un archivo CSV
    filename = f"{id}.csv"
    with open(filename, mode='w') as file:
        for todo in json_data:
            file.write('"{}","{}","{}","{}"\n'
                       .format(id, name, todo["completed"], todo["title"]))
