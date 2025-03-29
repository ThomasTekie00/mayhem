import pygame
import random

pygame.init()


sw = 1000
sh = 600
clock = pygame.time.Clock()
screen = pygame.display.set_mode((sw, sh))
vector = pygame.math.Vector2
run = True

#Filbaner
bk_img = "bilder/space.jpg"
ship1 = "bilder/p1.png"

#Tegne skjermen
background = pygame.image.load(bk_img)
background = pygame.transform.scale(background,(sw,sh))
background = background.convert()

skip = pygame.image.load(ship1)
skip = pygame.transform.scale(skip, (60,60))
skip = skip.convert_alpha()



class StarShip(pygame.sprite.Sprite):
    def __init__(self, image, pos, vel):
        super().__init__()
        self.image = image
        self.original_img = image
        self.rect = self.image.get_rect(center=pos)
        self.pos = vector(pos)
        self.vel = vector(vel)
        self.direction = vector(0,-1)
        self.angle = 0
        self.angle_speed = 0
        self.thrust = 0.3


    def acc(self):
        self.vel += self.direction * self.thrust
    
    def update(self):
        key = pygame.key.get_pressed()

        self.angle_speed = 0

        if key[pygame.K_a]:
            self.angle += 5
        if key[pygame.K_d]:
            self.angle -= 5
        if key[pygame.K_w]:
            self.acc()
        if key[pygame.K_s]:
            self.vel *= 0.95

        self.pos += self.vel

        
      


ship = StarShip(skip, (sw // 2, sh), (0,0))

all_sprites = pygame.sprite.Group()
all_sprites.add(ship)




while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    all_sprites.update()
    screen.blit(background, (0,0))
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)
    

pygame.quit()
