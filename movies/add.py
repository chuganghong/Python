# Filename: add.py



import getDouban_module
import time
from MyDB import MyDB

host = 'localhost'
root = 'root'
pwd = ''
db = 'movies'
chset = 'utf8'
db = MyDB(host,root,pwd,db,chset)

			
			

def getUrl(html,	tag_id):
	p12 = getDouban_module.getP12(html)
	for p in p12:
		res = getDouban_module.getP12a(p)
		# print res
		pTitle = res[0][1]
		pUrl = res[0][0]
		# getDouban_module.saveData('\n' + pTitle + '\n','test55.txt')
		# getDouban_module.saveData('\n' + pUrl + '\n','test55.txt')
		db.saveTmpFilms(pTitle,	tag_id,	pUrl)
	

start = time.time()

tag_id = 1
url = 'http://movie.douban.com/tag/%E7%88%B1%E6%83%85?start=5460&type=T'
html2 = getDouban_module.getHtml(url)
getUrl(html2,	tag_id)
end = time.time()
cost = end - start
log = str(tag_id) + ' cost ' + str(cost) + '/n'
getDouban_module.saveData(log,'time.txt')


