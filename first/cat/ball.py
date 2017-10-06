import pygame
import sys
from pygame.locals import *

pygame.init()
FPS = 300
fpsClock = pygame.time.Clock()
size = (600, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Animation')

class Circle(object):
    def __init__(self, a, b, c, d, e, f, g, h, i, j, k):
        self.v_x = a
        self.v_y = b
        self.radius = c
        self.p_x = d
        self.p_y = e
        self.width = f
        self.color = (g, h, i)
        self.windowW = j
        self.windowH = k

    def circle_run(self):
        if self.p_x > (self.windowW-self.radius) or self.p_x < self.radius:
            self.v_x = -self.v_x

        if self.p_y > (self.windowH-self.radius) or self.p_y < self.radius:
            self.v_y = -self.v_y
        self.p_x += self.v_x
        self.p_y += self.v_y
        pos = (self.p_x, self.p_y)
        pygame.draw.circle(screen, self.color, pos, self.radius, self.width)


class Rect(object):
    def __init__(self, a, b, c, d, e, f, g, h, i, j, k):
        self.v_x = a
        self.v_y = b
        self.p_x = c
        self.p_y = d
        self.width = e
        self.height = f
        self.color = (g, h, i)
        self.windowW = j
        self.windowH = k
    def rect_run(self):
        if self.p_x > (self.windowW-self.width) or self.p_x < 0:
            self.v_x = -self.v_x

        if self.p_y > (self.windowH-self.height) or self.p_y < 0:
            self.v_y = -self.v_y
        self.p_x += self.v_x
        self.p_y += self.v_y
        list = (self.p_x, self.p_y, self.width, self.height)
        pygame.draw.rect(screen, self.color, list, 0)


circle1 = Circle(-1, 1, 20, 77, 77, 0, 128, 128, 0, size[0], size[1])
rect1 = Rect(1, -1, 250, 150, 60, 40, 128, 0, 128, size[0], size[1])
rect2 = Rect(1, 1, 148, 136, 80, 20, 225, 0, 0, size[0], size[1])
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
