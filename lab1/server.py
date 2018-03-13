#!/usr/bin/python2
# -*- coding: utf-8 -*-
# author: Adrian Frydmański

import socket
import sys
import json
from threading import Thread
from message import *
from Crypto.Util import number
from random import randint
import base64


PRIME_BIT_SIZE = 256


# logger thread
class Logger(Thread):
    
    def __init__(self):
        Thread.__init__(self)
        self.queue = []

    def info(self, data):
        self.queue.append(data)

    def run(self):
        while True:
            if self.queue:
                data = self.queue.pop(0)
                print(data)


# client thread for sending messages
class ClientSendHandler(Thread):

    def __init__(self, ip, port, conn):
        Thread.__init__(self) 
        self.ip = ip 
        self.port = port 
        self.conn = conn
        self.queue = []
        self.encryption = NONE

    def send(self,data):
        logger.info('[s] to   {}:{} \'{}\''.format(self.ip, str(self.port), data))
        self.conn.send(data)

    def run(self): 
        # send Msgs 'received' from other threads
        while True:
            if self.queue:
                data = self.queue.pop(0)
                self.send(data)


# client thread
class ClientHandler(Thread):

    def __init__(self, ip, port, conn):
        Thread.__init__(self) 
        self.ip = ip 
        self.port = port 
        self.conn = conn
        self.encryption = NONE
        self.sending_thread = ClientSendHandler(ip, port, conn)
        self.sending_thread.start()
        self.K = 0
        logger.info("[+] new server socket thread started for {}:{}".format(ip, str(port)))

    # message text outpur
    def rec(self, data):
        logger.info('[r] from {}:{} \'{}\''.format(self.ip, str(self.port), data))

    # raw message output and send
    def send(self, data):
        logger.info('[s] to   {}:{} \'{}\''.format(self.ip, str(self.port), data))
        self.conn.send(data)

    # info about encryption change
    def chng_enc(self):
        logger.info('[i] {}:{} set encryption to {}'. format(self.ip, str(self.port), self.encryption))

    # info about error
    def error(self):
        logger.info('[!] error occurred while parsing data from {}:{}'.format(self.ip, str(self.port)))

    def run(self):
        # wait for key request
        data = self.conn.recv(buffer_size)
        try:
            data = json.loads(data)
            if data['request'] == 'keys':
                pass
            else:
                self.conn.close()
                return
        except ValueError:
            self.error()
            self.sending_thread._Thread__stop()
            return
        self.rec(data)

        p = number.getPrime(PRIME_BIT_SIZE)
        g = p
        while g == p:
            g = number.getPrime(PRIME_BIT_SIZE)
        data = Msg.keys_resp % (p, g)
        self.send(data)

        b = randint(0, 100)
        B = g ** b % p
        data = Msg.b % B
        self.send(data)

        data = self.conn.recv(buffer_size)
        self.rec(data)
        try:
            received = json.loads(data)
            A = received['a']
        except ValueError:
            self.error()
            self.sending_thread._Thread__stop()
            return

        self.K = A ** b % p  # symmetric key for encrypt/decrypt messages to/from client

        while True:  # data receive in loop
            data = self.conn.recv(buffer_size)
            if data:
                try:
                    received = json.loads(data)
                    msg = ''
                    name = ''
                    if 'msg' in received and 'from' in received:  # normal message
                        msg = received['msg']
                        name = received['from']
                        msg = base64.b64decode(msg)
                        msg = decrypt(msg, self.encryption, self.K)  # decrypt
                        self.rec(msg)
                        # 'send' message to other threads except self
                        for thr in threads:
                            if thr.isAlive() and thr != self:
                                thr_msg = msg
                                # encrypt data for other clients
                                thr_msg = encrypt(thr_msg, thr.encryption, thr.K)
                                thr_msg = base64.b64encode(thr_msg)
                                data = Msg.msg % (thr_msg, name)
                                thr.sending_thread.queue.append(data)
                    if 'encryption' in received:  # set encryption message
                        self.encryption = received['encryption']
                        self.rec('{}'.format(received))
                        self.chng_enc()
                        continue
                except KeyError:
                    self.error()
                    self.sending_thread._Thread__stop()
                    return

            else:
                logger.info('[-] disconnecting {}:{}'.format(self.ip, str(self.port)))
                self.sending_thread._Thread__stop()
                break

# logger thread
logger = Logger()
logger.start()

if len(sys.argv) != 2:
    logger.info('usage: server.py port_number')
    logger._Thread__stop()
    sys.exit()

port = int(sys.argv[1])

buffer_size = 1024

# bind to socket
server_address = ('', port)
logger.info('[ ] starting up on {}\n    press CTRL + C to exit'.format(server_address))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
sock.bind(server_address)

threads = []  # empty client threads array

# run until CTRL+C
try:
    # infinite loop for listening
    while True:
        sock.listen(4)

        (conn, (ip, port)) = sock.accept()
        newthread = ClientHandler(ip, port, conn)
        newthread.start()
        threads.append(newthread) 

        for t in threads: 
            if not t.isAlive():
                t.join() 

except KeyboardInterrupt:
    # kill all alive threads
    for t in threads: 
        if t.isAlive():
            t.sending_thread._Thread__stop()
            t._Thread__stop()
    logger._Thread__stop()
    print('\b\b[ ] time to say goodbye!')
