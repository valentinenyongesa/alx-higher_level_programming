#!/bin/bash
#takes in a URL, sends a GET request to the URL, and displays the body
curl -sLw "%{http_code}" "$1" -o /dev/null | { read status; [ "$status" -eq 200 ] && curl -s "$1" || true; }
