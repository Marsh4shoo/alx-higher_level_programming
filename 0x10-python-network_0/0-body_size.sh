#!/bin/bash

# Check if URL is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url=$1

# Sending a GET request to the provided URL using curl and retrieving the body size in bytes
body_size=$(curl -sI "$url" | awk '/Content-Length/ {print $2}' | tr -d '\r')

if [ -z "$body_size" ]; then
    echo "Unable to retrieve content size for $url"
    exit 1
fi

echo "$body_size"

