import pygame
import config
from gameobject import RockShower
from gameobject import Health
from gameobject import Fuel
from starships import Player1
from starships import Player2
from starships import Blueprint
from starships import bullets_group
from starships import bullets_group_2
import random
import time

vector = pygame.math.Vector2


pygame.init()
#run = True
font = pygame.font.Font("bilder/font.otf", 50)
clock = pygame.time.Clock()





all_sprites = pygame.sprite.Group()
rock_group = pygame.sprite.Group()
heal_group = pygame.sprite.Group()
fuel_group = pygame.sprite.Group()



for i in range(3):
    rock = RockShower(config.rock)
    all_sprites.add(rock)
    rock_group.add(rock)







#Ship draws
"""
Random pos for both of the ships
"""

random_pos1 = (random.randint(50, config.SCREEN_X - 50), random.randint(50, config.SCREEN_Y - 50))
random_pos2 = (random.randint(50, config.SCREEN_X - 50), random.randint(50, config.SCREEN_Y - 50))
ship = Player1(config.p1, random_pos1)
ship2 = Player2(config.p2, random_pos2)

all_sprites.add(ship)
all_sprites.add(ship2)



heal_pos = ((random.randint(200, config.SCREEN_X - 50), random.randint(200, config.SCREEN_Y - 50)))
heal_ob = Health(config.heals, heal_pos)
heal_group.add(heal_ob)
all_sprites.add(heal_ob)


fuel_pos = ((random.randint(200, config.SCREEN_X - 50), random.randint(200, config.SCREEN_Y - 50)))
fuel_ob = Health(config.fuels, fuel_pos)
fuel_group.add(fuel_ob)
all_sprites.add(fuel_ob)



def loop():
    run = True
    player1_score = 0
    player2_score = 0
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False




        shots = pygame.sprite.groupcollide(bullets_group, rock_group, True, True)
        if shots:
            for bullet, rocks in shots.items():
                for rock in rocks:
                    if ship:
                        player1_score += 1
                    
                
            
                    new_rock = RockShower(config.rock)
                    all_sprites.add(new_rock) 
                    rock_group.add(new_rock)
        
        shots = pygame.sprite.groupcollide(bullets_group_2, rock_group, True, True)
        if shots:
            for bullet, rocks in shots.items():
                for rock in rocks:
                    if ship2:
                        player2_score += 1
                    
                
            
                    new_rock = RockShower(config.rock)
                    all_sprites.add(new_rock) 
                    rock_group.add(new_rock)




        fuel_collide = pygame.sprite.spritecollide(ship, fuel_group, True)
        if fuel_collide:
            ship.get_fuel(200)

            new_fuel_pos = (random.randint(100, config.SCREEN_X - 100), random.randint(100, config.SCREEN_Y - 100))
            new_fuel = Fuel(config.fuels, new_fuel_pos)
            fuel_group.add(new_fuel)
            all_sprites.add(new_fuel)

        fuel_collide = pygame.sprite.spritecollide(ship2, fuel_group, True)
        if fuel_collide:
            ship2.get_fuel(200)

            new_fuel_pos = (random.randint(100, config.SCREEN_X - 100), random.randint(100, config.SCREEN_Y - 100))
            new_fuel = Fuel(config.fuels, new_fuel_pos)
            fuel_group.add(new_fuel)
            all_sprites.add(new_fuel)



        heal_collide = pygame.sprite.spritecollide(ship, heal_group, True)
        if fuel_collide:
            ship.get_health(200)

            new_heal_pos = (random.randint(100, config.SCREEN_X - 100), random.randint(100, config.SCREEN_Y - 100))
            new_heal = Health(config.heals, new_heal_pos)
            heal_group.add(new_heal)
            all_sprites.add(new_heal)

        heal_collide = pygame.sprite.spritecollide(ship2, heal_group, True)
        if fuel_collide:
            ship2.get_health(200)

            new_heal_pos = (random.randint(100, config.SCREEN_X - 100), random.randint(100, config.SCREEN_Y - 100))
            new_heal = Health(config.heals, new_heal_pos)
            heal_group.add(new_heal)
            all_sprites.add(new_heal)



      

        if ship.current_health <= 0:
            player2_score += 1
            new_pos = (random.randint(50, config.SCREEN_X - 50), random.randint(50, config.SCREEN_Y - 50))
            ship.pos = new_pos
            ship.vel = vector(0,0)
            ship.current_health = config.current_health
            ship.current_fuel = config.current_fuel
            

        if ship2.current_health <= 0:
            player1_score += 1
            new_pos = (random.randint(50, config.SCREEN_X - 50), random.randint(50, config.SCREEN_Y - 50))
            ship.pos = new_pos
            ship.vel = vector(0,0)
            ship2.current_health = config.current_health
            ship2.current_fuel = config.current_fuel

        crash = pygame.sprite.spritecollide(ship, rock_group, False)
        if crash:
            for rock in crash:
                ship.lose_health(10)
                player1_score -= 1
                rock.kill()
            
                new_rock = RockShower(config.rock)
                all_sprites.add(new_rock) 
                rock_group.add(new_rock)

        all_sprites.update()
        bullets_group.update()
        bullets_group_2.update()
            

        crash = pygame.sprite.spritecollide(ship2, rock_group, False)
        if crash:
            for rock in crash:
                ship2.lose_health(5)
                player2_score -= 1
                rock.kill()


                new_rock = RockShower(config.rock)
                all_sprites.add(new_rock)
                rock_group.add(new_rock)
        
        
        if pygame.sprite.collide_rect(ship, ship2) or pygame.sprite.collide_rect(ship2, ship):
            ship.lose_health(10)
            ship2.lose_health(10)
        

        



        config.screen.blit(config.background, (0,0))
        all_sprites.draw(config.screen)
        bullets_group.draw(config.screen)
        bullets_group_2.draw(config.screen)
        ship.basic_fuel()
        ship.basic_health()
        if player1_score > 3:
            config.screen.blit(config.screen, (0,0))
        ship2.basic_fuel()
        ship2.basic_health()
        score_text1 = config.font.render(f"Score: {player1_score}", True, (255,255,255))
        config.screen.blit(score_text1, (10,80))
        score_text2 = config.font.render(f"Score: {player2_score}", True, (255,255,255))
        config.screen.blit(score_text2, (890,80))
       
    
     

        pygame.display.flip()
        clock.tick(60)







if __name__ == "__main__":
    loop()
    pygame.quit()