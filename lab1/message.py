# -*- coding: utf-8 -*-
# author: Adrian Frydmański

import codecs


class Msg:
    req_keys = '{ "request": "keys" }'
    keys_resp = '{ "p": %d, "g": %d }'
    a = '{ "a": %d }'
    b = '{ "b": %d }'
    encr_req = '{ "encryption": "%s" }'
    msg = '{ "msg": "%s", "from": "%s" }'

    @staticmethod
    def xor(string, key):
        new = ''
        for x in range(0, len(string)):
            new += chr(key ^ ord(string[x]))
        return string


def encrypt(msg, method, key):
    if method == 'rot13':
        msg = codecs.encode(msg, 'rot_13')
    elif method == 'xor':
        msg = Msg.xor(msg, key)
    return msg


def decrypt(msg, method, key):
    if method == 'rot13':
        msg = codecs.decode(msg, 'rot_13')
    elif method == 'xor':
        msg = Msg.xor(msg, key)
    return msg
