import pygame
import random

pygame.init()

W_Width = 1400 
W_Height = 700

screen = pygame.display.set_mode((W_Width, W_Height))

clock = pygame.time.Clock()
fps = 60

running = True
gameplay = True
title_screen = False
game_over_screen = False

class Boat():
    def __init__(self,img,pos_x,pos_y,speed,maxspeed,friction):
        self.position = [pos_x,pos_y]
        self.collision_rect = pygame.Rect(pos_x,pos_y,60,60)
        self.img = pygame.image.load(img)
        self.velocity = [0,0]
        self.speed = speed
        self.max_speed = maxspeed
        self.friction = friction
class Rock():
    def __init__(self,img,pos_x,pos_y):
        self.position = [pos_x,pos_y]
        self.img = pygame.image.load(img)
        self.collision_mask = pygame.mask.from_surface(img)

player = Boat("boat_player.png",70,70,7,25,3)


        
while running:
    for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                running = False
    clock.tick(fps)
    keys = pygame.key.get_pressed()

    if gameplay:

        #boat movement
    
        if keys[pygame.K_LEFT]: 
            player.velocity[0] -= player.speed/fps
        elif keys[pygame.K_RIGHT]:
            player.velocity[0] += player.speed/fps
        if keys[pygame.K_UP]:
            player.velocity[1] -= player.speed/fps
        elif keys[pygame.K_DOWN]:
            player.velocity[1] += player.speed/fps

        if player.velocity[1] >= player.max_speed:
            player.velocity[1] = player.max_speed
        elif player.velocity[1] <= -player.max_speed:
            player.velocity[1] = -player.max_speed
            
        if player.velocity[0] >= player.max_speed:
            player.velocity[0] = player.max_speed
        elif player.velocity[0] <= -player.max_speed:
            player.velocity[0] = -player.max_speed
        
        player.position[0] += player.velocity[0]
        player.position[1] += player.velocity[1]
        
        if player.velocity[0] > 0:
            player.velocity[0] -= player.friction/fps
            if player.velocity[0] < 0:
                player.velocity[0] = 0
        elif player.velocity[0] < 0:
            player.velocity[0] += player.friction/fps
            if player.velocity[0] > 0:
                player.velocity[0] = 0
        if player.velocity[1] > 0:
            player.velocity[1] -= player.friction/fps
            if player.velocity[1] < 0:
                player.velocity[1] = 0
        elif player.velocity[1] < 0:
            player.velocity[1] += player.friction/fps
            if player.velocity[1] > 0:
                player.velocity[1] = 0
        
        player.collision_rect.x = player.position[0]
        player.collision_rect.y = player.position[1]
        
        #drawing the game
        screen.fill((65, 175, 255))
        screen.blit(player.img,(player.position[0],player.position[1]))
        
        pygame.display.flip()
