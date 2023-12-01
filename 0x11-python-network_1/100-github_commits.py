#!/usr/bin/python3
"""
Python script that utilizes the GitHub API to list 10 commits
"""
import requests
import sys

if __name__ == '__main__':
    repository = sys.argv[1]
    user = sys.argv[2]
    url = f'https://api.github.com/repos/{user}/{repository}/commits'
    
    response = requests.get(url)

    try:
        commits = response.json()[:10]
        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    except (IndexError, KeyError):
        pass

