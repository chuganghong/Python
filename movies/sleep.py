# Filename:sleep.py

def sleep_say_i(n):
	import time
	while(n > 0):
		print n
		n = n - 1
		time.sleep(3)
	else:
		print 'while is over'

def no_sleep_say_i(n):
	import time
	while(n > 0):
		print n
		n = n - 1
	else:
		print 'while is over'

sleep_say_i(5)
no_sleep_say_i(10)
