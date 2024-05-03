#!/usr/bin/python3
"""
Python script to export data in the JSON format.
"""
import json
import requests
from collections import defaultdict
from sys import argv


if __name__ == "__main__":
    # Obtener todos los usuarios
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()

    # Inicializar el diccionario de tareas
    all_tasks = defaultdict(list)

    # Iterar sobre cada usuario
    for user in users:
        user_id = user['id']
        user_name = user['username']

        # Obtener las tareas de cada usuario
        todos_url = (
             f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'
        )
        todos = requests.get(todos_url).json()

        # Agregar las tareas al diccionario
        for todo in todos:
            task_dict = {
                "username": user_name,
                "task": todo["title"],
                "completed": todo["completed"]
            }
            all_tasks[user_id].append(task_dict)

    # Exportar los datos a un archivo JSON
    filename = "todo_all_employees.json"
    with open(filename, mode='w') as file:
        json.dump(all_tasks, file)
