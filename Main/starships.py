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

"""
    #Blueprint implements everything that our player ships will share, movement physic, health, fuel and screen bounds.
    - Through polymorphism, these subclasses(Player1 and Player 2) can customize behaviour while still keeping the main traits that
    both subclasses inherit from our blueprint

    #Attributes:
    - Image: Ships image
    - Original image: Ships image before rotation
    - rect: Our box around the ships, needed for collision checks
    - velocity: Set with vector
    - posistion: Set with vector
    - Direction: Direction the ship is facing(Upwards by fault)
    - Angle: Current rotation angle in degrees
    - Thrust power
    - Friction: A way to control maxspeed
"""





class Blueprint(pygame.sprite.Sprite):
    def __init__(self, image, pos, vel):
        """
        Args:
         - Image: The image that will represent each player
         - pos: Starting posistion with x and y
         - vel: Starting velocity with x and y
        """
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
        """
        Updates the ship for the current frame
        1. Rotates the ship
        2. Updates posistion based on gravity and movement
        3. Screen bounds
        4. Updates the direction vector

        """
        
        #Update image while keeping the pos center
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.pos)

        self.space_update()
        self.screen_bounds()
        self.direction_turn()

    def space_update(self):
        """
        Applies gravity to pull the ship downward
        Applies friction to limit the speed
        Updates the ships pos based on the velocity
        """
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
        """
        Updates the ships direction vector based on the angle
        Converts angle to 0-360 degrees and calculates the direction vector with trigonometry
        - This is used for movement and shootin

        Returns None
        """
        self.angle %= 360

        #Updates the direction based on the angle of the ship
        #Always take the minus angle while traveling
        self.direction.x = -math.sin(math.radians(self.angle))
        self.direction.y = -math.cos(math.radians(self.angle))

    def get_health(self, amount):
        """
        Method:
        Increases health by a spesified amount

        Args: 
        - Amount: Health to add

        returns None
        """
        if self.current_health < self.max_health:
            self.current_health += amount
        if self.current_health >= self.max_health:
            self.current_health = self.max_health
    
    def lose_health(self, amount):
        """
        Method:
        Removes health by a spesified amount: Within collisions

        Args: 
        - Amount: Health to lose

        returns None

        """
        if self.current_health > 0:
            self.current_health -= amount
        if self.current_health < 0:
            self.current_health = 0
    
    def get_fuel(self, amount):
        """
        Method:
        Increases fuel by a spesified amount

        Args: 
        - Amount: Fuel to refill

        returns None
        """

        if self.current_fuel < self.max_fuel:
            self.current_fuel += amount
        if self.current_fuel >= self.max_fuel:
            self.current_fuel = self.max_fuel
    
    def lose_fuel(self, amount):
        """
        Method:
        Decreases fuel by a spesified amount

        Args:
        - Amunt: Fuel to lose within thrusting #Kanskje med kollisjon også?

        Returns None
        """
        if self.current_fuel > 0:
            self.current_fuel -= amount
        if self.current_fuel < 0:
            self.current_fuel = 0
    



class Player1(Blueprint):
    def __init__(self, image, pos=None, vel =(0,0)):
        """
        Player 1 spaceship class

        Controlled with WASD keys for movement and SPACE for shooting.

        Attributes:
        - bullet_spawn: Cooldown timer for shooting
        - Bullet_delay: MAX cooldown between shots
        """
     
        super().__init__(image, pos, vel)

        self.bullet_spawn = 0
        self.bullet_delay = 15
    

    def update(self):
        """
        Method:
        Updates player 1 ship
        Updates the shooting with a cooldown
        Updates movement with the move method
        Calls update from the parent class for the basics
        """

        if self.bullet_spawn > 0:
            self.bullet_spawn -= 1

        self.move()
        super().update()



    def move(self):
        """
        Method:
        Handles player 1 movement input

        Keyboard inputs for thrust, shooting and rotation
        """


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

        """
        Method: 

        Fires a bullet from player 1

        Creates a new bullet from the ships posistion and adds it to the bullet group for tracking

        Return None
        """


        bullet = Bullet(self.pos, self.angle)
        bullets_group.add(bullet)



    def basic_health(self):
        """
        Method:
        Visual representation of the health bar and fuel bar thats on the top left corner

        - With a white border around

        Returns None
        """
        pygame.draw.rect(config.screen, "red", (10,10, self.current_health / self.health_ratio, 25))
        pygame.draw.rect(config.screen, "white", (10, 10, self.health_bar_length, 25), 5)
    
    def basic_fuel(self):
        pygame.draw.rect(config.screen, "green", (10, 50, self.current_fuel / self.fuel_ratio, 25))
        pygame.draw.rect(config.screen, "white", (10, 50, self.fuel_bar_length, 25), 5)
    

class Player2(Blueprint):
    def __init__(self, image, pos=None, vel =(0,0)):
        """
        Player 2 spaceship class

        Controlled with WASD keys for movement and SPACE for shooting.

        Attributes:
        - bullet_spawn: Cooldown timer for shooting
        - Bullet_delay: MAX cooldown between shots
        """
        super().__init__(image, pos, vel)
        self.bullet_spawn = 0
        self.bullet_delay = 15
    

    def update(self):
        """
        Method:

        Updates player 2 ship
        Updates the shooting with a cooldown
        Updates movement with the move method
        Calls update from the parent class for the basics
        
        """
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
        """
        Fires a bullet from player 2 ship

        Creates a new bullet at player 2 ships posistion and adds it to player 2s bullet group

        Returns None
        """
        bullet = Bullet(self.pos, self.angle)
        bullets_group_2.add(bullet)