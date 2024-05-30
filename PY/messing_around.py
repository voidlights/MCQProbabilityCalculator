import pygame
from math import *
import numpy as np
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Program')
color = (255,125,69)
ptcol = (69,125,255)
SizeScale = 10
angle_x = angle_y = angle_z = 0
running  = True
clock = pygame.time.Clock()


cube_vertices = np.array([
    [1, 1, 1],     # Vertex 1
    [1, 1, -1],    # Vertex 2
    [1, -1, 1],    # Vertex 3
    [1, -1, -1],   # Vertex 4
    [-1, 1, 1],    # Vertex 5
    [-1, 1, -1],   # Vertex 6
    [-1, -1, 1],   # Vertex 7
    [-1, -1, -1]   # Vertex 8
])

projection_matrix = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
])

def connect_points(i, j, points, lncol):
        pygame.draw.line(screen,(lncol), ( points[i] ), ( points[j] ) )

while running:
    
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
           running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:  # Scroll up
                screen.fill(color)
                SizeScale += 1
                
            elif event.button == 5:  # Scroll down
                screen.fill(color)
                SizeScale -= 1
                
        
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_UP]:
        
        angle_x += 1/360 * pi

    elif keys[pygame.K_DOWN]:
        
        angle_x -= 1/360 * pi
        
    elif keys[pygame.K_LEFT]:
        
        angle_y -= 1/360 * pi
        
    elif keys[pygame.K_RIGHT]:
        
        angle_y += 1/360 * pi
            
    screen.fill(color)

    points = []
    i = 0
    for vertex in cube_vertices:
        rotation_x = np.array([
            [1, 0, 0],
            [0, cos(angle_x), -sin(angle_x)],
            [0, sin(angle_x), cos(angle_x)]
        ])

        rotation_y = np.array([
            [cos(angle_y), 0, sin(angle_y)],
            [0, 1, 0],
            [-sin(angle_y), 0, cos(angle_y)]
        ])

        rotation_z = np.array([
            [cos(angle_z), -sin(angle_z), 0],
            [sin(angle_z), cos(angle_z), 0],
            [0, 0, 1]
        ])

        rotate_x = np.dot(rotation_x, vertex)
        rotate_y = np.dot(rotation_y, rotate_x)
        rotate_z = np.dot(rotation_z, rotate_y)
        point2d = np.dot(projection_matrix, rotate_z)
    
        x_coord = int(point2d[0] * SizeScale + 400)
        y_coord = int(point2d[1] * SizeScale + 300)

        points.append((x_coord, y_coord))

        pygame.draw.circle(screen, ptcol, (x_coord, y_coord), 5)
    connect_points(0, 1, points, (255,0,0))
    connect_points(1, 3, points, (0,255,0))
    connect_points(3, 2, points, (255,255,255))
    connect_points(2, 0, points, (255,255,255))
    connect_points(4, 5, points, (255,255,255))
    connect_points(5, 7, points, (255,255,255))
    connect_points(7, 6, points, (255,255,255))
    connect_points(6, 4, points, (255,255,255))
    connect_points(0, 4, points, (255,255,255))
    connect_points(1, 5, points, (0,0,255))
    connect_points(2, 6, points, (255,255,255))
    connect_points(3, 7, points, (255,255,255))
    
    clock.tick(60)
    pygame.display.update()
        

    
    


