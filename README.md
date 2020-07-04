# iot-honeypot
This repository contains a simple honeypot written in Python that will be deployed through Docker on Raspberry Pi.

# Prerequisities for running pure Python script.
- sudo apt install python3-pip -y
- sudo pip3 install virtualenv
- virtualenv -p python3 venv
- source venv/bin/activate
- pip3 install sendgrid
- export SENDGRID_API_KEY="your-top-secret-sendgrid-api-key"
- sudo -E python3 ftp-honeypot.py

# Dockerization of the Python application
## Build Docker Image
- source: https://runnable.com/docker/python/dockerize-your-python-application
- cd src
- sudo docker build -t ftp-honeypot .
- sudo docker run -p 21:21 -e "SENDGRID_API_KEY=your-top-secret-sendgrid-api-key" -e "HONEY_FROM_MAIL=birkan@birkan.com" -e "HONEY_TO_MAIL=birkan.kolcu@ozu.edu.tr" ftp-honeypot

## Upload Docker Image to Docker Hub
- docker images
- sudo docker tag your-docker-image-id your-docker-hub-username/ftp-honeypot:latest
- sudo apt install gnupg2 pass -y
- sudo docker login
- sudo docker push your-docker-hub-username/ftp-honeypot:latest

# Running Docker Image on Raspberry Pi with Docker Pirates
- install docker pirates
- configure wifi.yml
- flash the image with wifi config
- ssh yoyoyo@yoyoyo.local
- sudo docker run -p 21:21 -e "SENDGRID_API_KEY=your-top-secret-sendgrid-api-key" -e "HONEY_FROM_MAIL=birkan@birkan.com" -e "HONEY_TO_MAIL=birkan.kolcu@ozu.edu.tr" dockerhub-username/ftp-honeypot

# Testing the setup
- ftp targetip
- check out the email you used in "docker run" command. You should've receveid an email.

# Credits
Inspired and partially used source code from https://github.com/joeylane/honeypot.py