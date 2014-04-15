# Filename: test.py

import urllib2
import re

print 2
url = 'http://movie.douban.com/tag/%E7%88%B1%E6%83%85'
html = urllib2.urlopen(url).read()
# find_re = re.compile(r'data-total-page="(\d+)"')
# res = find_re.findall(html)
# print res[0]

# find_re = re.compile(r'(<table[^>]*?>.+?<\/table>)',re.DOTALL)
find_re = re.compile(r'(<table[^>]*?class=""?">.+?<\/table>)',re.DOTALL)

res = find_re.findall(html)
print res
# f = file('a.txt','a+')
# f.write(res[0])
# f.close()
for i in res:
	print i
	f = file('a.txt','a+')
	f.write(i)
	f.write('\n')
	f.write('-------------------------------------------------------------------------\n')
	f.close()

