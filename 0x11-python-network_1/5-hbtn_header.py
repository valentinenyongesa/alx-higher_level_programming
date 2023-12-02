#!/usr/bin/python3
"""Reaponse header value"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        url = sys.argv[1]

        try:
            response = requests.get(url)
            x_request_id = response.headers.get('X-Request-Id')
            print(x_request_id)
        except Exception as e:
            print("Error:", e)
    else:
        print("Usage: ./5-hbtn_header.py <URL>")
