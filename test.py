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

#Skip 2
skip2 = pygame.image.load(p2_img).convert_alpha()
skip2 = pygame.transform.scale(skip2, (60,50))
skip2 = pygame.transform.flip(skip2, True, False)


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


    screen.blit(background, (0,0))
    #pygame.draw.rect(screen, background_color , (0,1000, SCREEN_X, SCREEN_Y / 2))
    screen.blit(skip1, (500,500))
    screen.blit(skip2, (700, 500))
    screen.blit(stein, (350, stein_y_pos))
    stein_y_pos += 4
    if stein_y_pos < -1100:
        stein_y_pos = -10
    screen.blit(stein_2, (100, 500))
    screen.blit(text_surface, (800, 100))

    pygame.display.flip()
    clock.tick(60)
    

pygame.quit()


