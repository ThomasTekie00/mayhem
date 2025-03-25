import pygame
import config


class Player(pygame.sprite.Sprite):
    pass



p1_img = "bilder/p1.png"
p2_img = "bilder/p2.png"
# Blir ikke samme class som player
class Spaceship(pygame.sprite.Sprite):

    def __init__(self):
        image = pygame.image.load(p1_img).convert_alpha()
        self.image = pygame.transform.scale(image, (42, 30))

    def fire(sefl) :
        pass

    def update(self):
        pass
