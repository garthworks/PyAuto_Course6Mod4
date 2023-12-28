#!/usr/bin/env python3

import psutil
import shutil
import socket
import emails
 
# check localhost resolves to 127.0.01
def localhost_ip_check():
    name = "localhost"
    ip = socket.gethostbyname(name) # get the IP
    if ip != "127.0.0.1":
        #set subject line, call email function
        subject = "Error -localhost cannot be resolved to 127.0.0.1"
        email_alert(subject)
    else:
        print("ip address okay")

# check cpu util is less than 80%
def cpu_util():
    cpu_reading = psutil.cpu_percent(interval=1)
    if cpu_reading > 80:
        #set subject line, send email
        subject = "Error - CPU usage is over 80%"
        email_alert(subject)
    else:
        print("processor okay")

# check disk free space is greater than 20%
def disk_space_check():
    path = "/"
    data = shutil.disk_usage(path)
    used_per = int((data.used / data.total) * 100)
    if used_per > 80:
        # set subject line, send email
        subject =  "Error - Available disk space is less than 20%"
        email_alert(subject)
    else:
        print("disk okay")

# check available memory is greater than 100MB
def memory_avail():
    mem_free = psutil.virtual_memory().available
    mem_free = int(mem_free / (1024 ** 2))
    if mem_free < 100:
        subject = "Error - Available memory is less than 100MB"
        email_alert(subject)
    else:
        print("memory okay")

def email_alert(subject):
    sender = "automation@example.com"
    recipient = "student@example.com"
    body =  "Please check your system and resolve the issue as soon as possible."
    email_alert = emails.generate_email(sender, recipient, subject, body)
    emails.send_email(email_alert)


if __name__ == "__main__":
    localhost_ip_check()
    cpu_util()
    disk_space_check()
    memory_avail()