#!/usr/bin/python2
# -*- coding: utf-8 -*-

import socket
import sys
import json
from threading import Thread


class ClientHandler(Thread):

    def __init__(self,ip,port,conn): 
        Thread.__init__(self) 
        self.ip = ip 
        self.port = port 
        self.conn = conn
        self.queue = []
        print "[+] new server socket thread started for {}:{}".format(ip, str(port))
 
    def run(self): 
        # handshake and keys...

        while True : 
            # receive data
            data = self.conn.recv(2048)
            if data:
                # print received data
                print('[r] from {}:{} \'{}\''.format(self.ip, str(self.port), data))
                # 'send' to other threads except self
                for t in threads:
                    if t.isAlive() and t != self:
                        t.queue.append(data)
                # send messages 'received' from other threads
                while self.queue:
                    data = self.queue.pop(0)
                    print('[s] to   {}:{} \'{}\''.format(self.ip, str(self.port), data))
                    self.conn.send(data)
            else:
                print('[-] disconnecting {}:{}'.format(self.ip, str(self.port)))
                break


if len(sys.argv) != 2:
    print('usage: server.py port_number')
    sys.exit() 

port = int(sys.argv[1])

buffer_size = 1024

server_address = ('localhost', port)
print('[ ] starting up on {}\n    press CTRL + C to exit'.format(server_address))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
sock.bind(server_address)

threads = []

# Hardcoded
g = 123
p = 456

try:
    while True:
        sock.listen(1)

        (conn, (ip,port)) = sock.accept() 
        newthread = ClientHandler(ip,port,conn) 
        newthread.start() 
        threads.append(newthread) 

        for t in threads: 
            if not t.isAlive():
                t.join() 

except KeyboardInterrupt:
    for t in threads: 
        if t.isAlive():
            t._Thread__stop()
    print('\b\b[ ] time to say good bye!')

