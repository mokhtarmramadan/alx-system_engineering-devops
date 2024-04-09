#!/usr/bin/python3
''' Script that queries reddits API '''
import requests
import json


def number_of_subscribers(subreddit):
    ''' Returns the number of subscribers for a given subreddit '''
    header = {'User-Agent': 'script1.0/by/mokhtarm.ramadan'}
    resource = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(resource, header, allow_redirects=False)

    if response.status_code == 200:
        subreddit_info = response.json()

        subreddit_data = subreddit_info.get('data', 0)
        if subreddit_data == 0:
            return 0
        subreddit_subs = subreddit_data['subscribers']
        return subreddit_subs

    else:
        return 0
