#!/usr/bin/env python3

import psutil
import shutil
import socket
from emails import generate_email
from emails import send_email

# check localhost resolves to 127.0.01
def localhost_ip_check():
    host_ip = socket.gethostbyname('localhost') # get the IP
    if host_ip != 127.0.0.1
        #set subject line, call email


# check cpu util is less than 80%
def cpu_util():
    cpu_reading = psutil.cpu_percent(interval=1)
    if cpu_reading > 80
        #set subject line, call email function

# check disk free space is greater than 20%
psutil.disk_partitions()

psutil.disk_usage('/')

# check memory is greater than 500MB


if __name__ == "__main__":
    sender = "automation@example.com"
    recipient = "student@example.com"
    body =  "EDIT HERE"
    message = generate_email(sender, recipient, subject, body, attachment_path)
    send_email(message)