#!/usr/bin/python3

""" Queries the Reddit API and prints the titles of all hot articles """

import requests


def recurse(subreddit, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": 100}

    if after:
        params["after"] = after

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]

        for post in posts:
            hot_list.append(post["data"]["title"])

        after = data["data"]["after"]

        if after is not None:
            recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
