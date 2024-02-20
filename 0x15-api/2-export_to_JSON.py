#!/usr/bin/python3

"""
script that, using this REST API, for a given employee ID
returns information about his/her list progress """

import csv
import requests
from sys import argv
import json

if __name__ == '__main__':
    api_url = "https://jsonplaceholder.typicode.com/"
    user_id = argv[1]
    data = {user_id: []}
    try:
        response = requests.get(api_url + "users/{}".format(user_id))
        if response.status_code == 200:
            users = response.json()
            user_name = users['username']
            response = requests.get(api_url +
                                    "todos?userId={}".format(user_id))

            if response.status_code == 200:
                tasks = response.json()
                json_file = '{}.json'.format(user_id)

                with open(json_file, 'w') as f:
                    for task in tasks:
                        data[user_id].append({'task': task['title'], 'completed': task['completed'], 'username': user_name})

                    json.dump(data, f)
            else:
                print("fail {}", response.status_code)

        else:
            print("Fail {}".format(response.status_code))
    except Exception as e:
        print("Error {}".format(e))
