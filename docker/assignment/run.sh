#!/bin/bash

docker run \
    --rm -d \
    --name notifications-service \
    --network lab1network \
    -p 3000:3000 \
    dclandau/cec-notifications-service "$@"
