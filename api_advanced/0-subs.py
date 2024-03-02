#!/usr/bin/python3

"""This module pulls information about a subreddit's subscribers"""

import requests

def number_of_subscribers(subreddit):
    response = requests.get("https://www.reddit.com/r/{}/about.json".format(subreddit))
    if response.statuscode == 200:
        return response["subscribers"]
    else:
        return 0
