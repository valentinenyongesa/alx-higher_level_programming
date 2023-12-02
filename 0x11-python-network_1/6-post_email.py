#!/usr/bin/python3
"""Post an Email"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 3:
        url = sys.argv[1]
        email = sys.argv[2]

        data = {'email':email}

        try:
            response = requests.post(url, data=data)
            print("Your email is:", response.text)
        except Exception as e:
            print("Error:", e)
    else:
        print("Usage: ./6-post_email.py <URL> <email>")
