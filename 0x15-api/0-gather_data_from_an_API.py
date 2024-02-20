#!/usr/bin/python3

"""
script that, using this REST API, for a given employee ID
returns information about his/her list progress """

if __name__ == '__main__':
    import requests
    import json
    from sys import argv

    api_url = "https://jsonplaceholder.typicode.com/"
    user_id = argv[1]
    try:
        response = requests.get(api_url + "users/{}".format(user_id))
        if response.status_code == 200:
            users = response.json()
            user_name = users['name']
            response = requests.get(api_url +
                                    "todos?userId={}".format(user_id))

            if response.status_code == 200:
                tasks = response.json()
                total_tasks = len(tasks)
                completed_tasks_counter = 0
                completed_tasks = []
                for task in tasks:
                    if task['completed'] is True:
                        completed_tasks_counter += 1
                        completed_tasks.append(task['title'])
                print("Employee {} is done with tasks({}/{}):".format(
                        user_name, completed_tasks_counter, total_tasks))
                for title in completed_tasks:
                    print("   {}".format(title))
            else:
                print("fail {}", response.status_code)

        else:
            print("Fail {}".format(response.status_code))
    except Exception as e:
        print("Error {}".format(e))
