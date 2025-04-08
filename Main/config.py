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
health_img = "bilder/health.png"
fuel_img = "bilder/fuel.png"
font_img = "bilder/font.otf"
bullet_img = "bilder/bullet.png"

font = pygame.font.Font(font_img, 20)




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

#Ship setup
p1 = pygame.image.load(p1_img)
p1 = pygame.transform.scale(p1, (30,25))

p2 = pygame.image.load(p2_img)
p2 = pygame.transform.scale(p2, (30,25))

#Rock setup
rock = pygame.image.load(rock1_img)
rock = pygame.transform.scale(rock, (80,80))



#Health
heals = pygame.image.load(health_img)
heals = pygame.transform.scale(heals, (30, 30))
current_health = 1000
max_health = 1000
health_bar_length = 200
health_ratio = max_health / health_bar_length

bullet = pygame.image.load(bullet_img)
bullet = pygame.transform.scale(bullet, (30,30))
bullet = bullet.convert()





#Fuel
fuels = pygame.image.load(fuel_img)
fuels = pygame.transform.scale(fuels, (30,25))
current_fuel = 1000
max_fuel = 1000
fuel_bar_length = 200
fuel_ratio = max_fuel / fuel_bar_length


#Ship physics
thrust = 1.2
friction = 0.85
gravity = vector(0,0.3)

