#!/usr/bin/env python3

import time
import socket
import atexit
import sendgrid
import os
from sendgrid.helpers.mail import *

BANNER = b'220 ProFTPD 1.2.8 Server\nName: '
LHOST = '0.0.0.0'
LPORT = 21
TIMEOUT = 10

SENDGRID_API_KEY=os.environ.get('SENDGRID_API_KEY')
FROM_EMAIL=os.environ.get('HONEY_FROM_MAIL')
TO_EMAIL=os.environ.get('HONEY_TO_MAIL')

sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)
listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def sendLog(fromip, message):
    text = fromip + " " + message
    from_email = Email(FROM_EMAIL)
    to_email = To(TO_EMAIL)
    subject = "Honeypot Alert"
    content = Content("text/plain", text)
    mail = Mail(from_email, to_email, subject, content)
    response = sg.client.mail.send.post(request_body=mail.get())

def exit_handler():
    print('\n[*] Honeypot is shutting down!')
    listener.close()

def main():
    print ('[*] Honeypot starting on ' + LHOST + ':' + str(LPORT))
    atexit.register(exit_handler)
    listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listener.bind((LHOST, LPORT))
    listener.listen(5)
    while True:
        (insock, address) = listener.accept()
        insock.settimeout(TIMEOUT)
        print ('[*] Honeypot connection from ' + address[0] + ':' + str(address[1]) + ' on port ' + str(LPORT))
        sendLog(address[0], "Honeypot is accessed by an attacker!");
        try:
            insock.send(BANNER)
            data = insock.recv(1024)
        except socket.error as e:
            sendLog(address[0],'Error: ' + str(e))
            time.sleep(5)
        else:
            print("Attacker is sending data.")
        finally:
            insock.close()
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
