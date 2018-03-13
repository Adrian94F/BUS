#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: Adrian Frydmański

import requests, urllib, base64, sys, itertools

# $plain = "query=".$_POST['query']."&f=".$flaga;

url = 'http://training.securitum.com/rozwal/crypto/1.php'
# query=AAAAAAAAAA AAAA&f=ROZWAL_{X AAAAAAAAAAAAAAAA AAAA&f=ROZWAL_{X
# query=AAAAAAAAAA AAA&f=ROZWAL_{XX AAAAAAAAAAAAAAAA AAA&f=ROZWAL_{XX
# query=AAAAAAAAAA AA&f=ROZWAL_{XXX AAAAAAAAAAAAAAAA AA&f=ROZWAL_{XXX
# query=AAAAAAAAAA A&f=ROZWAL_{XXXX AAAAAAAAAAAAAAAA A&f=ROZWAL_{XXXX
# query=AAAAAAAAAA &f=ROZWAL_{XXXXX AAAAAAAAAAAAAAAA &f=ROZWAL_{XXXXX
# ...

found = ''
test = (16 - 2) * 'A' + '&f=ROZWAL_{'
for x in range(0, 16):
    for c in itertools.chain(range(48, 57), range(65, 90), range(97, 122)):
        txt = test + chr(c) + (16 - x + 4) * 'A'
        # print('query: {}'.format(txt))

        r = requests.post(url, data={'query': txt, 'go': 'set'})
        if r.status_code != 200:
            print "REQUEST FAILED"
            sys.exit()
        cookie = base64.b64decode(urllib.unquote(dict(r.cookies)['auth']))

        second_block = cookie[16:32]
        fourth_block = cookie[48:64]

        if second_block == fourth_block:
            print(chr(c))
            found += chr(c)
            test = test[1:] + chr(c)
            # print(cookie)
            break
print(found)