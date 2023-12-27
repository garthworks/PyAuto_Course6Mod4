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
        #set subject line, send email
        subject = "Error -localhost cannot be resolved to 127.0.0.1"


# check cpu util is less than 80%
def cpu_util():
    cpu_reading = psutil.cpu_percent(interval=1)
    if cpu_reading > 80
        #set subject line, send email
        subject = "Error - CPU usage is over 80%"
        send_email(sender, recipient, subject, body)

# check disk free space is greater than 20%
def disk_space_check
    path = "/"
    data = shutil.disk_usage(path)
    disk_cap = data[0]
    disk_used = data[1]
    used_per = (disk_used / disk_cap) * 100
    if used_per > 80:
        # set subject line, send email
        subject =  "Error - Available disk space is less than 20%"
        send_email(sender, recipient, subject, body)


psutil.disk_usage('/')

# check memory is greater than 500MB
subject = "Error - Available memory is less than 100MB"

if __name__ == "__main__":
    sender = "automation@example.com"
    recipient = "student@example.com"
    body =  "Please check your system and resolve the issue as soon as possible."
    # may not need to generate message or need to generate a message without an attachment
    # message = generate_email(sender, recipient, subject, body)
    # send_email(message)