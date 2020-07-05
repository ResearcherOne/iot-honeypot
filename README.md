# iot-honeypot
This repository contains a simple honeypot written in Python that will be deployed through Docker on Raspberry Pi.

# Prerequisities for running pure Python script
- echo "Follow these steps only if you do not want to proceed with Docker"
- sudo apt install python3-pip -y
- sudo pip3 install virtualenv
- virtualenv -p python3 venv
- source venv/bin/activate
- pip3 install sendgrid
- export SENDGRID_API_KEY="your-top-secret-sendgrid-api-key"
- sudo -E python3 ftp-honeypot.py

# Dockerization of the Python application
- cd src
- sudo docker build -t ftp-honeypot .
- sudo docker run -p 21:21 -e "SENDGRID_API_KEY=your-top-secret-sendgrid-api-key" -e "HONEY_FROM_MAIL=birkan@birkan.com" -e "HONEY_TO_MAIL=birkan.kolcu@ozu.edu.tr" ftp-honeypot
- echo "exit from the application once you done with testing your image and proceed with the docker pirates"

# Running Docker Image on Raspberry Pi with Docker Pirates
- install docker pirates
- configure wifi.yml
- flash the image with wifi config
- ssh yoyoyo@yoyoyo.local
- git clone this-repository
- cd src
- sudo docker build -t ftp-honeypot .
- sudo docker run -p 21:21 -e "SENDGRID_API_KEY=your-top-secret-sendgrid-api-key" -e "HONEY_FROM_MAIL=birkan@birkan.com" -e "HONEY_TO_MAIL=birkan.kolcu@ozu.edu.tr" dockerhub-username/ftp-honeypot

# Testing the setup
- echo "find target host. This should also trigger alerts."
- nmap 192.168.1.0/24
- echo "connect to the ftp service"
- ftp targetip
- check out the email you used in "docker run" command. You should've receveid an email.

# Credits
- Inspired and partially used source code from https://github.com/joeylane/honeypot.py
- Dockerization of Python application - https://runnable.com/docker/python/dockerize-your-python-application
- Docker Pirates - https://blog.hypriot.com/