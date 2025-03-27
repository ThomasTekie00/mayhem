import pygame
import random

vector = pygame.math.Vector2



class PickUps(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        super().__init__()
        self.image = image
        self.width = 60
        self.height = 60
        self.pos = vector(pos)
        self.rect = self.image.get_rect(center=pos)

    def update(self):
        self.rect.center = self.pos

    def picked(self):
        pass


class Fuel(PickUps):
    def __init__(self, image, pos, fuel_amount = 200):
        super().__init__()
        self.fuel_amount = fuel_amount

    def picked(self):
       pass


class Health(PickUps):
    def __init__(self, image, pos, health_amount = 100):
        super().__init__()
        self.health_amount = health_amount


class Fuel(PickUps):
    def __init__(self, image, pos, fuel_amount = 200):
        super().__init__()
        self.fuel_amount = fuel_amount

    def picked(self):
        pass

class RockShower(pygame.sprite.Sprite):
    




