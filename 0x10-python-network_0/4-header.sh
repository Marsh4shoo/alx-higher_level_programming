#!/bin/bash

# Check if a URL is provided as an argument
if [ -z "$1" ]; then
    echo "Please provide a URL"
    exit 1
fi

# Send a request with a custom header variable
curl -s -H "X-School-User-Id: 98" "$1"
