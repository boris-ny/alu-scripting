#!/usr/bin/python3
"""Return the number of subscribers of a given subreddit"""

import requests


def number_of_subscribers(subreddit):
    """function that fetches number_of_subscribers"""
    URL = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    HEADERS = {"User-Agent": "Mozilla/5.0"}

    try:
        RESPONSE = requests.get(URL, headers=HEADERS, allow_redirects=False)
        return RESPONSE.json().get("data").get("subscribers")

    except Exception as e:
        print("Error:", e)
        return 0


if __name__ == "__main__":
    subreddit = input("Enter the subreddit name: ")
    print("Number of subscribers:", number_of_subscribers(subreddit))
