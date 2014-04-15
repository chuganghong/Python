# Filename: test_selectTags.py

import getDouban_module
import time
import sys
import pygame
from MyDB import MyDB

host = 'localhost'
root = 'root'
pwd = ''
db = 'movies'
chset = 'utf8'
db = MyDB(host,root,pwd,db,chset)

res = db.selectTags(3)
for r in res:
	print str(r[0]) + '\n'
	print str(r[1]) + '\n'
	print r[3] + '\n'
	print '---------------------\n'
else:
	print 'over'