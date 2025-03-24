import pygame


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
bk_img = "bilder/space.png"
bakke_img = "bilder/bak1.png"
p1_img = "p1.png"
p2_img = "p2.png"

#Bakgrunnen
background = pygame.image.load(bk_img)
background = pygame.transform.scale(background,(SCREEN_X, SCREEN_Y))
background = background.convert()
#Får fargen til bunnen av skjermen slik at jeg kan bruke det som en platform
background_color = background.get_at((SCREEN_X // 2, 1000))







while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    screen.blit(background, (0,0))
    pygame.draw.rect(screen, background_color , (0,1000, SCREEN_X, SCREEN_Y / 2))
    screen.blit(text_surface, (800, 100))

    pygame.display.flip()
    clock.tick(60)
    

pygame.quit()


