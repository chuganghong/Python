# Filename: getDouban_url.py

import getDouban_module
import time
import sys
import pygame
from MyDB import MyDB

reload(sys)
sys.setdefaultencoding('utf-8')

host = 'localhost'
root = 'root'
pwd = ''
db = 'movies'
chset = 'utf8'
db = MyDB(host,root,pwd,db,chset)


def getUrls(url,	tag_id):
	html = getDouban_module.getHtml(url)
	# print html
	pages = int(getDouban_module.getTotalPage(html))
	# print pages
	if pages == 0:
		getUrl(html,	tag_id)
		db.setTmpIf(1,tag_id)
	else:
		for i in range(pages):
			url2 = url + '?start=' + str(20*i) + '&type=T'
			html2 = getDouban_module.getHtml(url2)
			getUrl(html2,	tag_id)
			# if i == 5:
				# print 'over'
				# break
			# update tmp_tags tag_if
		db.setTmpIf(1,tag_id)
			
			

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

# play music		
def music():
	pygame.init()
	pygame.mixer.init()
	screen=pygame.display.set_mode([450,300])
	pygame.time.delay(1000)
	pygame.mixer.music.load("time.mp3")
	pygame.mixer.music.play()
	while 1:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				sys.exit()
				# break


def getU():
	print 'Enter a number:'
	n = raw_input()	
	res = db.selectTags(int(n))
	for r in res:
		url = r[3]
		tag_id = int(r[0])
		start = time.time()	
		getUrls(url,	tag_id)
		end = time.time()
		cost = end - start
		log = str(tag_id) + ' cost ' + str(cost) + '\n'
		print log
		getDouban_module.saveData(log,'time.txt')		
	# else:
	print 'for loop is over'		
	music()
	print 'Do you want to continue?Y/N'
	yn = raw_input()
	if yn == 'Y':
		getU()
	elif yn == 'N':
		print 'Game over!'

# start
getU()	




	

# getDouban_module.saveData(pages,'test4.txt')

