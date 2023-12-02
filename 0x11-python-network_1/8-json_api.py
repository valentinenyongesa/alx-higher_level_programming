#!/usr/bin/python3
"""Search API"""
import requests
import sys

def search_user(letter):
    """search a post request"""
    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': letter}

    try:
        response = requests.post(url, data=data)
        response.raise_for_status()

        result = response.json()

        if result:
            print("[{}] {}".format(result.get('id'), result.get('name')))
        else:
            print("No result")

    except requests.exception.HTTPError:
        print("No result")
    except ValueError:
        print("Not a valid JSON")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        letter = sys.argv[1]
    else:
        letter = ""
    search_user(letter)
