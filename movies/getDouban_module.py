# Filename:getDouban_module.py

import urllib2
import re

def sayHi():
	print 'hi'
	
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

# get html
def getHtml(url):
	html = urllib2.urlopen(url).read()
	return html
	
# save data 
def saveData(data,filename):
	f = file(filename,'a+')
	f.write(data)
	f.close()

# get list start
def getTotalPage(html):
	find_total = re.compile(r'data-total-page="(\d*?)"',re.DOTALL)
	page = find_total.findall(html)
	# print page
	if page == []:
		# print 0
		res = 0
	else:
		# print 1
		res = page[0]
	return res

# get p12
def getP12(html):
	find_p12 = re.compile(r'<div[^>]*?class="pl2">(.+?)<\/div>',re.DOTALL)
	p12 = find_p12.findall(html)
	return p12

# get p12 href
def getP12a(html):
	find_a = re.compile('<a[^>]*?href="(.*?)"[^>]*?class="">(.*?)<\/a>',re.DOTALL)
	urls = find_a.findall(html)
	return urls
# get list end 

# get the content of a film start
def getTitle(html):
	find_title = re.compile(r'<span[^>]*?property="v:itemreviewed">(.*?)<\/span>',re.DOTALL)
	title = find_title.findall(html)
	return title[0]

# get the info of a film 
def getInfo(html):
	find_info = re.compile(r'<div[^>]*?id="info">(.*?)<\/div>',re.DOTALL)
	info = find_info.findall(html)
	return info[0] 
# get the related_info of a film 
def getRelatedInfo(html):
	find_related_info = re.compile(r'<div[^>]*?class="related-info">(.*?)<\/div>',re.DOTALL)
	related_info = find_related_info.findall(html)
	return related_info[0] 
# get the content of a film end



	