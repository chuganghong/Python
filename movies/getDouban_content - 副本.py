# Filename: getDouban_url.py

import getDouban_module
import time
import sys
import pygame
import random
import urllib2
from MyDB import MyDB

reload(sys)
sys.setdefaultencoding('utf-8')

# cheat
def cheat_get_html(url,req_header):
	req_timeout = 5
	req = urllib2.Request(url,None,req_header)
	resp = urllib2.urlopen(req,None,req_timeout)
	html = resp.read()
	# print html
	# return False
	return html


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
	print 'Please enter a number:'
	n = raw_input()
	urls = db.selectTmpFilm(int(n))
	
	minute = 5*60
	
	start = int(time.time())
	for ur in urls:	
		current_time = int(time.time())
		cost = current_time - start
		if( (cost != 0) and (cost%minute == 0)):		
			second = random.uniform(60, 180)
			print 'sleep ' + str(second) + '.....'			
			time.sleep(second)
			print 'wake up!Start to work...'
		
		url = ur[3]
		tag_id = ur[2]
		film_id = ur[0]	
		# print film_id
		# return False
		try:
			html = getDouban_module.getHtml(url)
			# global req_header
			# html = cheat_get_html(url,req_header)
		except:
			msg = 'get ' + str(tag_id) + ' ' + url + ' faild\n'
			filename = 'filmError.txt'
			print 'Error:' + msg + '\n'
			getDouban_module.saveData(msg,filename)
			error_if = 1
			db.setTempFilmError(film_id,error_if)
			continue
		tmp_title = getDouban_module.getTitle(html)
		# print title
		tmp_info = getDouban_module.getInfo(html)
		tmp_related_info = getDouban_module.getRelatedInfo(html)
		db.saveTmpFilmContent(tag_id, tmp_title, tmp_info,  tmp_related_info)
		db.setTmpFilmIf(1,film_id)
		print tmp_title + ' save success'
	print 'for loop is over'		
	# music()

host = 'localhost'
root = 'root'
pwd = ''
db = 'movies'
chset = 'utf8'
db = MyDB(host,root,pwd,db,chset)

req_header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:28.0) Gecko/20100101 Firefox/28.0',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Cookie':'bid="hsM53yRAjQ8"; __utma=30149280.907110929.1386117661.1398322932.1398335444.20; __utmz=30149280.1398167843.17.13.utmcsr=baidu|utmccn=(organic)|utmcmd=organic|utmctr=urllib2%20403; ll="118281"; __utma=223695111.1156190174.1396328833.1398322932.1398335444.11; __utmz=223695111.1396588375.4.4.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmb=30149280.1.10.1398335444; __utmc=30149280; __utmb=223695111.1.10.1398335444; __utmc=223695111',
'Host':'movie.douban.com'
}

getTmpContent()