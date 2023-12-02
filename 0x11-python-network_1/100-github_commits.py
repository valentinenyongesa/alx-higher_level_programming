#!/usr/bin/python3
"""Python script for an interview"""

import requests
import sys

def get_commits(repo, owner):
    """Describes a repo owner"""
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    params = {'per_page': 10}

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()

        commits = response.json()

        for commit in commits:
            sha = commit.get('sha')
            author_name = commit.get('commit', {}).get('author', {}).get('name')
            print(f"{sha}: {author_name}")
    except requests.exceptions.HTTPError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) == 3:
        repository = sys.argv[1]
        owner = sys.argv[2]
