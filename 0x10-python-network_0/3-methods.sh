#!/bin/bash

# Check if a URL is provided as an argument
if [ -z "$1" ]; then
    echo "Please provide a URL"
    exit 1
fi

# Retrieve and display the allowed HTTP methods
allowed_methods=$(curl -s -I "$1" | grep -i "Allow" | cut -d " " -f 2-)

# Display the list of allowed HTTP methods
echo "$allowed_methods"
