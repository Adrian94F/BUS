#!/usr/bin/python2
# -*- coding: utf-8 -*-

import socket
import sys
import json
import threading
import time

if len(sys.argv) != 3 and len(sys.argv) != 4:
    print('usage: client.py server_address port_number')
    sys.exit()

addr = sys.argv[1]
port = int(sys.argv[2])
encryption = sys.argv[3] if len(sys.argv) == 4 else 'none'

buffer_size = 1024

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

name = raw_input('type your name: ')

# Connect the socket to the port where the server is listening
server_address = (addr, 2580)
print('connecting to {} with encryption set to \'{}\''.format(server_address, encryption))
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
    counter = 1
    while True:
        message = 'client{} - {}'.format(name, counter) # raw_input()
        # JSON magic...
        sock.send(message)
        counter += 1
        time.sleep(2)

except KeyboardInterrupt:
    mythread._Thread__stop()
    sock.close()
    print(' time to say good bye!')
