import sys
import pygame
from pygame.locals import *

pygame.init()
# Resolution is ignored on Android
surface = pygame.display.set_mode((640, 480))
myfont = pygame.font.SysFont("Arial", 64)
label = myfont.render("Chandrayaan-3", 1, (255, 255, 255))

flag = pygame.image.load("flag.png")
moon = pygame.image.load("moon.png")
rocket = pygame.image.load("rocket.png")
 
rocketrect = rocket.get_rect()
clock = pygame.time.Clock()

width = surface.get_width()
height = surface.get_height()

speed = [-2, 15]
speed2 = [0,-8]
while True:
    for ev in pygame.event.get():
        if ev.type == QUIT:
            pygame.quit()
    clock.tick(60)
    surface.fill((0, 0, 0))
    
    rocketrect = rocketrect.move(speed)
    surface.blit(rocket,(0,50), rocketrect)
    
    surface.blit(moon,(0,480))
    surface.blit(label,(110,300))
    surface.blit(flag,(110,-150))
    pygame.display.flip()
