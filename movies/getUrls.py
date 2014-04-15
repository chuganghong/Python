# Filename: getUrl.py

import urllib2
import re
import sys

sysCharType = sys.getfilesystemencoding()








def getHtml(url):
    html = urllib2.urlopen(url).read()
    return html

def getUrl(html):
    #find_re = re.compile(r'<h1>(.+?)<\/h1>',re.DOTALL)

    find_re = re.compile(r'<table[^>]class="tagCol">(.*?)<\/table>',re.DOTALL)
    
    urls = find_re.findall(html)
    return urls

def getHref(str):
    #<a href="./爱情">爱情</a>
    pattern = re.compile(r'<a[^>]*?href="([\s\S]*?)">([\s\S]*?)<\/a>',re.DOTALL)
    #print pattern
    hrefs = pattern.findall(str)
    #print 'hrefs',  hrefs
    return hrefs

def saveData(data):
    url = 'http://movie.douban.com/tag/' + data
    f = file('data.txt','a+')
    print 'save',   url,   '\n'
    #data2 = data, '\n'
    f.write(url)
    f.write('\n')
    f.close()

url = 'http://movie.douban.com/tag/?view=type'
html = getHtml(url)



urls = getUrl(html)

#print urls
#print urls

i = 1
sysHtml = html.decode('utf8').encode(sysCharType)
for url in urls:
    
    print "第",  i,  "个：\n"
    #print url
    hrefs = getHref(url)
    #print hrefs
    for href in hrefs:
        saveData(href[1])
    i = i + 1
else:
    print 'The for loop is over'
    
