#! python2.7
# -*- coding: utf-8 -*-
# searchFile.py - search files whose name contain the required string in current dir and sub-dir.

import os, sys

def searchFile():
    if len(sys.argv) != 2:
        print 'Usage: python searchFile.py searchKey'
        sys.exit()
        
    searchKey = sys.argv[1]

    for root, dirs, files in os.walk('.'):
        for file in files:
            if searchKey in file:
                print os.path.join(root, file)
                
searchFile()
