#!/usr/bin/python2
# -*- coding: utf-8 -*-

import socket
import sys
import json

buffer_size = 1024

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 2580)
print('starting up on {}'.format(server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

# Hardcoded
g = 123
p = 456

try:
    while True:
    # Wait for a connection
        print('waiting for a connection')
        connection, client_address = sock.accept()

        try:
            print('connection from {}'.format(client_address))

            # Receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(buffer_size)
                print('received "{}"'.format(data))
                if data:
                    print('sending data back to the client')
                    connection.sendall(data)
                else:
                    print('no more data from'.format(client_address))
                    break
        finally:
            # Clean up the connection
            connection.close()

except KeyboardInterrupt:
    print(' time to say good bye!')

