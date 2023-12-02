#!/usr/bin/python3
"""Displays value of the response"""
import urllib.request
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        url = sys.argv[1]

        try:
            with urllib.request.urlopen(url) as response:
                x_request_id = response.getheader('X-Request-Id')
                print(x_request_id)
        except Exception as e:
            print("Error:", e)
    else:
        print("Usage: ./1-hbtn_header.py <URL>")
