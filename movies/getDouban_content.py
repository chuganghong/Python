# Filename: getDouban_url.py

import getDouban_module
import time
import sys
import pygame
import random
import urllib2
import gzip
import StringIO
from MyDB import MyDB

reload(sys)
sys.setdefaultencoding('utf-8')

# cheat
def cheat_get_html(url,req_header):
	req_timeout = 5
	req = urllib2.Request(url,None,req_header)
	resp = urllib2.urlopen(req,None,req_timeout)
	html = resp.read()
	html = gzip.GzipFile(fileobj=StringIO.StringIO(html), mode="r")
	html = html.read()
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
def getTmpContent(headers):
	print 'Please enter a number:'
	n = raw_input()
	urls = db.selectTmpFilm(int(n))
	
	minute = 8*60
	
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

		# global req_header
		# html = cheat_get_html(url,req_header)
		
		
		try:
			# html = getDouban_module.getHtml(url)
			# global req_header
			w = random.randint(0, 1)
			req_header = headers[w]
			html = cheat_get_html(url,req_header)
			
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
		msg = tmp_title + ' save success'
		msg = msg.decode('utf-8').encode('gbk','ignore')
		print msg
	print 'for loop is over'		
	music()

host = 'localhost'
root = 'root'
pwd = ''
db = 'movies'
chset = 'utf8'
db = MyDB(host,root,pwd,db,chset)


req_header3 = {'Accept':'image/png,image/*;q=0.8,*/*;q=0.5',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
'Connection':'keep-alive',
'Cookie':'bid="BLn+omNAXcQ"; ll="130294"; __utma=30149280.754383318.1398390202.1398390202.1398390202.1; __utmb=30149280.3.10.1398390202; __utmc=30149280; __utmz=30149280.1398390202.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
'Host':'img3.douban.com',
'Referer':'http://movie.douban.com/subject/1295644/?qq-pf-to=pcqq.temporaryc2c',
'User-Agent':'Mozilla/5.0 (Windows NT 5.1; rv:28.0) Gecko/20100101 Firefox/28.0'
}


req_header2 = {'Host':'movie.douban.com',
'Connection': 'keep-alive',
'Accept': '*/*',
'X-Requested-With': 'XMLHttpRequest',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36',
'Referer': 'http://movie.douban.com/subject/6558801/',
'Accept-Encoding': 'gzip,deflate,sdch',
'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
'Cookie': 'bid="S2bsJtblOa0"; ll="118281"; viewed="1200840_1867455_1968704_10561367_1786120"; __utma=30149280.1560064197.1396532637.1397986989.1398359268.25; __utmb=30149280.1.10.1398359268; __utmc=30149280; __utmz=30149280.1397986989.24.12.utmcsr=movie.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=223695111.718571462.1396532637.1397984603.1398359268.16; __utmb=223695111.1.10.1398359268; __utmc=223695111; __utmz=223695111.1396871972.9.5.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/'
}

req_header1 = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Cookie':'bid="xtib4P+3ofQ"; __utma=30149280.1136841182.1394971055.1396533170.1398352253.11; __utmz=30149280.1396371265.9.8.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; ll="118281"; __utma=223695111.1098910402.1395479175.1396533170.1398352253.10; __utmz=223695111.1396371265.8.7.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmb=30149280.1.10.1398352253; __utmc=30149280; __utmb=223695111.1.10.1398352253; __utmc=223695111',
'Host':'movie.douban.com'
}

headers = [req_header1,req_header2]

getTmpContent(headers)