#!/usr/bin/python3

""" Queries the Reddit API and prints a sorted count of given keywords """

import requests
import re
from collections import Counter

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
           'AppleWebKit/537.36'
           '(KHTML, like Gecko)'
           'Chrome/58.0.3029.110'
           'Safari/537.36'}


def count_words(subreddit, word_list, count_dict=None):
    """ Queries the Reddit API and prints a sorted count of given keywords """
    if count_dict is None:
        count_dict = Counter()

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        if response.status_code == 404:
            return None
        else:
            return count_dict

    data = response.json()['data']
    children = data['children']

    for child in children:
        title = child['data']['title']
        words = re.findall(r'\b[a-z]+\b', title.lower())
        for word in word_list:
            if word.lower() in words:
                count_dict[word.lower()] += words.count(word.lower())

    if data['after'] is not None:
        return count_words(subreddit, word_list, count_dict=count_dict)
    else:
        sorted_count = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
        for item in sorted_count:
            print(item[0], item[1])
