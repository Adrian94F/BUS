#!/usr/bin/python2
# -*- coding: utf-8 -*-
# author: Adrian Frydmański

import socket
import sys
import json
import thread
from threading import Thread
import time
from message import *
from random import randint
import base64
from time import sleep
import re


# received data
def rec(data):
    print('[r] {}'.format(data))


# received message
def msg_out(data, name):
    print('[{}] {}'.format(name, data))


# error message
def error():
    print('[!] error occurred... goodbye\n    press any key')
    sys.exit()


# output thread for printing incoming data
class OutputThr(Thread):
    def run(self):
        while alive == 1:
            data = sock.recv(buffer_size)
            if data != '':
                try:
                    data = json.loads(data)
                    msg = data['msg']
                    sender = data['from']
                except ValueError:
                    error()
                    return
                msg = base64.b64decode(msg)
                msg = decrypt(msg, encryption, K)
                msg_out(msg, sender)
            else:
                thread.interrupt_main()
                error()
                return


if len(sys.argv) != 3 and len(sys.argv) != 4 and len(sys.argv) != 5:
    print('usage: client.py server_address port_number [none|xor|rot13] [bot]')
    sys.exit()

addr = sys.argv[1]
port = int(sys.argv[2])

encryption = NONE
bot = 0

for i in range(4, len(sys.argv) + 1):
    if sys.argv[i - 1] == XOR or sys.argv[i - 1] == CAESAR:
        encryption = sys.argv[i - 1]
    elif sys.argv[i - 1] == 'bot':
        bot = 1

buffer_size = 1024
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
name = raw_input('[ ] starting client\n    press CTRL + C to exit\n    type your name: ')
name = re.sub('[^A-Za-z0-9]+', '', name)
server_address = (addr, port)
print('[+] trying to connect to {} with encryption set to \'{}\''.format(server_address, encryption))
try:
    sock.connect(server_address)
except socket.error:
    print('[!] server unavailable, goodbye my friend')
    sys.exit(0)

alive = 1

# run until CTRL+C
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
    a = randint(0, 100)
    A = g ** a % p
    data = Msg.a % A
    sock.send(data)

    data = sock.recv(buffer_size)
    try:
        received = json.loads(data)
        B = received['b']
    except KeyError:
        error()

    # key
    K = B ** a % p

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
        msg = ''
        data = ''
        # send predefined messages in bot mode
        if bot:
            msg = 'message nr {}'.format(counter)
            counter += 1
            time.sleep(2)
        # send user input in normal mode
        else:
            msg = raw_input('')
            if msg == '':
                continue
        # if user changed encryption mode or in bot mode
        if msg == ENC_CHG_PREFIX + NONE or (bot and counter % 5 == 0 and counter % 3 == 0):
            data = Msg.encr_req % NONE
            encryption = NONE
            print('[ ] setting encryption to none')
        elif msg == ENC_CHG_PREFIX + CAESAR or (bot and counter % 5 == 0 and counter % 3 == 1):
            data = Msg.encr_req % CAESAR
            encryption = CAESAR
            print('[ ] setting encryption to caesar')
        elif msg == ENC_CHG_PREFIX + XOR or (bot and counter % 5 == 0 and counter % 3 == 2):
            data = Msg.encr_req % XOR
            encryption = XOR
            print('[ ] setting encryption to xor')
        # else - send normal message
        else:
            msg = encrypt(msg, encryption, K)
            msg = base64.b64encode(msg)
            data = Msg.msg % (msg, name)
        sock.send(data)
    alive = 0

except KeyboardInterrupt:
    mythread._Thread__stop()
    sock.close()
    print('\b\b[ ] time to say goodbye!')
