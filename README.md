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
- source: https://runnable.com/docker/python/dockerize-your-python-application
- cd src
- sudo docker build -t iot-honeypot .
- sudo docker run -p 21:21 -e "SENDGRID_API_KEY=your-top-secret-sendgrid-api-key" -e "HONEY_FROM_MAIL=birkan@birkan.com" -e "HONEY_TO_MAIL=birkan.kolcu@ozu.edu.tr" iot-honeypot

# Testing the setup
- ftp localhost

# Credits
Inspired and partially used source code from https://github.com/joeylane/honeypot.py