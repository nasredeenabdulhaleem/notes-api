FROM ubuntu:22

ENV TZ=Africa/Lagos \
    DEBIAN_FRONTEND=npminteractive

RUN apt update && apt-install -y  sudo software-properties-common ca-certificates lsb-release 

