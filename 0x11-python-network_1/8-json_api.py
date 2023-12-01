#!/usr/bin/python3
"""
Python script to send a POST request with a letter as a parameter to a URL
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        letter = ""
    else:
        letter = sys.argv[1]

    data = {'q': letter}
    url = 'http://0.0.0.0:5000/search_user'

    try:
        response = requests.post(url, data=data)
        json_response = response.json()

        if json_response:
            print(f"[{json_response.get('id')}] {json_response.get('name')}")
        else:
            print("No result")
    except requests.RequestException as e:
        print(f"Request failed: {e}")
    except ValueError:
        print("Not a valid JSON")

