#!/usr/bin/python3
"""
Python script to export data in the JSON format.
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    id = int(argv[1])

    employee = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{id}').json()
    user_name = employee.get("username")

    todos = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{id}/todos').json()

    # Diccionario para almacenar las tareas del usuario
    tasks_dict = {f"{id}": []}

    for todo in todos:
        task_dict = {
            "task": todo["title"],
            "completed": todo["completed"],
            "username": user_name
        }
        tasks_dict[f"{id}"].append(task_dict)

    # Convierte a formato JSON
    json_data = json.dumps(tasks_dict)

    # Exporta los datos a un archivo JSON
    filename = f"{id}.json"
    with open(filename, mode='w') as file:
        file.write(json_data)
