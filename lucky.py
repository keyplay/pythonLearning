#! python2.7
# lucky.py - Opens several Google search results.

import sys, webbrowser, requests, bs4

print 'Googling...'    # display text while downloading the Google page
res = requests.get('https://www.google.com/search?q=' + ' '.join(sys.argv[1:]))
try:
    res.raise_for_status()
except Exception as err:
    print err
    
# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text)
# TODO: Open a browser tab for each result.
elem = soup.select('.r a')   # find all <a> elements that are within an element that has the r CSS class.
numOpen = min(5, len(elem))
for i in range(numOpen):
    webbrowser.open('http://google.com' + elem[i].get('href'))
