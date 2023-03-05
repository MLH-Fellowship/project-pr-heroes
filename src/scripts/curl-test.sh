#!/bin/env bash

user="Random User"
email="random@email.com"
content="Last Random timeline post"

# Make the POST request and get the HTTP status code and response body
response=$(curl --connect-timeout 3 -s -X POST "$(hostname)".local:5000/api/timeline_post -d "name=$user&email=$email&content=$content" -w "\n%{http_code}" )

# Extract the HTTP status code from the response
poststatuscode=$(echo "$response" | tail -n1)

if [ "$poststatuscode" -eq 200 ]; then
    # Extract the ID of the new record from the response
    id=$(echo "$response" | head -n-1 | jq '.id')

    # Use the ID to filter the timeline_posts
    new_timeline=$(curl --connect-timeout 3 -s "$(hostname)".local:5000/api/timeline_post | jq --argjson id "$id" '.timeline_posts[] | select(.id == $id)')

    if [ -n "$new_timeline" ]; then
        echo "Successfully added"
        echo "$new_timeline"
    else
        echo "POST method did not add any timeline_post"
    fi
else
    echo "POST request failed with status code $poststatuscode"
fi