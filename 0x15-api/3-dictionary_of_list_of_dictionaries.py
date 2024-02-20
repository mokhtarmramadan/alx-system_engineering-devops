#!/usr/bin/python3

"""
script that, using this REST API, for a given employee ID
returns information about his/her list progress """

import csv
import json
import requests
from sys import argv

if __name__ == '__main__':
    api_url = "https://jsonplaceholder.typicode.com/"
    employees = {}
    try:
        response = requests.get(api_url + "users/")
        if response.status_code == 200:
            users = response.json()
            for user in users:
                user_id = user['id']
                username = user['username']
                user_dict = {user_id: []}  
                response = requests.get(api_url + "todos?userId={}".format(user_id))
                if response.status_code == 200:
                    tasks = response.json()
                    for task in tasks:
                        user_dict[user_id].append({'username': username, 'task': task['title'], 'completed': task['completed']})
                else:
                    print("Fail {}".format(response.status_code))
                employees.update(user_dict)
            with open('todo_all_employees.json', 'w') as f:
                json.dump(employees, f)

        else:
            print("fail {}", response.status_code)

    except Exception as e:
        print("Error {}".format(e))
