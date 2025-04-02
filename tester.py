import pygame
import random
import math


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

#Skip 1
skip1 = pygame.image.load(p1_img).convert_alpha()
skip1 = pygame.transform.scale(skip1, (30,25))
skip1 = pygame.transform.flip(skip1, True, False)








    

class Starship(pygame.sprite.Sprite):
    def __init__(self, vel):
        super().__init__()
        self.image = skip1
        self.w = self.image.get_width()
        self.h = self.image.get_height()
        self.x = SCREEN_X // 2
        self.y = SCREEN_Y // 2
        self.angle = 0
        self.vel = vector(vel)
        self.rotatedSurf = pygame.transform.rotate(self.image, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w // 2, self.y - self.sine * self.h//2)
       
    
    def draw(self, win):
        win.blit(self.rotatedSurf, self.rotatedRect)

    def turnLeft(self):
        self.angle += 5
        self.rotatedSurf = pygame.transform.rotate(self.image, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine + self.w // 2, self.y - self.sine * self.h // 2)
    
    def turnRight(self):
        self.angle -= 5
        self.rotatedSurf = pygame.transform.rotate(self.image, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine + self.w // 2, self.y - self.sine * self.h // 2)
    
    def MoveForward(self):
        self.x += self.cosine * 6
        self.y -= self.sine * 6
        self.rotatedSurf = pygame.transform.rotate(self.image, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine + self.w // 2, self.y - self.sine * self.h // 2)
        self.vel += vector(self.cosine * 0.2, -self.sine * 0.2)
    
    def space_update(self):
    # Dempning
        self.vel *= 0.85
        
        # Konstant nedtrekk på y aksen
        self.vel += vector(0,0.1)
        
        # Apply velocity to position
        self.x += self.vel.x
        self.y += self.vel.y
        
        # Update the rotated surface and rectangle
        self.rotatedSurf = pygame.transform.rotate(self.image, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)


    def Flyzone(self):
        #Skipet går ut på venstre, kommer inn på høyre side(Siden x,y aksen starter på top venstre)
        if self.x < 0:
            self.x = SCREEN_X
        elif self.x > SCREEN_X:
            self.x = 0
        if self.y < 0:
            self.y = SCREEN_Y
        elif self.y > SCREEN_Y:
            self.y = 0






gameover = False



def redrawWindow():
    screen.blit(background, (0,0))
    player.draw(screen)

    pygame.display.update()


player = Starship((0,0))

run = True

while run:
    clock.tick(60)
    if not gameover:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            player.turnLeft()
        if keys[pygame.K_RIGHT]:
            player.turnRight()
        if keys[pygame.K_UP]:
            player.MoveForward()

        player.Flyzone()
        player.space_update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    redrawWindow()

pygame.quit()
