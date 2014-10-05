#!/usr/bin/env python -tt
# -*- coding: utf-8 -*-
""" task_04 """
import data

SALT = 'monosodium-glutamate'

def test_passwords(account):
    user_id = []
    pass_hash = []
    hashword = ''

    for user_id in account:
        pass_hash = user_id.split(':')
        hash_word = crack_it(pass_hash[1])
        print pass_hash[4], pass_hash[1]

def crack_it(hash_w):
    for crack in data.WORDS:
        if hash_w == data.crypt(crack, SALT):
            print crack, hash_w
            print '\n'
            
    
#def report():

test_passwords(data.PASSWD)
