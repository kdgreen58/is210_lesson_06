#!/usr/bin/env python
# -*- coding: utf-8 -*-

import data
SALT = 'monosodium-glutamate'
def test_passwords(users):
    for i in range(len(users)):
        cracked_pws = []
        pws = users[i].split(':')
        cracked = crack_it(pws)
        if cracked == pws[1]:
            cracked_pws.append(pws[0], pws[1])
            users = cracked_pws
        return users

def crack_it(pws):
    words = test_passwords(pws)
    users = []
    for i in range(0, len(data.WORDS)):
        x = data.crypt(data.WORDS[i], SALT)
        if x in words:
            users.append(x)
    return users

def report(users):
    print "Cracked passwords\n-------------\n{0}".format(test_passwords(data.WORDS))
