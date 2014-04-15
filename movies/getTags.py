# -*- coding: cp936 -*-
#Filename: getTags.py

import urllib2
import re

#get html contetent
def getHtml(url):
    html = urllib2.urlopen(url).read()
    return html

#get tags html
def getTagsHtml(html):
    find_tag = re.compile(r'<table[^>]+class="tagCol">(.*?)<\/table>',re.DOTALL)
    tagsHtml = find_tag.findall(html)
    return tagsHtml

#get url
def getUrl(html):
    find_url = re.compile(r'<a[^>]+href="(.*?)">(.*?)<\/a>',re.DOTALL)
    urls = find_url.findall(html)
    return urls

#save data
def saveData(pre,data,filename='data2.txt'):
    f = file(filename,'a+')
    url = pre + data
    f.write(url)
    f.write('\n')
    f.close()

#get list max page
def getMaxPage(html):    
    find_page = re.compile(r'data-total-page="(\d+)"')
    res = find_page.findall(html)
    return res
def getMaxPage2(html):
    find_page = re.compile(r'data',re.DOTALL)
    res = find_page.search(html)
    return res

url = 'http://movie.douban.com/tag/?view=type'
html = getHtml(url)
tagsHtml = getTagsHtml(html)
#print tagsHtml

#print tagsHtml[2]
urlHtml = tagsHtml[0]
urls = getUrl(urlHtml)
#print urls[0]

for url in urls:
    #print url[1]
    pre = 'http://movie.douban.com/tag/'
    saveData(pre,url[1])


#for tag in tagsHtml:
 #   print tag
#else:
 #   print 'over'

pUrl = 'http://movie.douban.com/tag/爱情'
page = getHtml(pUrl)
#print page
f2 = file('page.txt','a+')
f2.write(page)
f2.close()
p = getMaxPage(page)
print p
for pp in p:
    print pp

    
