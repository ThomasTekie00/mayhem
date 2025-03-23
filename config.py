import pygame
import config


#Setup:
SCREEN_X = 1200
SCREEN_Y = 800
screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
pygame.display.set_caption("Mayhem")
running = True
BACKGROUND_COLOR = (0,0,0)
clock = pygame.time.Clock()


#Filbaner til bildene:

p1_img = "p1.png"
p2_img = "p2.png"





#Spiller bevegelse:
GRAVITY = 0.2
THRUST = 0.5
ROTATION_SPEED = 5
MAX_SPEED = 10
FRICTION = 0.8

#Romskip innstillinger:
SHIP_SIZE = (30,20)
STARTING_FUEL = 1000
#Per thrust
DRAIN_FUEL = 1



#våpen
BULLET_SPEED = 5
BULLET_SIZE = 5
BULLET_TIME = 15
BULLET_LIFE = 120


#Plattform
PLATFORM_X = 80
PLATFORM_Y = 10

#Hindringer 
OBSTACLE_COLOR = (128, 128, 128)



#Pickups









#Kontroller
#Spiller 1
P1_LEFT = pygame.K_a
P1_RIGHT = pygame.K_d
P1_THRUST = pygame.K_w
P1_FIRE = pygame.K_SPACE

#Spiller 2
P2_LEFT = pygame.K_LEFT
P2_RIGHT = pygame.K_RIGHT
P2_THRUST = pygame.K_UP
P2_FIRE = pygame.K_RSHIFT