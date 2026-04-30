import pygame
import random
import math

pygame.init()

W_Width = 1600 
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
        self.collision_rect = pygame.Rect(pos_x,pos_y,25,25)
        self.img = pygame.image.load(img)
        self.img = pygame.transform.scale2x(self.img)
        self.velocity = [0,0]
        self.speed = speed
        self.max_speed = maxspeed
        self.friction = friction
class Rock():
    def __init__(self,img,pos_x,pos_y):
        self.position = [pos_x,pos_y]
        self.img = pygame.image.load(img)
        #self.collision_mask = pygame.mask.from_surface(img)

player = Boat("boat_player.png",70,70,7,25,3)

rocks = []
for i in range(20):
    rocks.append(Rock("rock.png",random.randint(100,W_Width),random.randint(0,W_Height)))
        
while running:
    for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                running = False
    clock.tick(fps)
    keys = pygame.key.get_pressed()

    if gameplay:

        movement_direction = [0,0]
        
        #boat movement
        if keys[pygame.K_LEFT]: 
            player.velocity[0] -= player.speed/fps
            movement_direction[0] -= 1
        elif keys[pygame.K_RIGHT]:
            player.velocity[0] += player.speed/fps
            movement_direction[0] -= -1
        if keys[pygame.K_UP]:
            player.velocity[1] -= player.speed/fps
            movement_direction[1] -= -1
        elif keys[pygame.K_DOWN]:
            player.velocity[1] += player.speed/fps
            movement_direction[1] -= 1
        
        #max speed limit
        if player.velocity[1] >= player.max_speed:
            player.velocity[1] = player.max_speed
        elif player.velocity[1] <= -player.max_speed:
            player.velocity[1] = -player.max_speed
            
        if player.velocity[0] >= player.max_speed:
            player.velocity[0] = player.max_speed
        elif player.velocity[0] <= -player.max_speed:
            player.velocity[0] = -player.max_speed

        #changing position by adding veloctiy
        player.position[0] += player.velocity[0]
        player.position[1] += player.velocity[1]

        #adding friction
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
        
        player.collision_rect.x = player.position[0] - player.collision_rect.w/2
        player.collision_rect.y = player.position[1] - player.collision_rect.h/2
        
        #drawing the game
        screen.fill((65, 175, 255))

        
        
        temp_player_image = pygame.transform.rotate(player.img, math.degrees(math.atan2(movement_direction[1],movement_direction[0]))-90)
        screen.blit(temp_player_image,(player.position[0]-(temp_player_image.get_width()/2),player.position[1]-(temp_player_image.get_height()/2)))


        pygame.draw.rect(screen,(255,0,0,60),player.collision_rect)
        
        for rock in rocks:
            screen.blit(rock.img,(rock.position[0],rock.position[1]))
        pygame.display.flip()
