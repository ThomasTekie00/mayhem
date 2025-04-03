import gameobject
import config
import pygame
import math
import random

vector = pygame.math.Vector2





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
        self.thrust = config.thrust
        self.friction = config.friction
      

        """
        Health system:
        - Function for health
        - Max health variable
        - Current health variable
        - Health ratio
        """
        self.current_health = config.current_health
        self.max_health = config.max_health
        self.health_bar_length = config.health_bar_length
        self.health_ratio = config.health_ratio

        #Fuel system: 
        self.current_fuel = config.current_fuel
        self.max_fuel = config.max_fuel
        self.fuel_bar_length = config.fuel_bar_length
        self.fuel_ratio = config.fuel_ratio

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
        #Updates the pos based on the travel
        self.pos += self.vel


    def space_update(self):
        self.vel += config.gravity

        self.vel *= config.friction



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