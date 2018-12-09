
import pygame, sys
import pygame.camera
from pygame.locals import *

pygame.init()
pygame.camera.init()

screen = pygame.display.set_mode ((640,480))

cam = pygame.camera.Camera ("/dev/video0",(640,480))
cam.start()

while 1:
    image = cam.get_image()
    screen.blit(image,(0,0,420,410))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

