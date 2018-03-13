# -*- coding: utf-8 -*-
# author: Adrian Frydmański

import string


# message class with json templates
class Msg:
    req_keys = '{ "request": "keys" }'
    keys_resp = '{ "p": %d, "g": %d }'
    a = '{ "a": %d }'
    b = '{ "b": %d }'
    encr_req = '{ "encryption": "%s" }'
    msg = '{ "msg": "%s", "from": "%s" }'


CAESAR = 'cezar'
XOR = 'xor'
NONE = 'none'
ENC_CHG_PREFIX = '@@@'


# xor function
def xor(text, key):
    new = ''
    for x in range(0, len(text)):
        new += chr((key % 256) ^ ord(text[x]))
    return new


# caesar  function
def caesar(text, key):
    alphabet_u = string.uppercase
    alphabet_l = string.lowercase
    key = key % len(alphabet_l)
    shifted_alphabet_u = alphabet_u[key:] + alphabet_u[:key]
    shifted_alphabet_l = alphabet_l[key:] + alphabet_l[:key]
    table = string.maketrans(alphabet_l + alphabet_u, shifted_alphabet_l + shifted_alphabet_u)
    return text.translate(table)


# encrypting function
def encrypt(msg, method, key):
    if method == CAESAR:
        msg = caesar(msg, key)
    elif method == XOR:
        msg = xor(msg, key)
    return msg


# decryoting function
def decrypt(msg, method, key):
    if method == CAESAR:
        msg = caesar(msg, -key)
    elif method == XOR:
        msg = xor(msg, key)
    return msg
