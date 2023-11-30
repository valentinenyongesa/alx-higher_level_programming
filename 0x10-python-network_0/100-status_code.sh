#!/bin/bash
#Sends a URL and displays status code of response
curl -so /dev/null -w "%{http_code}" "$1"
