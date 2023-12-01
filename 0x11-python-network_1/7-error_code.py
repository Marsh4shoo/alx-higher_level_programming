#!/usr/bin/python3
"""
Python script to handle HTTP response and display body or error code
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        response = requests.get(url)
        if response.ok:
            print(response.text)
        else:
            print(f"Error code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Request failed: {e}")

