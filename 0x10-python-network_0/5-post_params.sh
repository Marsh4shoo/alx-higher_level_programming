#!/bin/bash

# Check if a URL is provided as an argument
if [ -z "$1" ]; then
    echo "Please provide a URL"
    exit 1
fi

# Send a POST request with two variables
curl -s -L -X POST "$1" -d "email=test%40gmail%2Ecom&subject=I+will+always+be+here+for+PLD"

