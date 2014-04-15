# Filename: getDouban_url.py

import getDouban_module
import time
import sys
import pygame
from MyDB import MyDB

reload(sys)
sys.setdefaultencoding('gb2312')


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

# get film content
def getTmpContent():
	print 'Please enter a number:\n'
	n = raw_input()
	urls = db.selectTmpFilm(int(n))
	
	# print urls
	# return False
	
	for ur in urls:
	
		url = ur[3]
		tag_id = url[2]
		film_id = url[0]
		print ur
		print ur[0]
		print ur[1]
		print ur[2]
		print url[3]
		print url[4]
		return False
		html = getDouban_module.getHtml(url)
		tmp_title = getDouban_module.getTitle(html)
		# print title
		tmp_info = getDouban_module.getInfo(html)
		tmp_related_info = getDouban_module.getRelatedInfo(html)
		db.saveTmpFilmContent(tag_id, tmp_title, tmp_info,  tmp_related_info)
	db.setTmpFilmIf(1,film_id)
	print 'for loop is over'		
	music()

host = 'localhost'
root = 'root'
pwd = ''
db = 'movies'
chset = 'utf8'
db = MyDB(host,root,pwd,db,chset)

getTmpContent()


# getDouban_module.saveData('\n' + title + '\n','content.txt')
# getDouban_module.saveData('\n' + info + '\n','content.txt')
# getDouban_module.saveData('\n' + relatedInfo + '\n','content.txt')
	

# getDouban_module.saveData(pages,'test4.txt')

