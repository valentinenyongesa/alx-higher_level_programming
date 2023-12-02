#!/usr/bin/python3
"""Displays body of the error response"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        url = sys.argv[1]

        try:
            response = requests.get(url)
            response.raise_for_status()

            print(response.text)
        except requests.exceptions.HTTPError as e:
            print(f"Error code: {e.response.status_code}")
    else:
        print("Usage: ./7-error_code.py <URL>")
