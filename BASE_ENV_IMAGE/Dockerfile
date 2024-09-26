FROM ubuntu:18.04
RUN apt-get update && \
    apt-get install python3-pip -y && \
    pip3 install --upgrade pip && \
    pip3 install flask==2.0.0 && \
    pip3 install requests==2.27.1

ENV BASE_ENV_IMAGE "This image was derived from the BASE_ENV_IMAGE docker image"

