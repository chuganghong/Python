import pygame,sys
print 'please enter some words:\n'
str = raw_input()
if str == 'y':
	print 'music turn on'
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
elif str == 'n':
	print 'over'