#!/usr/bin/python3
"""Display GitHub id"""
import requests
import sys

def get_user_id(username, token):
    """Gets the username and token"""

    url = 'https://api.github.com/user'

    try:
        response = requests.get(url, auth=(username, token))
        response.raise_for_status()

        return user_id
    except requests.exceptions.HTTPError:
        return None
    except ValueError:
        print()

if __name__ == "__main__":
    if len(sys.argv) == 3:
        username = sys.argv[1]
        token = sys.argv[2]

        user_id = get_user_id(username, token)

        if user_id is not None:
            print(user_id)
        else:
            print("None")
    else:
        print("Usage: ./10-my_github.py <username> <token>")
