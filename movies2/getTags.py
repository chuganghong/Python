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
tagsHtml = getTagsHtml(html)
#print tagsHtml

print tagsHtml[2]
urlHtml = tagsHtml[0]
urls = getUrl(urlHtml)
#print urls[0]

for url in urls:
    print url[1]
    saveData(url[1])
else:
    print 'over'


#for tag in tagsHtml:
 #   print tag
#else:
 #   print 'over'
    
    
