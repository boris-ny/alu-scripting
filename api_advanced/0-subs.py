#!/usr/bin/python3
"""
0-subs

  Args:
      subreddit: The name of the subreddit to query.

    Returns:
      The number of subscribers for the subreddit, or 0 if the subreddit is \n
      invalid.
"""
import requests


def number_of_subscribers(subreddit):

    # Define the Reddit API endpoint for subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json?limit=0"

    # Set a custom User-Agent header to avoid "Too Many Requests" errors
    headers = {
        'User-Agent': 'my-reddit-app (https://github.com/boris-ny/alu)'}

    try:
        # Send a GET request to the API endpoint, following no redirects
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check for successful response (status code 200)
        if response.status_code == 200:
            data = response.json()
            # Extract the number of subscribers from the response data
            return data.get('data', {}).get('subscribers', 0)
        else:
            # Invalid subreddit or other error
            return 0
    except requests.exceptions.RequestException:
        # Handle any errors during the request
        return 0
