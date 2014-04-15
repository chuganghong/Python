# Filename: getDouban_save.py

import MySQLdb

class MyDB:
	# Initialize a conn
	def __init__(self,host,root,pwd,db,chset):
		try:
			self.conn = MySQLdb.connect(host = 'localhost', user = 'root', passwd = '', db = 'movies', charset = 'utf8')
			self.cur = self.conn.cursor()
		except MySQLdb.Error,e:
			print 'Mysql Error %d: %s' % (e.args[0], e.args[1])
			
	# save log
	def saveError(msg,filename):
		f = file(filename,'a+')
		f.write(msg)
		f.close()
			
	# save tag and tag url
	def saveTagUrl(self, kind_id, tag_name, tag_url):
		try:
			value = [kind_id, tag_name, tag_url]
			# sql = 'INSERT INTO mo_tag (kind_id, tag_name, tag_url) VALUES (%s, %s, %s)'
			sql = 'INSERT INTO tmp_tags (kind_id, tag_name, tag_url) VALUES (%s, %s, %s)'
			self.cur.execute(sql,value)
			self.conn.commit()
		except MySQLdb.Error,e:
			print 'MySQL Error %d: %s' %s (e.args[0], e.args[1])
	
	# save tmp files
	def saveTmpFilms(self,	film_name,	tag_id,	film_url):
		try:
			value = [film_name,	tag_id,	film_url]
			sql	=	'INSERT INTO tmp_films (film_name,	tag_id,	film_url)	VALUES	(%s,	%s,	%s)'
			self.cur.execute(sql,value)
			self.conn.commit()			
			# self.setTmpIf(1,tag_id)
			print 'save ' + film_url + ' success'
		except MySQLdb.Error,e:
			# print 'MySQL Error %d:	%s'	%s	(e.args[0],	e.args[1])
			msg = msg + '\n'
			filename = 'tmp_film_' + str(tag_id) + '.txt'
			self.saveError(msg,filename)
	# save tmp film content
	def saveTmpFilmContent(self, tag_id, tmp_title, tmp_info,  tmp_related_info):
		try:
			value = [tag_id, MySQLdb.escape_string(tmp_title), MySQLdb.escape_string(tmp_info), MySQLdb.escape_string(tmp_related_info)]
			sql = 'INSERT INTO tmp_film_content (tag_id, tmp_title, tmp_info, tmp_related_info) VALUES (%s, %s, %s, %s)'
			self.cur.execute(sql, value)
			self.conn.commit()
			print 'save success\n'
		except MySQLdb.Error,e:
			# print 'MySQ Error %d: %s' %s (e.args[0], e.args[1])
			msg = msg + '\n'
			filename = 'tmp_film_content_' + str(tag_id) + '.txt'
			self.saveError(msg,filename)
		
	# save the content of a film
	def saveContent(self, tag_id, title, info, relatedInfo):
		try:
			value = [tag_id, title, info, relatedInfo]
			sql = 'INSERT INTO tmp_film_content (tag_id, tmp_title, tmp_info,tmp_related_info) VALUES (%s, %s, %s, %s)'
			self.cur.execute(sql,value)
			self.conn.commit()
		except MySQLdb.Error,e:
			# print 'MySQL Error %d: %s' %s (e.args[0], e.args[1])
			msg = 'MySQL Error %d: %s' %s (e.args[0], e.args[1])
			msg = msg + '\n'
			filename = 'tmp_film_' + str(tag_id) + '.txt'
			self.saveError(msg,filename)
	
	# select tag from tmp_tags
	def selectTags(self,n):
		sql = 'SELECT * FROM tmp_tags WHERE tag_if = 0'
		self.cur.execute(sql)
		res = self.cur.fetchmany(n)
		return res
		
	# select tmp_film from tmp_films
	def selectTmpFilm(self,n):
		sql = 'SELECT * FROM tmp_films WHERE film_if = 0'
		self.cur.execute(sql)
		res = self.cur.fetchmany(n)
		return res
	
	# update tmp_tags set tag_if = 1
	def setTmpIf(self,i,j):
		value = [i,j]
		sql = 'UPDATE tmp_tags SET tag_if=%s WHERE tag_id=%s'
		self.cur.execute(sql,value)
		self.conn.commit()
		
	# update tmp_films set film_if=1
	def setTmpFilmIf(self,i,j):
		value = [i,j]
		sql = 'UPDATE tmp_films SET film_if=%s WHERE film_id=%s'
		self.cur.execute(sql,value)
		self.conn.commit()
		
	
		
		
			
			
	