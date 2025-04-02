from gameobject import gameobject
from config import config

vector = pygame.math.Vector2

import pygame
import math
import random







class Blueprint(pygame.sprite.Sprite):
    def __init__(self, image, pos, vel):
        super().__init__()
        self.image = image
        self.original_image = image
        self.rect = self.image.get_rect(center = pos)

        self.vel = vector(vel)
        self.pos = vector(pos)

        self.direction = vector(0,-1)
        self.angle = 0
        self.thrust = 0.8
      

        """
        Health system:
        - Function for health
        - Max health variable
        - Current health variable
        - Health ratio
        """
        self.current_health = 1000
        self.max_health = 1000
        self.health_bar_length = 200
        self.health_ratio = self.max_health / self.health_bar_length

        """
        Fuel system
        - Function for fuel
        - Max fuel variable
        - Current fuel variable
        - fuel ratio
        """
        self.current_fuel = 1000
        self.max_fuel = 1000
        self.fuel_bar_length = 200
        self.fuel_ratio = self.max_fuel / self.fuel_bar_length

        """
        Method for player speed in the direction they are facing:
        Acceleration
        - Self.direction = Defines the direction the object will accelerate in
        - Self.thrust = Controls the speed of the acceleration
        Which puts the effect into how the object moves
        - Self.vel
        """
    def acceleration(self):
        self.vel += self.direction * self.thrust

    def update(self):
        self.pos += self.vel





    def screen_bounds(self):
        #If ship goes out of bounds to the left, it reenters on the right side
        if self.pos.x < 0:
            self.pos.x = config.SCREEN_X
        #If ship goes out of bounds to the right, it reenters on the left side
        elif self.pos.x > config.SCREEN_X:
            self.pos.x = 0
        #If ship goes out of bounds from the top of the screen, it reenters from the bottom
        if self.pos.y < 0:
            self.pos.y = config.SCREEN_Y
        #If the ship goes out of bounds from the bottom, it reenters from the top
        elif self.pos.y > config.SCREEN_Y:
            self.pos.y = 0