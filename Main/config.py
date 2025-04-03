import pygame



pygame.init()

#Vectors
vector = pygame.math.Vector2

#Filpaths
bk_img = "bilder/space.jpg"
p1_img = "bilder/p1.png"
p2_img = "bilder/p2.png"
rock1_img = "bilder/meteor1.png"
rock2_img = "bilder/meteor2.png"




#Screen Setup
SCREEN_X = 1000
SCREEN_Y = 600
FPS = 60


#Screen display:
screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
pygame.display.set_caption("Mayhem")

#Background setup
background = pygame.image.load(bk_img)
background = pygame.transform.scale(background,(SCREEN_X, SCREEN_Y))
background = background.convert()




#Health
current_health = 1000
max_health = 1000
health_bar_length = 200
health_ratio = max_health / health_bar_length


#Fuel
current_fuel = 1000
max_fuel = 1000
fuel_bar_length = 200
fuel_ratio = max_fuel / fuel_bar_length


#Ship physics
thrust = 0.8
friction = 0.85
gravity = vector(0,0.3)

