import pygame
from pygame.locals import *
import sys


FPS = 300 # frames per second setting
fpsClock = pygame.time.Clock()

class Circle():
    def __init__(self,a,b,c,d,e,f,g,h,i):
        self.vel_x = a
        self.vel_y = b
        self.radius = c
        self.pos_x = d
        self.pos_y = e
        self.width = f
        self.color = g, h, i


    def circle_run(self):
        if self.pos_x > 580 or self.pos_x < 20:
            self.vel_x = -self.vel_x

        if self.pos_y > 480 or self.pos_y < 20:
            self.vel_y = -self.vel_y
        self.pos_x += self.vel_x
        self.pos_y += self.vel_y
        pos = (self.pos_x, self.pos_y)
        pygame.draw.circle(screen, self.color, pos, self.radius, self.width)


class Rect():
    def __init__(self,a,b,c,d,e,f,g,h,i):
        self.vel_x = a
        self.vel_y = b
        self.pos_x = c
        self.pos_y = d
        self.width = e
        self.height = f
        self.color = g, h, i

    def rect_run(self):
        if self.pos_x > 540 or self.pos_x < 0:
            self.vel_x = -self.vel_x

        if self.pos_y > 460 or self.pos_y < 0:
            self.vel_y = -self.vel_y
        self.pos_x += self.vel_x
        self.pos_y += self.vel_y
        list = (self.pos_x, self.pos_y, self.width, self.height)
        pygame.draw.rect(screen, self.color, list, 0)

pygame.init()
screen = pygame.display.set_mode((600, 500))

circle1 = Circle(-1,1,20,77,77,0,128,128,0)
rect1 = Rect(1,-1,250,150,60,40,128,0,128)
rect2 = Rect(1,1,148,136,80,20,225,0,0)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    screen.fill((0, 0, 0))

    circle1.circle_run()
    rect1.rect_run()
    rect2.rect_run()

    pygame.display.update()
    fpsClock.tick(FPS)
