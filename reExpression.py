# python2.7
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.
'''
Say you have the boring task of finding every phone number 
and email address in a long web page or document. If you manually 
scroll through the page, you might end up searching for a long time. 
But if you had a program that could search the text in 
your clipboard for phone numbers and email addresses, you could simply 
press CTRL-A to select all the text, press CTRL-C to copy it to the clipboard, 
and then run your program. It could replace the text on the clipboard with just 
the phone numbers and email addresses it finds
'''

import pyperclip, re

# Create phone regex
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?               # area code
    (\s|-|\.)?                       # separator
    (\d{3})                          # first 3 dights
    (\s|-|\.)                        # separator
    (\d{4})                          # last 4 dights
    (\s*(ext|x|ext.)\s*(\d{2,5}))?   # extension
    )''', re.VERBOSE)
    
# Create email regex
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+                # username
    @                                # @ symbol
    [a-zA-Z0-9.-]+                   # domain name
    (\.[a-zA-Z]{2,4})                # dot-something
    )''', re.VERBOSE)

# Find matches in clipboard text
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Copy results to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print 'Copied to clipboard'
    print '\n'.join(matches)
else:
    print 'No phone numbers or email addresses found.'