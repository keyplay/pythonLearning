#! python2.7
# downloadXkcd.py - Downloads every single XKCD comic.

import requests, bs4, os

url = 'http://xkcd.com'              # starting url
os.makedir('xkcd', exist_ok=True)
while not url.endswith('#'):      # may be should be '/1/'
    # Download the page.
    print 'Downloading page %s...' % url
    res = requests.get(url)
    try:
        res.raise_for_status()
    except Exception as err:
        print err
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    # TODO: Find the URL of the comic image.       add a if to judge if elem is empty
    elem = soup.select('#comic img')
    comicUrl = 'http://' + elem[0].get('src')
    comicRes = requests.get(comicUrl)
    try:
        comicRes.raise_for_status()
    except Exception as err:
        print err
    # TODO: Download the image.
    
    # TODO: Save the image to ./xkcd.

    # TODO: Get the Prev button's url.
    
    
print 'Done'
