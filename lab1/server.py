#!/usr/bin/python2
# -*- coding: utf-8 -*-

import socket
import sys
import json
from threading import Thread
from SocketServer import ThreadingMixIn 

if len(sys.argv) != 2:
    print('usage: server.py port_number')
    sys.exit() 

port = int(sys.argv[1])

buffer_size = 1024

server_address = ('localhost', port)
print('starting up on {}'.format(server_address))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
sock.bind(server_address)

threads = []

# Hardcoded
g = 123
p = 456

class ClientHandler(Thread):

    def __init__(self,ip,port): 
        Thread.__init__(self) 
        self.ip = ip 
        self.port = port 
        print "[+] New server socket thread started for {}:{}".format(ip, str(port))
 
    def run(self): 
        while True : 
            data = conn.recv(2048) 
            print('[r] from {}:{} \'{}\''.format(ip, str(port), data))
            if data:
                print('[s] to {}:{} \'{}\''.format(ip, str(port), data))
                conn.send(data)
            else:
                print('[-] no more data from {}:{}'.format(ip, str(port)))
                break
    # def run(self):
    #     while True:
    #         data = connection.recv(buffer_size)
    #         print(data)

try:
    while True:
        # Listen for incoming connections
        sock.listen(1)

        (conn, (ip,port)) = sock.accept() 
        newthread = ClientHandler(ip,port) 
        newthread.start() 
        threads.append(newthread) 

        # connection, client_address = sock.accept()

        # try:
        #     print('connection from {}'.format(client_address))

        #     # Receive the data in small chunks and retransmit it
        #     while True:
        #         data = connection.recv(buffer_size)
        #         print('received "{}"'.format(data))
        #         if data:
        #             print('sending data back to the client')
        #             connection.sendall(data)
        #         else:
        #             print('no more data from'.format(client_address))
        #             break
        # finally:
        #     # Clean up the connection
        #     connection.close()

        for t in threads: 
            if not t.isAlive():
                t.join() 

except KeyboardInterrupt:
    print(' time to say good bye!')

