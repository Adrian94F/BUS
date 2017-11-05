#!/usr/bin/python2
# -*- coding: utf-8 -*-
# author: Adrian Frydmański

import socket
import sys
import json
import threading
from threading import Thread
import time
from message import *
from random import randint
import base64
from time import sleep
import re


def rec(data):
    print('[r] {}'.format(data))


def msg_out(data, name):
    # with lock:
    print('[{}] {}'.format(name, data))


def error():
    print('[!] error occurred... goodbye')
    sys.exit()


class OutputThr(Thread):
    def run(self):
        while alive == 1:
            data = sock.recv(buffer_size)
            try:
                data = json.loads(data)
                msg = data['msg']
                sender = data['from']
            except ValueError:
                error()
                return
            msg = base64.b64decode(msg)
            msg = decrypt(msg, encryption, K)
            # sender = base64.b64decode(sender)
            msg_out(msg, sender)


if len(sys.argv) != 3 and len(sys.argv) != 4:
    print('usage: client.py server_address port_number [none|xor|rot13] [bot]')
    sys.exit()

addr = sys.argv[1]
port = int(sys.argv[2])

encryption = NONE
bot = 0
if len(sys.argv) == 4:
    if sys.argv[3] == XOR or sys.argv[3] == CAESAR:
        encryption = sys.argv[3]
    elif sys.argv[3] == 'bot':
        bot = 1

buffer_size = 1024
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
name = raw_input('[ ] starting client\n    press CTRL + C to exit\n    type your name: ')
# name = base64.b64encode(name)
name = re.sub('[^A-Za-z0-9]+', '', name)
server_address = (addr, port)
print('[+] trying to connect to {} with encryption set to \'{}\''.format(server_address, encryption))
sock.connect(server_address)

alive = 1

try:
    # Request keys
    data = Msg.req_keys
    sock.send(data)

    # Wait for keys
    data = sock.recv(buffer_size)
    rec(data)

    try:
        received = json.loads(data)
        p = received['p']
        g = received['g']
    except KeyError:
        error()

    # Send to server A and wait for B 
    b = randint(0, 100)
    B = g ** b % p
    data = Msg.b % B
    sock.send(data)

    data = sock.recv(buffer_size)
    try:
        received = json.loads(data)
        A = received['a']
    except KeyError:
        error()

    # key
    K = A ** b % p

    # Send info about encryption
    data = Msg.encr_req % encryption
    sleep(0.1)
    sock.send(data)

    # Start output thread
    try:
        mythread = OutputThr(name="OutputThread")
        mythread.start()
        print('[ ] starting... done!')
    except:
        print('[!] error: unable to start thread')

    # Start input reading
    counter = 1
    while True:
        if bot:
            msg = 'message nr {}'.format(counter)
            counter += 1
            time.sleep(2)
        else:
            # with lock:
            msg = raw_input('')
        msg = encrypt(msg, encryption, K)
        msg = base64.b64encode(msg)
        data = Msg.msg % (msg, name)
        sock.send(data)
    alive = 0

except KeyboardInterrupt:
    mythread._Thread__stop()
    sock.close()
    print('\b\b[ ] time to say goodbye!')
