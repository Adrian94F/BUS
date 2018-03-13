#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: Adrian Frydmański

import base64

encoded = 'GCg7Ozs7Oy01e3oNMz4gP3ogP3ovPjs2NXoZM3opMz96KDUgKSAjPCg1LTs5ei4/MSkueiA7KSAjPCg1LTs0I3oqNTA/PiM0OSAjN3o4OzAuPzd0ehQ1ej41OCg7dno8Njs9O3ouNWB6CBUADRsWBSEJMzQ9Nj8CNSgYIy4/GTMqMj8oJw=='
encrypted = base64.b64decode(encoded)
word = 'ROZWAL_{'
for c in range(0, len(encrypted) - len(word) - 1):
    count = 0
    key = ord(encrypted[c]) ^ ord(word[0])
    for w in range(1, len(word)):
        if ord(encrypted[c + w]) ^ key != ord(word[w]):
            break
        else:
            count += 1
    if count == len(word) - 1:
        out = ''
        for e in encrypted:
            out += chr(ord(e) ^ key)
        print('wynik: {}'.format(out))





