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
fuel_img = "bilder/fuel.png"
health_img = "bilder/health.png"

#Bakgrunnen
background = pygame.image.load(bk_img)
background = pygame.transform.scale(background,(SCREEN_X, SCREEN_Y))
background = background.convert()
#Får fargen til bunnen av skjermen slik at jeg kan bruke det som en platform

#Health
fuel_can = pygame.image.load(fuel_img)
fuel_can = pygame.transform.scale(fuel_can, (40,40))
#fuel_can = 

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
        self.health_bar_length = 200
        self.health_ratio = self.maximum_health / self.health_bar_length

        self.current_fuel = 1000
        self.maximum_fuel = 1000
        self.fuel_bar_length = 200
        self.fuel_ratio = self.maximum_fuel / self.fuel_bar_length

        self.is_landed = False

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

    def basic_fuel(self):
        pygame.draw.rect(screen, "Green", (10,50, self.current_fuel / self.fuel_ratio, 25 ))
        pygame.draw.rect(screen, "white", (10, 50, self.health_bar_length, 25), 5) 

    def get_fuel(self, amount):
        if self.current_fuel < self.maximum_fuel:
            self.current_fuel += amount
        if self.current_fuel >= self.maximum_fuel:
            self.current_fuel = self.maximum_fuel

    def lose_fuel(self, amount):
        if self.current_fuel > 0:
            self.current_fuel -= amount
        if self.current_fuel < 0:
            self.current_fuel = 0




    def acc(self):
        self.vel += self.direction * self.thrust



    def update(self):
       
        #PURE MOVEMENT AND SCREEN WRAPPIGN
       #Sjekker hvilken taster som er trykket 
       key = pygame.key.get_pressed()

       #Nullstilling 
       self.angle_speed = 0


       if key[pygame.K_RIGHT]:
           self.angle_speed += -5
       if key[pygame.K_LEFT]:
           self.angle_speed += 5
       if key[pygame.K_UP]:
           self.acc()
           self.lose_fuel(2)

       #Oppdatere vinkel på hvor nesen peker basert på rotatsjonshastighet 
       self.angle += self.angle_speed
       #Oppdatering retningsvektoren basert på ny vinkel
       self.direction = vector(0, -1). rotate(-self.angle)

       #Fartdemper 
       self.vel *= 0.85

       
       #Posisjon oppdatering med fart 
       self.pos += self.vel

       #Bilde rotatsjon 
       self.image = pygame.transform.rotate(self.original_image, self.angle)

       self.rect = self.image.get_rect(center = self.pos) 

       self.Flyzone()
       self.gravity()

    
    def gravity(self):
        #Konstant nedtrekk på y aksen
        self.vel += vector(0,0.1)


    def Flyzone(self):
        #Skipet går ut på venstre, kommer inn på høyre side(Siden x,y aksen starter på top venstre)
        if self.pos.x < 0:
            self.pos.x = SCREEN_X
        elif self.pos.x > SCREEN_X:
            self.pos.x = 0
        if self.pos.y < 0:
            self.pos.y = SCREEN_Y
        elif self.pos.y > SCREEN_Y:
            self.pos.y = 0


class Fuel(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=pos)
        self.pos = vector(pos)
    def update(self):
        self.rect.center = self.pos
    

class Health(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        super().__init__()
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (30,30))
        self.rect = self.image.get_rect(center=pos)
        self.pos = vector(pos)

    



class RockShower(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        
        #Tilfeldig X start
        start_x = random.randint(100,900)
        start_y = random.randint(-300, -50)

        self.pos = vector(start_x, start_y)

        #Randomfart
        speed_x = random.uniform(-0.8, 0.8)
        speed_y = random.uniform(1,4)

        self.vel = vector(speed_x, speed_y)
        self.rect.center = self.pos

    def update(self):
        #Bevegelse
        self.pos += self.vel
        self.rect.center = self.pos

        #Fra bunnen tilbake til toppen, random høyde og start
        if self.rect.top > 600:
            self.pos.x = random.randint(100, 900)
            self.pos.y = random.randint(-200, -50)

            #Tilfeldig fart også
            self.vel.x = random.uniform(-0.8, 0.8)
            self.vel.y = random.uniform(1, 4)








#Meteor 1
stein = pygame.image.load(rock_img)
stein = pygame.transform.scale(stein, (80,80))
stein_y_pos = 0

#Meteor 2
stein_2 = pygame.image.load(rock2_img)
stein_2 = pygame.transform.scale(stein_2, (200,200))







rockshower_group = pygame.sprite.Group()

all_sprites = pygame.sprite.Group()

health_group = pygame.sprite.Group()
health_pos = ((random.randint(200, SCREEN_X - 50), random.randint(200, SCREEN_Y - 50)))
health_ob = Health(health_img, health_pos)
health_group.add(health_ob)
all_sprites.add(health_ob)

fuel_group = pygame.sprite.Group()
fuel_pos = (random.randint(200, SCREEN_X - 200), random.randint(200, SCREEN_Y - 200))
fuel_ob = Fuel(fuel_can, fuel_pos)
fuel_group.add(fuel_ob)
all_sprites.add(fuel_ob)


for i in range(4):
    rock = RockShower(stein)
    all_sprites.add(rock)
    rockshower_group.add(rock)


ship = Starship(skip1, (SCREEN_X // 2, SCREEN_Y), (0,0))

all_sprites.add(ship)


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
    fuel_check = pygame.sprite.spritecollide(ship, fuel_group, True)
    if fuel_check:
        ship.get_fuel(500)

        new_fuel_pos = (random.randint(100, SCREEN_X - 100), random.randint(100, SCREEN_Y - 100))
        new_fuel = Fuel(fuel_can, new_fuel_pos)
        fuel_group.add(new_fuel)
        all_sprites.add(new_fuel)
    
    health_check = pygame.sprite.spritecollide(ship, health_group, True)
    if health_check:
        ship.get_health(500)

        new_health_pos = (random.randint(100, SCREEN_X - 100), random.randint(100, SCREEN_Y - 100))
        new_health = Health(health_img, new_health_pos)
        health_group.add(new_health)
        all_sprites.add(new_health)




    all_sprites.update()

    
    
    screen.blit(background, (0,0))
    all_sprites.draw(screen)
    ship.basic_health(screen)
    ship.basic_fuel()
    fuel_group.draw(screen)
    health_group.draw(screen)
    
    #pygame.draw.rect(screen, (255, 0, 0), ship.rect, 1)
    
    screen.blit(text_surface, (800, 100))

    pygame.display.flip()
    clock.tick(60)
    

pygame.quit()


