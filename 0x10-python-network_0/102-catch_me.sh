#!/bin/bash

# Check if a URL is provided as an argument
if [ -z "$1" ]; then
    echo "Please provide a URL"
    exit 1
fi

# Send a PUT request to the specified URL with a custom 'Origin' header
curl -sL "$1" -X PUT -H "Origin: You got me!"
