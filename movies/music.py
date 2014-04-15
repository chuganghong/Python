# Filename:	music.py

import pygame

pygame.init()
pygame.mixer.init()
m = pygame.mixer.music.load('time.mp3')


pygame.mixer.music.play(5)

