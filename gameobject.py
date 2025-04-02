import pygame
import random

vector = pygame.math.Vector2



class PickUps(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        super().__init__()
        self.image = image 
        self.rect = self.image.get_rect(center = pos)
        self.pos = vector(pos)

    def update(self):
        self.rect.center = self.pos
    #Spawn
    def respawn(self, SCREEN_X, SCREEN_Y):
        new_pos = (random.randint(100, SCREEN_X - 100), random.randint(100, SCREEN_Y - 100))
        self.pos = new_pos
        self.rect.center = self.pos
        return self.pos



class Fuel(PickUps):
    def __init__(self, image, pos, fuel_amount = 200):
        super().__init__()
        self.fuel_amount = fuel_amount



class Health(PickUps):
    def __init__(self, image, pos, health_amount = 100):
        super().__init__()
        self.health_amount = health_amount


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
    


class Bullet(pygame.sprite.Sprite)
    def __init__(self):
        pass

    #Movement
    #Killself
    #Fart
    #

