# Filename: test2.py

import urllib2
import re

url = 'http://movie.douban.com/tag/%E7%88%B1%E6%83%85'
html = urllib2.urlopen(url).read()
f2 = file('h.txt','a+')
f2.write(html)
f2.close()

find_r = re.compile(r'<div[^>]*?class="pl2">(.+?)<\/div>',re.DOTALL)
find_a = re.compile('<a[^>]*?href="(.*?)"[^>]*?class="">(.*?)<\/a>',re.DOTALL)
# find_r = re.compile(r'<a[^>]*?href="(.+?)"[^>]*?class="">(.+?)<\/a>',re.DOTALL) failure
urls = find_r.findall(html)
# print urls
a2 = ''
for u in urls:
	f = file('test2_12.txt','a+')
	a = find_a.findall(u)
	f.write(u)
	# print u
	# print a
	f2 = file('a3.txt','a+')
	f2.write('\n' + a[0][0] + '\n')
	f2.write('\n------------------------------------------\n' + a[0][1] + '\n--------------------------------------\n')
	f2.close()
	f.write('\n------------------------------------------------------\n')
	f.close()
	


