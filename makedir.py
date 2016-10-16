#! python2.7
# -*- coding: utf-8 -*-
# makedir.py - output something like dir -l using os module.

import os, time

dirList = os.listdir('.')

print '\n   LastWriteTime     Length Name'
print '   -------------     ------ ----'
for i in dirList:
    lastWriteTime = time.localtime(os.path.getmtime(i))
    lastDate = time.strftime('%d/%m/%Y', lastWriteTime)
    lastTime = time.strftime('%H:%M', lastWriteTime)
    length = os.path.getsize(i)
    if length == 0:
        length = '   '
        
    print lastDate + '   ' + lastTime + '    ' + str(length) + ' ' + i
