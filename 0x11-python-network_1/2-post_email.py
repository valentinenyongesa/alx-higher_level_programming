#!/usr/bin/python3
"""Sends a post request to the passed URL"""
import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    if len(sys.argv) == 3:
        url = sys.argv[1]
        email = sys.argv[2]

        data = urllib.parse.urlencode({'email': email}).encode('utf-8')

        try:
            with urllib.request.urlopen(url, data=data) as response:
                body = response.read().decode('utf-8')
                print("Your email is:", body)
        except Exception as e:
            print("Error:", e)
    else:
        print("Usage: ./2-post_email.py <URL> <email>")
