#!/bin/bash

# Check if the required arguments are provided
if [ $# -lt 2 ]; then
    echo "Usage: $0 <URL> <JSON_FILE>"
    exit 1
fi

url="$1"
json_file="$2"

# Check if the JSON file exists
if [ ! -f "$json_file" ]; then
    echo "JSON file '$json_file' not found"
    exit 1
fi

# Send a JSON POST request to the URL and display the body of the response
curl -s "$url" -d "@$json_file" -X POST -H "Content-Type: application/json"

