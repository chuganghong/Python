# Filename: getContent.py

import urllib2
import re

def saveData(data,filename):
	f = file(filename,'a+')
	f.write('\n' + data + '\n')
	f.close()


url = 'http://movie.douban.com/subject/3094909/'
html = urllib2.urlopen(url).read()

# success
find_title = re.compile(r'<span[^>]*?property="v:itemreviewed">(.*?)<\/span>',re.DOTALL)
title = find_title.findall(html)
# print title[0]
saveData(title[0],'title.txt')
# success
find_info = re.compile(r'<div[^>]*?id="info">(.*?)<\/div>',re.DOTALL)
info = find_info.findall(html)
# print info
for inf in info:
	data = inf
	filename = 'inf.txt'
	saveData(data,filename)
else:
	print 'info is overs'

# success
find_related_info = re.compile(r'<div[^>]*?class="related-info">(.*?)<\/div>',re.DOTALL)
related_info = find_related_info.findall(html)
# print related_info

for related_in in related_info:
	data = related_in
	filename = 'content.txt'
	saveData(data,filename)
else:
	print '\nover'
	


