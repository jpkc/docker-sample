#!/bin/bash
docker image rm content_image authorization_image authentication_image
# docker image rm content_image authorization_image authentication_image base_env_image ubuntu:18.04 datascientest/fastapi:1.0.0
docker network rm toy_network
rm -fr SHARED_STORAGE
# docker images -a
# docker system prune
# docker rmi AAAA AAA AAA AAA AAA
