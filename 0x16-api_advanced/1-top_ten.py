#!/usr/bin/python3
''' Script that queries reddits API '''
import requests


def top_ten(subreddit):
    ''' prints the titles of the first 10 hot posts listed
     for a given subreddit '''
    header = {'User-Agent': "script1.1/by/mokhtarmramadan"}
    resource = f'https://www.reddit.com/r/{subreddit}/top.json?limit=10'

    response = requests.get(resource, header, allow_redirects=False)

    if response.status_code == 200:
        response = response.json()

        posts = response['data']['children']
        for post in posts:
            print(post['data']['title'])
    else:
        return 0
