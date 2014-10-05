#!/usr/bin/env python -tt
# -*- coding: utf-8 -*-
""" task_04 Cracking Passwords
Specifications

Create a file named task_04.py

Import the data.py file.
Instantiate a variable named SALT and assign it a value of 'monosodium-glutamate'.
Create a function named test_passwords() that accepts a list object parameter.
Separate the user account data list items by the : into a temporary list of field values
Call the crack_it() function on the second field item and assign the return value to a variable
Use the stored return value to determine if the password was cracked
Append any cracked passwords to a new list using a tuple object that includes the matched password and the user's name.
Return the new list to the calling statement.
Create a function named crack_it() that accepts a string object.
The input of this function will be the string of hashed password characters collected by the calling test_passwords() function
Loop through the data.WORDS list
Call the data.crypt() function with each word and the SALT variable. Compare the result of the string returned by data.crypt() with that passed as the input parameter. Return the word if if a match is found.
Create a function named report() that accepts a list of tuples
Display a report of each user your with a weak password as shown in the example output.
Call the test_passwords() function with data.PASSWD as the input parameter. Assign the returned list of tuples to a variable or nest the test_passwords() within you report() function to display your results.
Output Example

Note

This is only example output and not the real passwords in the assignment.

$ python task_04.py

    Cracked passwords
    -------------------------------
    Jill Lawrence   password
    Timmothy Hanks  monkey
    Ronda Rihanna   shadow
    Donny Johnson   princess
data.crypt() Function Usage Example

Note how the second "salt" parameter changes the output. This is called a salted hash.

>>> import data
>>> data.crypt('myweakpassword', 'RockSalt')
'V4pbI2d55lfZvSnstgv8L+uaFyg='
>>> data.crypt('myweakpassword', 'monosodium-glutamate')
'XcuEJjmciLaD9enxYJ4IGatgnD4='
>>>
"""
import data

SALT = 'monosodium-glutamate'

def test_passwords(account):
    user_id = []
    pass_hash = []
    hashword = None
    rep_tuple = []

    for user_id in account:
        pass_hash = user_id.split(':')
        hash_word = crack_it(pass_hash[1])
        rep_tuple += (pass_hash[4], hash_word)

    report(rep_tuple)

def crack_it(hash_w):
    for crack in data.WORDS:
        if hash_w == data.crypt(crack, SALT):
            return crack

def report(this_tuple):
    """http://stackoverflow.com/questions/2990121/how-do-i-loop-through-a-python-list-by-twos"""
    print 'Cracked Passwords' + '\n' + ('-' * 40)
    for index in range(0, len(this_tuple)-1, 2):
        print this_tuple[index] + "   " + this_tuple[index + 1]

test_passwords(data.PASSWD)
