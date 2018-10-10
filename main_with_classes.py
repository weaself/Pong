# Attempt at Pong
# Adrian Wisla

import pygame
#from pygame.locals import *
from sys import exit
import random

class Pong(object):

    def __init__(self):
        self.x = pygame.init()
        self.gameExit = False
        self.speed_of_the_ball_y = 5
        self.speed_of_the_ball_x = 10

        self.initialize_display(5, 70)

        while not self.gameExit:
            self.screen.fill(self.BLACK)
            pygame.draw.rect(self.screen, self.WHITE, [self.firstPaddleLead_x, self.firstPaddleLead_y, 10, self.firstPaddleLength])
            pygame.draw.rect(self.screen, self.WHITE, [self.secondPaddleLead_x-15, self.secondPaddleLead_y, 10, self.secondPaddleLength])
            pygame.draw.rect(self.screen, self.WHITE, [self.ball_x, self.ball_y, 10, 10])

            pygame.display.update()
            #print(self.firstPaddleLead_y + self.firstPaddleLength)

            self.keyboard_actions(20)
            self.move_paddles()
            self.move_ball()
            self.check_if_player_loses()

            self.clock.tick(self.FPS)

    def initialize_display(self, paddle_width, paddle_length):
        self.resolution = (800, 600)
        self.clock = pygame.time.Clock()  # pygame's clock object.
        self.FPS = 30

        self.WHITE = (255, 255, 255)  # RGB values in tuples
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 155, 0)

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('MyPong')

        # pygame.display.update()#this is to update the screen

        self.firstPaddleLead_x = 5
        self.firstPaddleLead_y = 0
        self.firstPaddleLength = 70

        self.secondPaddleLead_x = 800
        self.secondPaddleLead_y = 0
        self.secondPaddleLength = 70

        self.ball_x = self.resolution[0] / 2
        self.ball_y = self.resolution[1] / 2

        self.y_change = 0
        self.y_change_sec = 0

    def keyboard_actions(self, speed):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.y_change = speed
                    print(self.firstPaddleLead_y)
                elif event.key == pygame.K_UP:
                    self.y_change = -speed
                elif event.key == pygame.K_w:
                    self.y_change_sec = -speed
                elif event.key == pygame.K_s:
                    self.y_change_sec = speed

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s or event.key == pygame.K_w:
                    self.y_change_sec = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    self.y_change = 0

        # if firstPaddleLead_y + firstPaddleLength > 600:
        # y_change = 0
    def move_paddles(self):

        self.firstPaddleLead_y += self.y_change

        if self.firstPaddleLead_y + self.firstPaddleLength >= 600:
            self.y_change = 0
        elif self.firstPaddleLead_y <= 0:
            self.y_change = 0

        self.secondPaddleLead_y += self.y_change_sec

        if self.secondPaddleLead_y + self.firstPaddleLength >= 600:
            self.y_change_sec = 0
        elif self.secondPaddleLead_y <= 0:
            self.y_change_sec = 0

    def move_ball(self):

        if self.ball_x >= self.secondPaddleLead_x - 20 or self.ball_x <= self.firstPaddleLead_x + 10:
            print('The ball got to the paddle lead!', self.secondPaddleLead_x - 15)
            if self.ball_y > self.secondPaddleLead_y or self.ball_y < self.secondPaddleLead_y + self.secondPaddleLength:
                print('The ball went beyond Y', self.ball_y, self.secondPaddleLead_y)
                self.speed_of_the_ball_x *= -1

        #print(self.ball_x)

        if self.ball_y > 600 - 10 or self.ball_y < 0:
            self.speed_of_the_ball_y *= -1
        #print('Ball x before addition: ', self.ball_x)
        self.ball_x += self.speed_of_the_ball_x
        #print('Is the speed still inverted? ', self.speed_of_the_ball)
        self.ball_y += self.speed_of_the_ball_y
        #print('Ball x after addition: ', self.ball_x)

    def check_if_player_loses(self):
        if self.ball_x <= 10 and (self.ball_y > self.firstPaddleLead_y + 60 or self.ball_y < self.firstPaddleLead_y):
            print('You lose!')
        #print(self.ball_x <= 0 and (self.ball_y > self.firstPaddleLead_y + 60 or self.ball_y < self.firstPaddleLead_y))
        print(self.ball_x, ' this is lead of the paddle: ', self.firstPaddleLead_y)

if __name__ == '__main__':
    Pong()

pygame.quit() # needed to quit. Uninitializes everything
quit()
