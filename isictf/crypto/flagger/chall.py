#!/usr/bin/env python3

import os
import random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

KEY = ''.join(random.choice('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
              for _ in range(32)).encode()


def encrypt(name):
    cipher = AES.new(KEY, AES.MODE_ECB)
    return cipher.encrypt(pad(name.encode(), AES.block_size)).hex()


def decrypt(ciphertext):
    cipher = AES.new(KEY, AES.MODE_ECB)
    result = unpad(cipher.decrypt(bytes.fromhex(ciphertext)), AES.block_size)
    return result.decode()


print('welcome to flagger!')
while 1:
    print('1. view flag')
    print('2. generate token')

    value = input('> ')
    if value == '1':
        token = input('token: ')
        try:
            name = decrypt(token)
        except ValueError:
            print('invalid token')
            continue
        if name == 'adel':
            print(os.environ.get('FLAG', 'ISICTF{fake_flag}'))
        else:
            print('sorry, only adel can view the flag')
    elif value == '2':
        name = input('name: ')
        if name == 'adel':
            print('nice try!')
        else:
            print(f'here\'s your token: {encrypt(name)}')
    else:
        print('unknown input!')
