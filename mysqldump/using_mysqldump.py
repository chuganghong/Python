# Filename:using_mysqldump.py
# using mysqldump to backup database

import os
import traceback

def dumpdb(db, target):
	global user
	global pwd
	
	
	sqlvalformat = "E:/cg/wamp/bin/mysql/mysql5.6.12/bin/mysqldump -u%s -p%s %s>%s"
	sqlval = sqlvalformat % (user,pwd,db,target)
	result = os.system(sqlval)
	
def startdb():
	sqlval = r"E:/cg/wamp/bin/mysql/mysql5.6.12/bin/mysqld -install"
	result = os.system(sqlval)

def closedb():
	sqlval = "E:/cg/wamp/bin/mysql/mysql5.6.12/bin/mysqladmin -uroot -shutdown"
	result = os.system(sqlval)
	
def startwamp():
	cmdval = r"E:/cg/wamp/wampmanager"
	result = os.system(cmdval)


	

host = 'localhost'
user = 'root'
pwd = ''

db = 'rising'
target = r'E:/www/Github/python/mysqldump/h.sql'

result = startwamp()
# print result

dumpdb(db, target)

# result = closedb()
# print result
