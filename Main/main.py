import pygame
import config
#import gameobject
#import starships
#import random


pygame.init()
#run = True
font = pygame.font.Font("bilder/font.otf", 50)
clock = pygame.time.Clock()






def loop():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        config.screen.blit(config.background, (0,0))
       
    
     

        pygame.display.flip()
        clock.tick(60)







if __name__ == "__main__":
    loop()
    pygame.quit()