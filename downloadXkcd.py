#! python2.7
# downloadXkcd.py - Downloads every single XKCD comic.

import requests, bs4, os

url = 'http://xkcd.com'              # starting url
try:
    os.makedirs('xkcd')
except OSError:
    if not os.path.isdir('xkcd'):
        raise
        
while not url.endswith('#'):      
    # Download the page.
    print 'Downloading page %s...' % url
    res = requests.get(url)
    try:
        res.raise_for_status()
    except Exception as err:
        print err
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    # Find the URL of the comic image.       
    elem = soup.select('#comic img')
    if elem == []:
        print 'There is no comic image.'
    else:
        comicUrl = 'http:' + elem[0].get('src')
        # Download the image.
        print 'Downloading image %s...' % (comicUrl)
        comicRes = requests.get(comicUrl)
        try:
            comicRes.raise_for_status()
        except Exception as err:
            print err
            prevLink = soup.select('a[rel="prev"]')[0]
            url = 'http://xkcd.com' + prevLink.get('href')
            continue

        # Save the image to ./xkcd.
        imgFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in comicRes.iter_content(100000):
            imgFile.write(chunk)
        imgFile.close()

    # Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')
    
    
print 'Done.'
