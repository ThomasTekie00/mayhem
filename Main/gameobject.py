import pygame
import random
import math
import config

vector = pygame.math.Vector2



class PickUps(pygame.sprite.Sprite):
    """
    Blueprint class for all the pickup items in the game

    Defines the common behaviour for the health packs and fuel packs
    """
    def __init__(self, image, pos):
        """
        Args:
        - image = Display the image
        - pos = (x,y) coords with the help of vector
        """
        super().__init__()
        self.image = image 
        self.rect = self.image.get_rect(center = pos)
        self.pos = vector(pos)

        

    def update(self):
        """Update the pickups posistion for each frame"""
        self.rect.center = self.pos

    #Spawn test
    def respawn(self, SCREEN_X, SCREEN_Y):
        """
        Moves the pickups to a new random posistion

        Args:
        - screen_x: Screen width
        - screen_y: screen height

        Returns: the new location for the pickups as (x,y)
        """
        new_pos = (random.randint(100, SCREEN_X - 100), random.randint(100, SCREEN_Y - 100))
        self.pos = new_pos
        self.rect.center = self.pos
        return self.pos

    #Branch test

class Fuel(PickUps):
    """Fuel pickup that gives the ship fuel when picked up"""
    def __init__(self, image, pos):
        """
        Args:
        - Image: To display our image
        - Pos: (x,y) posistion
        """
        super().__init__(image, pos)

        
        




class Health(PickUps):
    def __init__(self, image, pos):
        super().__init__(image,pos)
    
   


class RockShower(pygame.sprite.Sprite):
    """
    Class for the obstacles:

    Rock shower falling from the x-axis with varying speed 
    """
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        
        #Gives us the random X spawn posistions
        spawn_x = random.randint(100,900)
        spawn_y = random.randint(-300, -50)
        self.pos = vector(spawn_x, spawn_y)

        
        #Gives us the random downwards speed
        speed_y = random.uniform(1,2)
        self.vel = vector(0, speed_y)
        self.rect.center = self.pos

    def update(self):
        """
        Method:
        - Updates the posistion based on the velocity
        - Rocks reset when they go out of bounds
        """
        self.pos += self.vel
        self.rect.center = self.pos

        #Restarts from the bottom of the screen to the top with a random pos
        if self.rect.top > 600:
            self.pos.x = random.randint(50, 900)
            self.pos.y = random.randint(-200, -50)

            
    


class Bullet(pygame.sprite.Sprite):
    """
    Class for bullets:

    Bullets fired from the ships, destroys rocks and damages ships

    Attributes:
    - White square surface: Bullets
    - Posistion using vectors
    - Direction based on firing angle
    - Constant speed that can be adjusted

    """
    def __init__(self, pos, angle):
        """
        Args:
        - Pos: Starting posistion for the bullets
        - angle: direction angle in degrees -> Similar to the blueprint of ships
        
        """
        super().__init__()
        self.original_image = pygame.Surface((5,5))
        self.original_image.fill("White")
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect(center=pos)
        self.direction = vector(0,0)
        self.pos = vector(pos)
        self.angle = angle
        self.speed = 10
        
        
        self.direction.x = -math.sin(math.radians(self.angle))
        self.direction.y = -math.cos(math.radians(self.angle))

    def update(self):
        """
        Method:
        - Updates posistion based on the direction and speed
        """
        self.pos += self.direction * self.speed
        
    
        self.rect.center = self.pos

        #Makes sure the bullets dont get tracked when they are beyond screen limits
        if self.pos.x < 0 or self.pos.x > config.SCREEN_X or self.pos.y < 0 or self.pos.y > config.SCREEN_Y:
            self.kill()
            
        
        
        

        

