#!/bin/bash

# Check if a URL is provided as an argument
if [ -z "$1" ]; then
    echo "Please provide a URL"
    exit 1
fi

# Send a request to the URL and display only the status code of the response
status_code=$(curl -s -o /dev/null -w "%{http_code}" "$1")

# Display the HTTP status code
echo "$status_code"

