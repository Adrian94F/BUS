#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: Adrian Frydmański

import base64

encoded = 'PAADREshCgcRDgZPBAoPSxgGBBEOAR0ABksVEUUeDw4YCksoBlQWAg5PBgoRGBUNAxkEGBUGSx8KGkUfDgQHEUVLIgEWAgoDVAoFSw0NBksFBhEGBEsLGBARGBUNSUsKDQ1FBgQVGAwcDk8WHAcETwQXEQ4fBgocCgsOAAUCClQADQ4EABwcBQoTCksKGxUOHkVPOQoRDk8eABgRDA4ASx8dGwYDDk8EBA8PBhoCHksVEQcSSwEdAEsJFhgKSxEOVBEZHgsaCkVLIB9JSw0DFQIKSxsbRTkkNSMkJzQUNQkCCAo9FiIGHwYAGBgKEBg='
encrypted = base64.b64decode(encoded)
word = 'ROZWAL'
passwords = []

for c in range(0, len(encrypted) - len(word)):
    password = []
    count = 0
    for x in range(0, len(word)):
        k = chr(ord(encrypted[c + x]) ^ ord(word[x]))
        if k.isalnum():
            password.append(k)
        else:
            break
    if len(password) == 6:
        passwords.append(password)

print(len(passwords))
print(passwords)

# przejrzałem wygenerowane fragmenty połączonych haseł i wywnioskowałem, że hasło to 'kotek'
# (znalazłem fragment połączonych kluczy 'kkotek') - założyłem, że to proste hasło słownikowe
# następnie dopisałem poniższy kod:
key = 'kotek'
out = ''
for i in range(0, len(encrypted)):
    out += chr(ord(encrypted[i]) ^ ord(key[i % len(key)]))
print(out)



