#!/bin/bash

# Starting Model container
docker container run --rm -d -p 8000:8000 --network toy_network --name TOY_MODEL datascientest/fastapi:1.0.0

# docker container run -it --rm --name TOY_AUTHENTICATION --volume ./SHARED_STORAGE:/home/SHARED_STORAGE authentication_image:latest bash
# docker container run --rm -d               --network toy_network --name TOY_AUTHENTICATION --volume ./SHARED_STORAGE:/home/SHARED_STORAGE authentication_image:latest
docker container run --rm -d -e LOG="1"    --network toy_network --name TOY_AUTHENTICATION --volume ./SHARED_STORAGE:/home/SHARED_STORAGE authentication_image:latest

# docker container run -it --rm --network toy_network --name TOY_AUTHORIZATION --volume ./SHARED_STORAGE:/home/SHARED_STORAGE authorization_image:latest bash
# docker container run --rm -d               --network toy_network --name TOY_AUTHORIZATION  --volume ./SHARED_STORAGE:/home/SHARED_STORAGE authorization_image:latest
docker container run --rm -d -e LOG="1"    --network toy_network --name TOY_AUTHORIZATION  --volume ./SHARED_STORAGE:/home/SHARED_STORAGE authorization_image:latest

# docker container run -it --rm --network toy_network --name TOY_CONTENT --volume ./SHARED_STORAGE:/home/SHARED_STORAGE content_image:latest bash
# docker container run --rm -d               --network toy_network --name TOY_CONTENT        --volume ./SHARED_STORAGE:/home/SHARED_STORAGE content_image:latest
docker container run --rm -d -e LOG="1"    --network toy_network --name TOY_CONTENT        --volume ./SHARED_STORAGE:/home/SHARED_STORAGE content_image:latest

# Some sample test
# Status:
curl -X  GET -i http://localhost:8000/status

# Authentication Tests
curl -X  GET -i http://localhost:8000/permissions?username=bob\&password=builder -H 'accept: application/json'
curl -X  GET -i http://localhost:8000/permissions?username=alice\&wonderland=builder -H 'accept: application/json'
curl -X  GET -i http://localhost:8000/permissions?username=clementine\&password=mandarine -H 'accept: application/json'

# Authorization Tests
curl -X GET http://localhost:8000/v1/sentiment?username=alice\&password=wonderland\&sentence=The%20sky%20is%20blue%2C%20and%20so%20are%20you. -H 'accept: application/json'
curl -X GET http://localhost:8000/v2/sentiment?username=alice\&password=wonderland\&sentence=The%20sky%20is%20blue%2C%20and%20so%20are%20you. -H 'accept: application/json'

# Content Test
curl -X GET http://localhost:8000/v1/sentiment?username=alice\&password=wonderland\&sentence=life%20is%20beautiful -H 'accept: application/json'
curl -X GET http://localhost:8000/v2/sentiment?username=alice\&password=wonderland\&sentence=life%20is%20beautiful -H 'accept: application/json'

curl -X GET http://localhost:8000/v1/sentiment?username=alice\&password=wonderland\&sentence=That%20sucks -H 'accept: application/json'
curl -X GET http://localhost:8000/v2/sentiment?username=alice\&password=wonderland\&sentence=That%20sucks -H 'accept: application/json'

# Stopping Model container
docker container stop TOY_MODEL

# cat SHARED_STORAGE/api_test.log  # Only with root privileges
