#!/usr/bin/python2
import socket
import sys
import json
import threading

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 2580)
print('connecting to {}'.format(server_address))
sock.connect(server_address)



class OutputThread(threading.Thread):
    def run(self):
        while True:
            data = sock.recv(16)
            print(data)

#start output thread
try:
    mythread = OutputThread(name = "OutputThread") 
    mythread.start() 
except:
   print "error: unable to start thread"

# start input reading
try:
    while True:
        message = raw_input()
        # json magic...
        sock.sendall(message)
except KeyboardInterrupt:
    mythread._Thread__stop()
    print('good bye!')
