#!/usr/bin/python2
# -*- coding: utf-8 -*-
# author: Adrian Frydmański

import socket
import sys
import json
from threading import Thread
import time
from message import Msg
from random import randint

def rec(data):
	print('[r] {}'.format(data))

def error():
	print('[!] error occurred... goodbye')
	sys.exit()


class OutputThr(Thread):
	def run(self):
		while alive == 1:
			data = sock.recv(buffer_size)
			rec(data)


if len(sys.argv) != 3 and len(sys.argv) != 4:
	print('usage: client.py server_address port_number')
	sys.exit()

addr = sys.argv[1]
port = int(sys.argv[2])
encryption = sys.argv[3] if len(sys.argv) == 4 else 'none'

buffer_size = 1024
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
name = raw_input('[ ] starting client\n    press CTRL + C to exit\n    type your name: ')
server_address = (addr, 2580)
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
	B = g^b % p
	data = Msg.b % (B)
	sock.send(data)

	data = sock.recv(buffer_size)
	try:
		received = json.loads(data)
		A = received['a']
	except KeyError:
		error()

	#key
	K=A^b % p

	# Send info about encryption
	data = Msg.encr_req % (encryption)

	# Start output thread
	try:
		mythread = OutputThr(name = "OutputThread") 
		mythread.start() 
	except:
		print('[!] error: unable to start thread')

	# Start input reading
	counter = 1
	while True:
		data = 'I am {} ({})'.format(name, counter) # raw_input('')
		# JSON magic...
		sock.send(data)
		counter += 1
		time.sleep(2)
	alive = 0

except KeyboardInterrupt:
	mythread._Thread__stop()
	sock.close()
	print('\b\b[ ] time to say goodbye!')
