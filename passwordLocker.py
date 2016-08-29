#! python2.7
# passwordLocker.py - An insecure password locker program.
'''
It is a password manager program that uses one master password to unlock the password manager.
This program isn't secure, but it offers a basic demonstration of how such programs work.
Then users can copy any account password to the clipboard and paste it into the website's Password field.
'''

PASSWORDS = {'email': 'dsfa',
             'blog': 'sdfs',
             'luggage': '213'}
             
import sys, pyperclip

if len(sys.argv) < 2:
    print 'Usage: python pw.py [account] - copy account password'
    sys.exit()
    
account = sys.argv[1]           # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print 'Password for ' + account + ' copied to clipboard.'
else:
    print 'There is no account named' + account
