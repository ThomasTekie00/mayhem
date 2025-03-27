import pygame
import random


pygame.init()
run = True
SCREEN_X = 1000
SCREEN_Y = 600
vector = pygame.math.Vector2
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
pygame.display.set_caption("Mayhem")
background_color = (0,0,0)
test_font = pygame.font.Font("bilder/font.otf", 50)


#Font
text_surface = test_font.render("Mayheim", False, "red")


#Filbane
bk_img = "bilder/space.jpg"
bakke_img = "bilder/bak1.png"
p1_img = "bilder/p1.png"
p2_img = "bilder/p2.png"
rock_img = "bilder/meteor1.png"
rock2_img = "bilder/meteor2.png"

#Bakgrunnen
background = pygame.image.load(bk_img)
background = pygame.transform.scale(background,(SCREEN_X, SCREEN_Y))
background = background.convert()
#Får fargen til bunnen av skjermen slik at jeg kan bruke det som en platform



#Skip 1
skip1 = pygame.image.load(p1_img).convert_alpha()
skip1 = pygame.transform.scale(skip1, (30,25))
skip1 = pygame.transform.flip(skip1, True, False)
#skip1_rect = skip1.get_rect(center = (500,700))
#skip1_speed = 5


#Skip 2
#skip2 = pygame.image.load(p2_img).convert_alpha()
#skip2 = pygame.transform.scale(skip2, (60,50))
#skip2 = pygame.transform.flip(skip2, True, False)
#skip2_rect = skip2.get_rect(center = (500,700))
#skip2_speed = 5




    

class Starship(pygame.sprite.Sprite):
    def __init__(self, image, pos, vel):
        super().__init__()
        self.original_image = image
        self.image = image
        self.rect = self.image.get_rect(center=pos)
        self.pos = vector(pos)
        self.vel = vector(vel)
        self.direction = vector(0,-1)
        self.speed = 8
        self.angle = 0
        self.angle_speed = 0
        self.thrust = 0.8
        self.max_speed = 8

        self.current_health = 200
        self.maximum_health = 1000
        self.health_bar_length = 400
        self.health_ratio = self.maximum_health / self.health_bar_length

##### HEALTH #######################################################################################################
    def get_damage(self, amount):
        if self.current_health > 0:
            self.current_health -= amount
        if self.current_health < 0:
            self.current_health = 0

    def get_health(self, amount):
        if self.current_health < self.maximum_health:
            self.current_health += amount
        if self.current_health >= self.maximum_health:
            self.current_health = self.maximum_health
        
    def basic_health(self, surface):
        pygame.draw.rect(screen, "red", (10,10, self.current_health/self.health_ratio, 25))
        pygame.draw.rect(screen, "white", (10, 10, self.health_bar_length, 25), 5)  


    def acc(self):
        self.vel += self.direction * self.thrust



    def update(self):

        #PURE MOVEMENT AND SCREEN WRAPPIGN

       key = pygame.key.get_pressed()

       self.angle_speed = 0

       if key[pygame.K_RIGHT]:
           self.angle_speed += -5
       if key[pygame.K_LEFT]:
           self.angle_speed += 5
       if key[pygame.K_UP]:
           self.acc()
       if key[pygame.K_DOWN]:
           self.vel *= 0.95

       self.angle += self.angle_speed
       self.direction = vector(0, -1). rotate(-self.angle)

       self.vel *= 0.85

       self.vel += vector(0,0.1)

       self.pos += self.vel


       self.image = pygame.transform.rotate(self.original_image, self.angle)

       self.rect = self.image.get_rect(center = self.pos) 


        

       if self.rect.x < 0:
        self.pos.x = SCREEN_X
       elif self.pos.x > SCREEN_X:
        self.pos.x = 0
       if self.pos.y < 0:
        self.pos.y = SCREEN_Y
       elif self.pos.y > SCREEN_Y:
        self.pos.y = 0 



class RockShower(pygame.sprite.Sprite):
    def __init__(self, image, pos, vel):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.pos = vector(pos)
        self.vel = vector(vel)
    
    def update(self):
        self.pos += self.vel
        self.rect.center = self.pos

        if self.rect.left > SCREEN_X:
            self.pos.x = -self.rect.width/2
        elif self.rect.right < 0:
            self.pos.x = SCREEN_X + self.rect.width/2
            
        if self.rect.top > SCREEN_Y:
            self.pos.y = -self.rect.height/2
        elif self.rect.bottom < 0:
            self.pos.y = SCREEN_Y + self.rect.height/2



#Meteor 1
stein = pygame.image.load(rock_img)
stein = pygame.transform.scale(stein, (80,80))
stein_y_pos = 0

#Meteor 2
stein_2 = pygame.image.load(rock2_img)
stein_2 = pygame.transform.scale(stein_2, (200,200))




ship = Starship(skip1, (SCREEN_X // 2, SCREEN_Y), (0,0))
rockshower_group = pygame.sprite.Group()

all_sprites = pygame.sprite.Group()
all_sprites.add(ship)

for i in range(15):
    x_pos = random.randint(100, 900)
    y_pos = random.randint(100, 500)

    x_speed = random.uniform(-0.7, 0.7)
    y_speed = random.uniform(-0.7, 0.7)

    rock1 = RockShower(stein, (x_pos, y_pos), (x_speed, y_speed))
    all_sprites.add(rock1)






while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
#################################################################
##Delete: TEST
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ship.get_health(200)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                ship.get_damage(200)
#################################################################       


    all_sprites.update()
    
    screen.blit(background, (0,0))
    all_sprites.draw(screen)
    ship.basic_health(screen)
    

    screen.blit(text_surface, (800, 100))

    pygame.display.flip()
    clock.tick(60)
    

pygame.quit()


