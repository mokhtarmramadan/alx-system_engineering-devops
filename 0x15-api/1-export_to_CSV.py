#!/usr/bin/python3

"""
script that, using this REST API, for a given employee ID
returns information about his/her list progress """

import csv
import requests
from sys import argv

if __name__ == '__main__':
    api_url = "https://jsonplaceholder.typicode.com/"
    user_id = argv[1]
    try:
        response = requests.get(api_url + "users/{}".format(user_id))
        if response.status_code == 200:
            users = response.json()
            user_name = users['username']
            response = requests.get(api_url +
                                    "todos?userId={}".format(user_id))

            if response.status_code == 200:
                tasks = response.json()
                csv_file = '{}.csv'.format(user_id)

                with open(csv_file, 'w', newline='') as f:
                    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
                    for task in tasks:
                        row = []
                        row.append(user_id)
                        row.append(user_name)
                        row.append(task['completed'])
                        row.append(task['title'])

                        writer.writerow(row)
            else:
                print("fail {}", response.status_code)

        else:
            print("Fail {}".format(response.status_code))
    except Exception as e:
        print("Error {}".format(e))
