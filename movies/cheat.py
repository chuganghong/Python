# Filename:cheat.py

import urllib2
import sys
import gzip

sysCharType = sys.getfilesystemencoding()




url = 'http://movie.douban.com/subject/2002744/'
# url = 'http://www.baidu.com'
req_header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:28.0) Gecko/20100101 Firefox/28.0',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Charset':'utf-8,ISO-8859-1;q=0.7,*;q=0.3',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Cookie':'bid="hsM53yRAjQ8"; __utma=30149280.907110929.1386117661.1398322932.1398335444.20; __utmz=30149280.1398167843.17.13.utmcsr=baidu|utmccn=(organic)|utmcmd=organic|utmctr=urllib2%20403; ll="118281"; __utma=223695111.1156190174.1396328833.1398322932.1398335444.11; __utmz=223695111.1396588375.4.4.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmb=30149280.1.10.1398335444; __utmc=30149280; __utmb=223695111.1.10.1398335444; __utmc=223695111',
'Host':'movie.douban.com'
}

req_timeout = 5
req = urllib2.Request(url,None,req_header)
opener = urllib2.build_opener()
response = opener.open(req)
html = response.read()
gzipped = response.headers.get('Content-Encoding')
if gzipped:
    html = gzip.zlib.decompress(html, 16)

print html



f = file('cheat.txt','a+')
f.write(html)
f.close()