#!/bin/bash

# Pulling necessary images
docker image pull ubuntu:18.04
docker image pull datascientest/fastapi:1.0.0

# Preparing shared volume
# docker volume create SHARED_STORAGE
mkdir SHARED_STORAGE
touch SHARED_STORAGE/api_test.log # to keep it from belonging to root

# Creating Network
docker network create --subnet 172.42.0.0/16 --gateway 172.42.0.1 toy_network

# Generating images
cd BASE_ENV_IMAGE
./setup.sh
cd ..

cd AUTHENTICATION_IMAGE
./setup.sh
cd ..

cd AUTHORIZATION_IMAGE
./setup.sh
cd ..

cd CONTENT_IMAGE
./setup.sh
cd ..
