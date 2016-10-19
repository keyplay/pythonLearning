#! python3.4
# -*- coding: utf-8 -*-
# safe_base64_decode.py - decode base64 whose = is removed.

import base64

def safe_base64_decode(s):
    # calculate the number of '=' we need
    remainder = len(s)%4
    if remainder == 0:
        return base64.b64decode(s)
        
    for i in range(remainder):
        s += b'='
    return base64.b64decode(s)


# test:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('Pass')
