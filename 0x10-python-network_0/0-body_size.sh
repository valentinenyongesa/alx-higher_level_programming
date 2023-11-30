#!/bin/bash
#takes in a URL, sends a request to that URL, and displays the body size
curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}' | tr -d '\r'
