import pygame
import random
import math
import config

vector = pygame.math.Vector2



class PickUps(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        super().__init__()
        self.image = image 
        self.rect = self.image.get_rect(center = pos)
        self.pos = vector(pos)

        

    def update(self):
        self.rect.center = self.pos

    #Spawn test
    def respawn(self, SCREEN_X, SCREEN_Y):
        new_pos = (random.randint(100, SCREEN_X - 100), random.randint(100, SCREEN_Y - 100))
        self.pos = new_pos
        self.rect.center = self.pos
        return self.pos

    #Branch test

class Fuel(PickUps):
    def __init__(self, image, pos, fuel_amount = 200):
        super().__init__(image, pos)
        self.fuel_amount = fuel_amount
    
    def picked(self, ship):
        ship.get_fuel(self.fuel_amount)
        return True



class Health(PickUps):
    def __init__(self, image, pos, health_amount = 100):
        super().__init__(image,pos)
        self.health_amount = health_amount
    
    def picked(self, ship):
        ship.get_health(self.health_amount)
        return True



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
    


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, angle):
        super().__init__()
        self.original_image = pygame.Surface((5,5))
        self.original_image.fill("White")
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect(center=pos)
        self.pos = vector(pos)
        self.angle = angle
        self.speed = 10
        
        self.direction = vector(-math.sin(math.radians(self.angle)), -math.cos(math.radians(self.angle)))

    def update(self):
        self.pos += self.direction * self.speed
        

        self.rect.center = (round(self.pos.x), round(self.pos.y))

        
        
        

        

