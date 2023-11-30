#!/bin/bash

# Check if a URL is provided as an argument
if [ -z "$1" ]; then
    echo "Please provide a URL"
    exit 1
fi

# Retrieve the Content-Length header from the response headers
content_length=$(curl -s -I "$1" | grep -i "Content-Length" | awk '{print $2}')

# Display the size of the response body in bytes
echo "$content_length"
