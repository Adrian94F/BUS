# -*- coding: utf-8 -*-
# author: Adrian Frydmański


class Msg:
    req_keys = '{ "request": "keys" }'
    keys_resp = '{ "p": %d, "g": %d }'
    a = '{ "a": %d }'
    b = '{ "b": %d }'
    encr_req = '{ "encryption": "%s" }'
    msg = '{ "msg": "%s", "from": "%s" }'


CAESAR = 'cezar'
XOR = 'xor'


def xor(string, key):
    new = ''
    for x in range(0, len(string)):
        new += chr(key ^ ord(string[x]))
    return new


def caesar(string, key):
    string_out = ''
    for each in string:
        c = (ord(each)+key) % 126
        if c < 32:
            if key > 0:
                c += 31
            else:
                c += 95
        string_out += chr(c)
    return string_out


def encrypt(msg, method, key):
    if method == CAESAR:
        msg = caesar(msg, key)
    elif method == XOR:
        msg = xor(msg, key)
    return msg


def decrypt(msg, method, key):
    if method == CAESAR:
        msg = caesar(msg, -key)
    elif method == XOR:
        msg = xor(msg, key)
    return msg
