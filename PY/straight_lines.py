import pygame
from math import *
import numpy as np
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Program')
color = (0,0,0)
running  = True
clock = pygame.time.Clock()
mouseDown = (0,0)
#mouseUp = (0,0)

while running:
    
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
           running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseDown = pygame.mouse.get_pos()
            pygame.draw.line(screen, (255,255,255), (mouseDown), (pygame.mouse.get_pos()))
            if event.button == 3:
                screen.fill(color)
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button != 3:
                mouseUp = pygame.mouse.get_pos()
                pygame.draw.line(screen, (255,255,255), (mouseDown), (mouseUp))

    
    
    clock.tick(60)
    pygame.display.update()