#!/usr/bin/python2
# -*- coding: utf-8 -*-
# author: Adrian Frydmański

import socket
import sys
import json
import threading
from threading import Thread
import time
from message import Msg
from random import randint
import base64


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
                name = data['from']
            except ValueError:
                error()
                return
            msg = base64.b64decode(msg)
            msg_out(msg, name)


if len(sys.argv) != 3 and len(sys.argv) != 4:
    print('usage: client.py server_address port_number [none|xor|rot13] [bot]')
    sys.exit()

addr = sys.argv[1]
port = int(sys.argv[2])

encryption = 'none'
bot = 0
if len(sys.argv) == 4:
    if sys.argv[3] == 'xor' or sys.argv[3] == 'rot13':
        encryption = sys.argv[3]
    elif sys.argv[3] == 'bot':
        bot = 1

buffer_size = 1024
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
name = raw_input('[ ] starting client\n    press CTRL + C to exit\n    type your name: ')
server_address = (addr, 2580)
print('[+] trying to connect to {} with encryption set to \'{}\''.format(server_address, encryption))
sock.connect(server_address)

alive = 1

lock = threading.Lock()

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
    B = g ^ b % p
    data = Msg.b % B
    sock.send(data)

    data = sock.recv(buffer_size)
    try:
        received = json.loads(data)
        A = received['a']
    except KeyError:
        error()

    # key
    K = A ^ b % p

    # Send info about encryption
    data = Msg.encr_req % encryption

    # Start output thread
    print('[ ] starting...')
    try:
        mythread = OutputThr(name="OutputThread")
        mythread.start()
    except:
        print('[!] error: unable to start thread')

    # Start input reading
    counter = 1
    while True:
        if bot:
            message = 'message nr {}'.format(counter)  # raw_input('')
        else:
            # with lock:
            message = raw_input('')  # sys.stdin.readline()
        message = base64.b64encode(message)
        data = Msg.msg % (message, name)
        sock.send(data)
        counter += 1
        time.sleep(2)
    alive = 0

except KeyboardInterrupt:
    mythread._Thread__stop()
    sock.close()
    print('\b\b[ ] time to say goodbye!')
