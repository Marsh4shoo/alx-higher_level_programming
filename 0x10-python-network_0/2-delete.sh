#!/bin/bash

# Check if a URL is provided as an argument
if [ -z "$1" ]; then
    echo "Please provide a URL"
    exit 1
fi

# Fetch and display the body of the response
curl -s -L -X GET "$1"
