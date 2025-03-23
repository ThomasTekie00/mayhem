import pygame


pygame.init

run = True

SCREEN_X = 1200 
SCREEN_Y = int(SCREEN_X * 0.8)

screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
pygame.display.set_caption("Mayhem")
background_color = (0,0,0)


#Filbane
p1_img = "p1.png"
p2_img = "p2.png"
rect_p1 = p1_img.get_rect()
rect_p2 = p2_img.get_rect()
rect.center = ()



while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()


