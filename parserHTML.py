#! python2.7
# -*- coding: utf-8 -*-
# parserHTML.py - parse HTML to retrieve the title, time and location of meetings from url 

from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint
import requests

class MyHTMLParser(HTMLParser):

    def __init__(self):
        self.timeflag = False
        self.locationflag = False
        self.titleflag = False
        self.liflag = False
        self.db = []
        self.buffer = ''                # store the data becasue there is some special character in data which will break handle_data()
        HTMLParser.__init__(self)
    
    def handle_starttag(self, tag, attrs):
        if tag == 'ul' and attrs[0][1] == 'list-recent-events menu':    # to identify where the information begins
            self.liflag = True
        elif self.liflag:    
            if tag == 'time':                                           # identify time information
                self.timeflag = True
            elif tag == 'span' and attrs[0][1] == 'event-location':     # identify location information
                self.locationflag = True
            elif tag == 'h3' and attrs[0][1] == 'event-title':          # identify title information
                self.db.append([])                                      # create a list to store information of one meeting
                self.titleflag = True

    def handle_endtag(self, tag):
        if tag == 'ul':
            self.liflag = False
        elif self.liflag:   
            if tag == 'time':
                self.db[-1].append(self.buffer)
                self.buffer = ''
                self.timeflag = False
            elif tag == 'span' and self.locationflag:
                self.db[-1].append(self.buffer)
                self.buffer = ''
                self.locationflag = False
            elif tag == 'h3' and self.titleflag:
                self.db[-1].append(self.buffer)
                self.buffer = ''
                self.titleflag = False

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_data(self, data):
        if self.timeflag:
            self.buffer += data
        elif self.locationflag:
            self.buffer += data
        elif self.titleflag:
            self.buffer += data

    def handle_comment(self, data):
        pass

    # deal with special character
    def handle_entityref(self, name):
        if self.timeflag or self.locationflag or self.titleflag:
            if name == 'quot':
                self.buffer += '\''
            elif name == 'ndash':
                self.buffer += '-'

    def handle_charref(self, name):
        pass

# test
htmldata = requests.get("https://www.python.org/events/python-events/").text
parser = MyHTMLParser()
parser.feed(htmldata)
print(parser.db)
for e in parser.db:
    print('title: ' + e[0])
    print('time: ' + e[1])
    print('location: ' + e[2])           # some location name like russian can not display
    print('-----------------')
