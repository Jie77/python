import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 60 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
catImg = pygame.image.load('cat.png')
mouseImg = pygame.image.load('mouse.png')
catx = 10
caty = 10
mousex = 180
mousey = 15
directioncat = 'right'
directionmouse = 'right'

while True: # the main game loop
    DISPLAYSURF.fill(WHITE)

    if directioncat == 'right':
        catx += 5
        if catx == 650:
            directioncat = 'down'
    elif directioncat == 'down':
        caty += 5
        if caty == 480:
            directioncat = 'left'
    elif directioncat == 'left':
        catx -= 5
        if catx == 30:
            directioncat = 'up'
    elif directioncat == 'up':
        caty -= 5
        if caty == 30:
            directioncat = 'right'

    if directionmouse == 'right':
        mousex += 5
        if mousex == 650:
            directionmouse = 'down'
    elif directionmouse == 'down':
        mousey += 5
        if mousey == 480:
            directionmouse = 'left'
    elif directionmouse == 'left':
        mousex -= 5
        if mousex == 30:
            directionmouse = 'up'
    elif directionmouse == 'up':
        mousey -= 5
        if mousey == 30:
            directionmouse = 'right'

    DISPLAYSURF.blit(catImg, (catx, caty))
    DISPLAYSURF.blit(mouseImg, (mousex, mousey))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
