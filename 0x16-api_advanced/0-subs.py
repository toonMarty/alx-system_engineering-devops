#!/usr/bin/python3
"""
This module contains a function that
that queries the Reddit API and returns
the number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """
    This function queries the Reddit API
    and returns the number of subscribers
    Args:
        subreddit: a subreddit
    Returns:
        int: the number of subscribers
        (not active users, total subscribers)
        If an invalid subreddit is given, the function returns 0.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
