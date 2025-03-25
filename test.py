import pygame
import random


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


#Skip 1
skip1 = pygame.image.load(p1_img).convert_alpha()
skip1 = pygame.transform.scale(skip1, (60,50))
skip1 = pygame.transform.flip(skip1, True, False)
skip1_rect = skip1.get_rect(center = (500,700))
skip1_speed = 5


#Skip 2
skip2 = pygame.image.load(p2_img).convert_alpha()
skip2 = pygame.transform.scale(skip2, (60,50))
skip2 = pygame.transform.flip(skip2, True, False)
skip2_rect = skip2.get_rect(center = (500,700))
skip2_speed = 5


#Meteor 1
stein = pygame.image.load(rock_img)
stein = pygame.transform.scale(stein, (200,200))
stein_y_pos = 0

#Meteor 2
stein_2 = pygame.image.load(rock2_img)
stein_2 = pygame.transform.scale(stein_2, (200,200))



while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        skip2_rect.x -= skip2_speed
    if keys[pygame.K_d]:
        skip2_rect.x += skip2_speed
    if keys[pygame.K_w]:
        skip2_rect.y -= skip2_speed
    if keys[pygame.K_s]:
        skip2_rect.y += skip2_speed
    
    if skip2_rect.left < 0:
        skip2_rect.left = 0
    if skip2_rect.right > SCREEN_X:
        skip2_rect.right = SCREEN_X
    if skip2_rect.top < 0:
        skip2_rect.top = 0
    if skip2_rect.bottom > SCREEN_Y:
        skip2_rect.bottom = SCREEN_Y
    
    
    if keys[pygame.K_LEFT]:
        skip1_rect.x -= skip1_speed
    if keys[pygame.K_RIGHT]:
        skip1_rect.x += skip1_speed
    if keys[pygame.K_UP]:
        skip1_rect.y -= skip1_speed
    if keys[pygame.K_DOWN]:
        skip1_rect.y += skip1_speed
    
    if skip1_rect.left < 0:
        skip1_rect.left = 0
    if skip1_rect.right > SCREEN_X:
        skip1_rect.right = SCREEN_X
    if skip1_rect.top < 0:
        skip1_rect.top = 0
    if skip1_rect.bottom > SCREEN_Y:
        skip1_rect.bottom = SCREEN_Y


    screen.blit(background, (0,0))
    #pygame.draw.rect(screen, background_color , (0,1000, SCREEN_X, SCREEN_Y / 2))
    screen.blit(skip1, skip1_rect)
    screen.blit(skip2, skip2_rect)
    screen.blit(stein, (350, stein_y_pos))
    stein_y_pos += 4
    if stein_y_pos < -1100:
        stein_y_pos = -10
    screen.blit(stein_2, (100, 500))
    screen.blit(text_surface, (800, 100))

    pygame.display.flip()
    clock.tick(60)
    

pygame.quit()


