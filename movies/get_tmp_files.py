# Filename: get_tmp_files.py

import getDouban_module
from MyDB import MyDB

host = 'localhost'
root = 'root'
pwd = ''
db = 'movies'
chset = 'utf8'
db = MyDB(host,root,pwd,db,chset)

url = 'http://movie.douban.com/tag/%E7%91%9E%E5%85%B8'
html = getDouban_module.getHtml(url)
num = getDouban_module.getTotalPage(html)
print num 
print '\n'

p12s = getDouban_module.getP12(html)
urls = getDouban_module.getP12a(p12s[0])
print urls[0][0]
print urls[0][1]
