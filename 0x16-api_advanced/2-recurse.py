#!/usr/bin/python3
''' Script that queries Reddit API '''
import json
import requests
import sys


def recurse(subreddit, host_list=[], after="null"):
    ''' Read reddit API and return top 10 hotspots '''
    headers = {'user-agent': 'redditscript1.0/by/mokhtarmramadan'}
    payload = {"limit": "100", "after": after}
    resource = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    response = requests.get(resource, headers=headers, params=payload)

    if response.status_code == 200:
        list_titles = response.json()['data']['children']
        after = response.json()['data']['after']
        if after is not None:
            host_list.append(list_titles[len(host_list)]['data']['title'])
            recurse(subreddit, host_list, after)
        else:
            return(host_list)
    else:
        return(None)
