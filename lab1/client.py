#!/usr/bin/python2
# -*- coding: utf-8 -*-

import socket
import sys
import json
import threading

buffer_size = 1024

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

name = raw_input('type your name: ')

# Connect the socket to the port where the server is listening
server_address = ('localhost', 2580)
print('connecting to {}'.format(server_address))
sock.connect(server_address)

class OutputThr(threading.Thread):
    def run(self):
        while True:
            data = sock.recv(buffer_size)
            print(data)

try:
    # Request keys

    # Wait for keys

    # Send to server A and wait for B 

    # Send info about encryption

    # Start output thread
    try:
        mythread = OutputThr(name = "OutputThread") 
        mythread.start() 
    except:
       print('error: unable to start thread')

    # Start input reading
    while True:
        message = raw_input()
        # JSON magic...
        sock.sendall(message)

except KeyboardInterrupt:
    mythread._Thread__stop()
    print(' time to say good bye!')
