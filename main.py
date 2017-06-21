# Attempt at Pong
# Adrian Wisla

import pygame
#from pygame.locals import *
from sys import exit
import random


x = pygame.init()
resolution=(800,600)
clock = pygame.time.Clock() # pygame's clock object. 
FPS=30

WHITE = (255, 255, 255) # RGB values in tuples
BLACK = (0, 0, 0)
RED = 	(255, 0, 0)
GREEN = (0, 155, 0)  

screen=pygame.display.set_mode((800,600))
pygame.display.set_caption('MyPong')

#pygame.display.update()#this is to update the screen

gameExit = False

firstPaddleLead_x = 5
firstPaddleLead_y = 0
firstPaddleLength = 70

secondPaddleLead_x = 800
secondPaddleLead_y = 0
secondPaddleLength = 70

ball_x = resolution[0]/2
ball_y = resolution[1]/2

y_change=0

while not gameExit:
	
	
	screen.fill(BLACK)
	pygame.draw.rect(screen, WHITE, [firstPaddleLead_x,firstPaddleLead_y,10,firstPaddleLength])
	pygame.draw.rect(screen, WHITE, [secondPaddleLead_x-15,secondPaddleLead_y,10,secondPaddleLength])
	pygame.draw.rect(screen, WHITE, [ball_x,ball_y,10,10])
	
	pygame.display.update()
	
# This code lets the first paddle move around.
	# for event in pygame.event.get():
		# if event.type == pygame.QUIT:
			# gameExit = True
				

		# if event.type == pygame.KEYDOWN:
			
			# if event.key == pygame.K_DOWN and firstPaddleLead_y < 600 - firstPaddleLength:
				# y_change = 10
				# print(y_change)
				
			# elif firstPaddleLead_y > 600 - firstPaddleLength:		
				# y_change = 0	
			# if event.key == pygame.K_UP:
				# y_change = -10
			
			
		# if event.type == pygame.KEYUP:
			# if event.key == pygame.K_DOWN:
				# y_change = 0
			# elif event.key == pygame.K_UP:
				# y_change = 0
				
	# if firstPaddleLead_y + firstPaddleLength > 600 or firstPaddleLead_y < 0:
		# print(firstPaddleLead_y)
		
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_DOWN:
				y_change = 10
				print(firstPaddleLead_y)	
			elif event.key == pygame.K_UP:
				y_change = -10
				
		if event.type == pygame.KEYUP:
			y_change = 0
	
	# if firstPaddleLead_y + firstPaddleLength > 600:
		# y_change = 0
	firstPaddleLead_y += y_change
	if firstPaddleLead_y + firstPaddleLength > 600:
		y_change = 0
	elif firstPaddleLead_y < 0:
		y_change = 0
	clock.tick(FPS)
	
pygame.quit() # needed to quit. Uninitializes everything
quit()