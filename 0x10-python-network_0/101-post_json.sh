#!/bin/bash
#Bash script that sends JSON POST request to URL passed as first argument
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
