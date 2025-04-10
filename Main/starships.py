import gameobject
import config
import pygame
import math
import random
from gameobject import Bullet



vector = pygame.math.Vector2

pygame.init()

bullets_group = pygame.sprite.Group()
bullets_group_2 = pygame.sprite.Group()

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

    def acceleration(self):
        """
        Method for player speed in the direction they are facing:
        Acceleration
        - Self.direction = Defines the direction the object will accelerate in
        - Self.thrust = Controls the speed of the acceleration
        Which puts the effect into how the object moves
        - Self.vel
        """
        self.vel += self.direction * self.thrust

    def update(self):
        
        #Update image while keeping the pos center
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.pos)

        self.space_update()
        self.screen_bounds()
        self.direction_turn()

    def space_update(self):
        #Gravity pull with a vector, where 0 is our x and -1 value gives a drag downwards
        self.vel += config.gravity

        #Friction so the speed is limited
        self.vel *= config.friction

        #Updates the pos based on the travel
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

    def direction_turn(self):
        self.angle %= 360

        #Updates the direction based on the angle of the ship
        #Always take the minus angle while traveling
        self.direction.x = -math.sin(math.radians(self.angle))
        self.direction.y = -math.cos(math.radians(self.angle))

    def get_health(self, amount):
        if self.current_health < self.max_health:
            self.current_health += amount
        if self.current_health >= self.max_health:
            self.current_health = self.max_health
    
    def lose_health(self, amount):
        if self.current_health > 0:
            self.current_health -= amount
        if self.current_health < 0:
            self.current_health = 0
    
    def get_fuel(self, amount):
        if self.current_fuel < self.max_fuel:
            self.current_fuel += amount
        if self.current_fuel >= self.max_fuel:
            self.current_fuel = self.max_fuel
    
    def lose_fuel(self, amount):
        if self.current_fuel > 0:
            self.current_fuel -= amount
        if self.current_fuel < 0:
            self.current_fuel = 0
    
  






class Player1(Blueprint):
    def __init__(self, image, pos=None, vel =(0,0)):
        super().__init__(image, pos, vel)

        self.bullet_spawn = 0
        self.bullet_delay = 15
    

    def update(self):

        if self.bullet_spawn > 0:
            self.bullet_spawn -= 1

        self.move()
        super().update()



    def move(self):


        key = pygame.key.get_pressed()

        if key[pygame.K_a]:
            self.angle += 5
        
        if key[pygame.K_d]:
            self.angle += -5
        
        if key[pygame.K_w] and self.current_fuel > 0:
            self.acceleration()
            self.lose_fuel(1)

        if key[pygame.K_SPACE] and self.bullet_spawn <= 0:
            self.shoot()
            self.bullet_spawn = self.bullet_delay
    

    def shoot(self):
        bullet = Bullet(self.pos, self.angle)
        bullets_group.add(bullet)



    def basic_health(self):
        pygame.draw.rect(config.screen, "red", (10,10, self.current_health / self.health_ratio, 25))
        pygame.draw.rect(config.screen, "white", (10, 10, self.health_bar_length, 25), 5)
    
    def basic_fuel(self):
        pygame.draw.rect(config.screen, "green", (10, 50, self.current_fuel / self.fuel_ratio, 25))
        pygame.draw.rect(config.screen, "white", (10, 50, self.fuel_bar_length, 25), 5)
    

class Player2(Blueprint):
    def __init__(self, image, pos=None, vel =(0,0)):
        super().__init__(image, pos, vel)
        self.bullet_spawn = 0
        self.bullet_delay = 15
    

    def update(self):
        if self.bullet_spawn > 0:
            self.bullet_spawn -= 1

        self.move()
        super().update()


    def move(self):


        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT]:
            self.angle += 5
        
        if key[pygame.K_RIGHT]:
            self.angle += -5
        
        if key[pygame.K_UP] and self.current_fuel > 0:
            self.acceleration()
            self.lose_fuel(1)
        if key[pygame.K_RSHIFT] and self.bullet_spawn <= 0:
            self.shoot()
            self.bullet_spawn = self.bullet_delay
    
    def basic_health(self):
        pygame.draw.rect(config.screen, "red", (790, 10, self.current_health / self.health_ratio, 25))
        pygame.draw.rect(config.screen, "white", (790, 10, self.health_bar_length, 25), 5)
    
    def basic_fuel(self):
        pygame.draw.rect(config.screen, "green", (790, 50, self.current_fuel / self.fuel_ratio, 25))
        pygame.draw.rect(config.screen, "white", (790, 50, self.fuel_bar_length, 25), 5)

        
    def shoot(self):
        bullet = Bullet(self.pos, self.angle)
        bullets_group_2.add(bullet)