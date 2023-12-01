#!/usr/bin/python3
"""
Python script that fetches a user ID from the GitHub API using provided credentials
"""
from requests import get, auth
import sys

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    
    username = sys.argv[1]
    user_password = sys.argv[2]

    response = get(url, auth=auth.HTTPBasicAuth(username, user_password))

    if response.status_code == 200:
        user_data = response.json()
        print(user_data.get('id'))
    else:
        print("Failed to retrieve user ID")

