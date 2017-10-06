import pygame
import sys
from pygame.locals import *

pygame.init()
FPS = 60
fpsClock = pygame.time.Clock()
size = (800, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Animation')

class Animal(object):
    def __init__(self, source, x, y, W, H):
        self.source = source
        self.x = x
        self.y = y
        self.direction = 'right'
        self.W = W
        self.H = H
    def run(self):
        if self.direction == 'right':
            self.x += 5
            if self.x == self.W-150:
                self.direction = 'down'
        elif self.direction == 'down':
            self.y += 5
            if self.y == self.H-120:
                self.direction = 'left'
        elif self.direction == 'left':
            self.x -= 5
            if self.x == 30:
                self.direction = 'up'
        elif self.direction == 'up':
            self.y -= 5
            if self.y == 30:
                self.direction = 'right'
        Img = pygame.image.load(self.source)
        pos = (self.x, self.y)
        screen.blit(Img, pos)

cat = Animal('cat.png', 10, 10, size[0], size[1])
mouse = Animal('mouse.png', 180, 15, size[0], size[1])

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))

    cat.run()
    mouse.run()

    pygame.display.update()
    fpsClock.tick(FPS)
