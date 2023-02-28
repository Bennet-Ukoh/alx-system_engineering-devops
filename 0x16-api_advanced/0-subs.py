#!/usr/bin/python3
"""
number of subscribers for a given subreddit
"""

# Import the requests library, which allows us to send HTTP requests
import requests

# Define a function called number_of_subscribers that takes a subreddit name as input
def number_of_subscribers(subreddit):
    # Construct the URL for the subreddit's about.json endpoint
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Define a custom user agent for the HTTP request (required by Reddit API)
    headers = {'User-Agent': 'Google Chrome Version 81.0.4044.129'}
    
    # Send a GET request to the URL with the custom user agent header
    response = requests.get(url, headers=headers)
    
    # If the response status code is 200 (OK), parse the JSON response and extract the number of subscribers
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    
    # If the response status code is not 200, return 0 (invalid subreddit)
    else:
        return 0

