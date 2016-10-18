#! python3.4
# -*- coding: utf-8 -*-
# loginmd5.py - decode the password of user and detect if the password is wrong when logining.


import hashlib

db = {}

def get_md5(s):
    md5 = hashlib.md5()
    md5.update(s.encode('utf-8'))
    return md5.hexdigest()

def register(username, password):
    db[username] = get_md5(password + username + 'the-Salt')

def login(username, password):
    if db[username] == get_md5(password + username + 'the-Salt'):
        print('Successfully login.')
        return True
    else:
        print('Password wrong!')
        return False
    
# test
register('a', '123')
login('a', '1')
login('a', '123')
