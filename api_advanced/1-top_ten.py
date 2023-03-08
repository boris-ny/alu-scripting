#!/usr/bin/python3
"""
Top Ten
"""
import requests


def top_ten(subreddit):
    """
    Titles function
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        for i in range(min(10, len(posts))):
            print(posts[i]["data"]["title"])
    else:
        print(None)
