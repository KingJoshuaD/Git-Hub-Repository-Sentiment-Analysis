import re
from re import sub
import time
import cookielib import CookieJar
import urllib2
from urllib2 import urlopen

oj  = CookieJar()
opener = urllib2.build(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

keyWord = 'obama'
startingLink = 'https://twitter.com/search/realtime?q='
