#!/usr/bin/env python
import os
from random import randint, choice, uniform


def random_hex():
    """ returns a random hex, with a random length between 2 and 64
    using os.urandom"""
    seedList = []
    seedList_len = randint(1, 128)
    count = 0
    while count < seedList_len:
        seedList.append(os.urandom(randint(1, 32)).encode('hex'))
        count += 1

    return choice(seedList)


def randSpecialChar():
    """return a random special character"""
    return choice('''`~!@#$%^&*()_-+={}[]\|:;"'<>,\.?/''')


def randChar():
    """return a random character"""
    return choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')


def randPwStr():
    """return a random special character string mixed with a-zA-Z, 0-9
    with a random lenght between 2 and 64"""
    seedList = []
    seedList_len = randint(1, 128)
    count = 0
    while count < seedList_len:
        strLen = 0
        randStr = ""
        while strLen < randint(2, 64):
            randStr += str(
                choice([randChar(), randSpecialChar(), randint(0, 9)])
            )
            strLen += 1

        seedList.append(randStr)
        count += 1

    return choice(seedList)


def random_data(num):
    """ will return json random float, hex and int
        {0: {
                'float': 186.66541583209647,
                'hex': '43435c553c722359e386804f6b28d2c2ee3754456c38f5e7e68f',
                'int': 851482763158959204,
                'password': '5AJ]-02X0J'
            }
        }"""
    data = {}
    count = 0
    while count < num:
        data.update(
            {
                count: {
                    "hex": random_hex(),
                    "int": randint(1, 10**18),
                    "float": uniform(0.1, 10**3.01),
                    "password": randPwStr()
                }
            }
        )
        count += 1
    return data
