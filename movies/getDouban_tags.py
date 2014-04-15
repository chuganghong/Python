# Filename: getDouban_tags.py

import getDouban_module
from MyDB import MyDB

host = 'localhost'
root = 'root'
pwd = ''
db = 'movies'
chset = 'utf8'
db = MyDB(host,root,pwd,db,chset)

url = 'http://movie.douban.com/tag/?view=type'
pre = 'http://movie.douban.com/tag/'
html = getDouban_module.getHtml(url)
tagsHtml = getDouban_module.getTagsHtml(html)
# print tagsHtml
i = 1
j = 0
for tagHtml in tagsHtml:
	# f = file('tagUrl.txt','a+')
	# f.write('\n------------' + str(i) + '------------------\n')
	tagUrl = getDouban_module.getUrl(tagHtml)
	for tu in tagUrl:		
		# f.write('\n' + tu[1] + '\n')
		# f.write('\n' + pre + tu[1] + '\n')
		kind_id = i
		tag_name = tu[1]
		tag_url = pre + tu[1]
		db.saveTagUrl(kind_id, tag_name, tag_url)	
		j = j + 1
		print 'save ' + str(j) + 'data\n'
	i = i + 1
	