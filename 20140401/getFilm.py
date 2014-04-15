# Filename: getFilem.py

import urllib
import re

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    page.close()
    return html

url = 'http://localhost/myhome.php'


html = getHtml(url)

def getDictionary(html):    
    reg = r"<a href=\"(*?)\">(*?)</a>"
    dicList = re.compile(reg).findall(html)
    return dicList

dicList = getDictionary(html)
print dicList


