#!/usr/bin/python2
# -*- coding: utf-8 -*-
# author: Adrian Frydmański

import socket
import sys
import json
from threading import Thread
from message import Msg
from Crypto.Util import number
from random import randint
import base64


class Logger(Thread):
    
    def __init__(self):
        Thread.__init__(self)
        self.queue = []

    def info(self,data):
        self.queue.append(data)

    def run(self):
        while True:
            if self.queue:
                data = self.queue.pop(0)
                print(data)


class ClientSendHandler(Thread):

    def __init__(self, ip, port, conn):
        Thread.__init__(self) 
        self.ip = ip 
        self.port = port 
        self.conn = conn
        self.queue = []
        self.encryption = 'none'

    def send(self,data):
        logger.info('[s] to   {}:{} \'{}\''.format(self.ip, str(self.port), data))
        self.conn.send(data)

    def run(self): 
        # send Msgs 'received' from other threads
        while True:
            if self.queue:
                data = self.queue.pop(0)
                self.send(data)


class ClientHandler(Thread):

    def __init__(self, ip, port, conn):
        Thread.__init__(self) 
        self.ip = ip 
        self.port = port 
        self.conn = conn
        self.encryption = 'none'
        self.sending_thread = ClientSendHandler(ip,port,conn)
        self.sending_thread.start()
        logger.info("[+] new server socket thread started for {}:{}".format(ip, str(port)))

    def rec(self, data):
        logger.info('[r] from {}:{} \'{}\''.format(self.ip, str(self.port), data))

    def send(self, data):
        logger.info('[s] to   {}:{} \'{}\''.format(self.ip, str(self.port), data))
        self.conn.send(data)

    def error(self):
        logger.info('[!] error occurred while parsing data from {}:{}'.format(self.ip, str(self.port)))

    def run(self): 
        # handshake and keys...
        data = self.conn.recv(buffer_size)
        if data != Msg.req_keys:
            self.conn.close()
            return
        self.rec(data)

        # Hardcoded 
        # TODO: generate
        p = number.getPrime(8)
        g = number.getPrime(8)
        data = Msg.keys_resp % (p, g)
        self.send(data)

        # send to client B, wait for A
        a = randint(0, 100)
        A = g ^ a % p
        data = Msg.a % A
        self.send(data)

        data = self.conn.recv(buffer_size)
        self.rec(data)
        try:
            received = json.loads(data)
            B = received['b']
        except ValueError:
            self.error()
            return

        # key
        K = B ^ a % p

        while True:
            # receive data
            data = self.conn.recv(2048)
            if data:
                try:
                    received = json.loads(data)
                    msg = received['msg']
                    name = received['from']
                except ValueError:
                    self.error()
                    return
                # print received data
                self.rec(data)

                # if encryption-mode message
                # change encryption mode
                # else decrypt

                # 'send' to other threads except self
                data = Msg.msg % (msg, name)
                for t in threads:
                    if t.isAlive() and t != self:
                        # encrypt data for other clients
                        t.sending_thread.queue.append(data)
            else:
                logger.info('[-] disconnecting {}:{}'.format(self.ip, str(self.port)))
                self.sending_thread._Thread__stop()
                break


logger = Logger()
logger.start()

if len(sys.argv) != 2:
    logger.info('usage: server.py port_number')
    sys.exit() 

port = int(sys.argv[1])

buffer_size = 1024

server_address = ('localhost', port)
print('[ ] starting up on {}\n    press CTRL + C to exit'.format(server_address))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
sock.bind(server_address)

threads = []

try:
    while True:
        sock.listen(1)

        (conn, (ip, port)) = sock.accept()
        newthread = ClientHandler(ip, port, conn)
        newthread.start()
        threads.append(newthread) 

        for t in threads: 
            if not t.isAlive():
                t.join() 

except KeyboardInterrupt:
    for t in threads: 
        if t.isAlive():
            t.sending_thread._Thread__stop()
            t._Thread__stop()
    logger._Thread__stop()
    print('\b\b[ ] time to say goodbye!')
