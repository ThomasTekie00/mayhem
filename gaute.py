import pygame
import random
import math

pygame.init()
run = True
SCREEN_X = 1920
SCREEN_Y = 1080
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

#Bakgrunnen
background = pygame.image.load(bk_img)
background = pygame.transform.scale(background,(SCREEN_X, SCREEN_Y))
background = background.convert()
#Får fargen til bunnen av skjermen slik at jeg kan bruke det som en platform
background_color = background.get_at((SCREEN_X // 2, 1000))



# Skip-klasser med thrust og rotasjon
class Ship:
    def __init__(self, image_path, position):
        self.original_img = pygame.image.load(image_path).convert_alpha()
        self.original_img = pygame.transform.scale(self.original_img, (60, 50))
        self.image = self.original_img
        self.rect = self.image.get_rect(center=position)
        self.angle = 0
        self.speed = pygame.math.Vector2(0, 0)
        self.thrust = 0.2
        self.max_speed = 5

    def rotate(self, direction):
        self.angle += direction
        self.angle %= 360
        self.image = pygame.transform.rotate(self.original_img, -self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def apply_thrust(self):
        rad = math.radians(self.angle)
        force = pygame.math.Vector2(math.cos(rad), -math.sin(rad)) * self.thrust
        self.speed += force
        # Begrens farten
        if self.speed.length() > self.max_speed:
            self.speed.scale_to_length(self.max_speed)

    def update(self):
        self.rect.centerx += self.speed.x
        self.rect.centery += self.speed.y

        # Hold skipet på skjermen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_X:
            self.rect.right = SCREEN_X
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_Y:
            self.rect.bottom = SCREEN_Y

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# Skip-instansene
player1 = Ship(p1_img, (400, 700))
player2 = Ship(p2_img, (1500, 700))

# Meteorer
stein = pygame.image.load(rock_img)
stein = pygame.transform.scale(stein, (200, 200))
stein_y_pos = 0

stein_2 = pygame.image.load(rock2_img)
stein_2 = pygame.transform.scale(stein_2, (200, 200))




# Skip-instansene
player1 = Ship(p1_img, (400, 700))
player2 = Ship(p2_img, (1500, 700))

# Meteorer
stein = pygame.image.load(rock_img)
stein = pygame.transform.scale(stein, (200, 200))
stein_y_pos = 0

stein_2 = pygame.image.load(rock2_img)
stein_2 = pygame.transform.scale(stein_2, (200, 200))



while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    # Player 1 (WASD + SPACE)
    if keys[pygame.K_a]:
        player1.rotate(5)
    if keys[pygame.K_d]:
        player1.rotate(-5)
    if keys[pygame.K_w]:
        player1.apply_thrust()

    # Player 2 (Arrows + Right Shift)
    if keys[pygame.K_LEFT]:
        player2.rotate(5)
    if keys[pygame.K_RIGHT]:
        player2.rotate(-5)
    if keys[pygame.K_UP]:
        player2.apply_thrust()

    # Oppdater spillobjekter
    player1.update()
    player2.update()
    stein_y_pos += 4
    if stein_y_pos > SCREEN_Y:
        stein_y_pos = -200

    # Tegn alt
    screen.blit(background, (0, 0))
    player1.draw(screen)
    player2.draw(screen)
    screen.blit(stein, (350, stein_y_pos))
    screen.blit(stein_2, (100, 500))
    screen.blit(text_surface, (800, 100))

    pygame.display.flip()
    clock.tick(60)

    

pygame.quit()