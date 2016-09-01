#! python2.7
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.
'''
Here's what the program does:
    The command line argument for the keyword is checked.
    If the argument is save, then the clipboard contents are saved to the keyword.
    If the argument is list, then all the keywords are copied to the clipboard.
    Otherwise, the text for the keyword is copied to the clipboard.
This means the code will need to do the following:
    Read the command line arguments from sys.argv.
    Read and write to the clipboard.
    Save and load to a shelf file.
'''

import shelve, pyperclip, sys

mcbShelve = shelve.open('mcb')
# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelve[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'save':
        pyperclip.copy(str(list(mcbShelve.keys())))  # whatif do not use str()
    elif sys.argv[1] in mcbShelve.keys():
        pyperclip.copy(mcbShelve[sys.argv[1]])

mcbShelve.close()
