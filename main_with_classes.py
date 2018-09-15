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

        self.initialize_display(5, 70)

        while not self.gameExit:
            self.screen.fill(self.BLACK)
            pygame.draw.rect(self.screen, self.WHITE, [self.firstPaddleLead_x, self.firstPaddleLead_y, 10, self.firstPaddleLength])
            pygame.draw.rect(self.screen, self.WHITE, [self.secondPaddleLead_x-15, self.secondPaddleLead_y, 10, self.secondPaddleLength])
            pygame.draw.rect(self.screen, self.WHITE, [self.ball_x, self.ball_y, 10, 10])

            pygame.display.update()

            self.keyboard_actions(10)
            self.move_paddles()

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

        if self.firstPaddleLead_y + self.firstPaddleLength > 600:
            self.y_change = 0
        elif self.firstPaddleLead_y < 0:
            self.y_change = 0

        self.secondPaddleLead_y += self.y_change_sec

        if self.secondPaddleLead_y + self.firstPaddleLength > 600:
            self.y_change_sec = 0
        elif self.secondPaddleLead_y < 0:
            self.y_change_sec = 0

    def move_ball(self):
        pass

if __name__ == '__main__':
    Pong()

pygame.quit() # needed to quit. Uninitializes everything
quit()
