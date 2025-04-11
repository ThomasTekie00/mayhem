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
import cProfile

vector = pygame.math.Vector2


pygame.init()

#run = True
font = pygame.font.Font("bilder/font.otf", 50)
clock = pygame.time.Clock()





all_sprites = pygame.sprite.Group()
rock_group = pygame.sprite.Group()
heal_group = pygame.sprite.Group()
fuel_group = pygame.sprite.Group()




#Rock shower
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

def screen():
    overlay = pygame.Surface((config.SCREEN_X, config.SCREEN_Y))
    overlay.fill("black")
    config.screen.blit(overlay, (0,0))

def show_game_over(winner):
    overlay = pygame.Surface((config.SCREEN_X, config.SCREEN_Y))
    overlay.fill("black")
    config.screen.blit(overlay, (0,0))

    if winner == 1:
        text = config.font_result.render("Player 1 wins!", True, "Red")
    else:
        text = config.font_result.render("Player 2 wins!", True, "Red")

    
    config.screen.blit(text, (270, 200))

    restart_text = config.font_restart.render("Press Y to play again!", True, "White")
    #restart_rect = restart_text.get_rect(center=(config.SCREEN_X // 2 + 50, config.SCREEN_Y // 2 + 50))
    config.screen.blit(restart_text, (280,300))

    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    waiting = False
                    return True
    return True


def loop():
    run = True
    player1_score = 0
    player2_score = 0
    while run:
        #dt = clock.tick(60) * .001 * config.FPS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


####################################Bullet collision#############################################################################
        ################Bullets from player 1 collide with rock##################
        shots = pygame.sprite.groupcollide(bullets_group, rock_group, True, True)
        if shots:
            player1_score += 1

            new_rock = RockShower(config.rock)
            all_sprites.add(new_rock) 
            rock_group.add(new_rock)
            


        ################Bullets from player 2 collide with rock##################
        shots = pygame.sprite.groupcollide(bullets_group_2, rock_group, True, True)
        if shots:
            player2_score += 1


            new_rock = RockShower(config.rock)
            all_sprites.add(new_rock) 
            rock_group.add(new_rock)
        
                    
        
        #Bullets hitting ship 2
        hits_1 = pygame.sprite.spritecollide(ship2, bullets_group, True)
        if hits_1:
            ship2.current_health -= 350
            player1_score += 1
        #Bullets hitting ship 1
        hits_2 = pygame.sprite.spritecollide(ship, bullets_group_2, True)
        if hits_2:
            ship.current_health -= 350
            player2_score += 1

#############################Pickups collisjons########################################################################################

        ################Player 1 pickups fuel can########################
        fuel_collide = pygame.sprite.spritecollide(ship, fuel_group, True)
        if fuel_collide:
            ship.get_fuel(200)

            new_fuel_pos = (random.randint(100, config.SCREEN_X - 100), random.randint(100, config.SCREEN_Y - 100))
            new_fuel = Fuel(config.fuels, new_fuel_pos)
            fuel_group.add(new_fuel)
            all_sprites.add(new_fuel)

        #################Player 2 pickups fuel can########################
        fuel_collide = pygame.sprite.spritecollide(ship2, fuel_group, True)
        if fuel_collide:
            ship2.get_fuel(200)
        
            new_fuel_pos = (random.randint(100, config.SCREEN_X - 100), random.randint(100, config.SCREEN_Y - 100))
            new_fuel = Fuel(config.fuels, new_fuel_pos)
            fuel_group.add(new_fuel)
            all_sprites.add(new_fuel)


        ##################Player 1 pickups health pack###################
        heal_collide = pygame.sprite.spritecollide(ship, heal_group, True)
        if heal_collide:
            ship.get_health(200)

            new_heal_pos = (random.randint(100, config.SCREEN_X - 100), random.randint(100, config.SCREEN_Y - 100))
            new_heal = Health(config.heals, new_heal_pos)
            heal_group.add(new_heal)
            all_sprites.add(new_heal)

        ################Player 2 pickups health pack######################
        heal_collide = pygame.sprite.spritecollide(ship2, heal_group, True)
        if heal_collide:
            ship2.get_health(200)

            new_heal_pos = (random.randint(100, config.SCREEN_X - 100), random.randint(100, config.SCREEN_Y - 100))
            new_heal = Health(config.heals, new_heal_pos)
            heal_group.add(new_heal)
            all_sprites.add(new_heal)


######################################################################################################################################
        
##Player gameplay logic
      
        #Respawning when the players lose their health
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
            ship2.pos = new_pos
            ship2.vel = vector(0,0)
            ship2.current_health = config.current_health
            ship2.current_fuel = config.current_fuel


        #Collisjon between rock and player 1 + spawns in a new rock
        crash = pygame.sprite.spritecollide(ship, rock_group, False)
        if crash:
            for rock in crash:
                ship.lose_health(100)
                player1_score -= 1
                rock.kill()
            
                new_rock = RockShower(config.rock)
                all_sprites.add(new_rock) 
                rock_group.add(new_rock)

       
        #Collisjon between rock and player2 + Spawns in a new rock 
        crash = pygame.sprite.spritecollide(ship2, rock_group, False)
        if crash:
            for rock in crash:
                ship2.lose_health(100)
                player2_score -= 1
                rock.kill()


                new_rock = RockShower(config.rock)
                all_sprites.add(new_rock)
                rock_group.add(new_rock)
        
        
        #Collisjon between the two ships
        if pygame.sprite.collide_rect(ship, ship2) or pygame.sprite.collide_rect(ship2, ship):
            ship.lose_health(200)
            ship2.lose_health(200)
        


        #Scoring enough points to win and redraw screen with show_game_over
        if player1_score >= config.win_points:
            if show_game_over(1):
                player1_score= 0
                player2_score = 0
                new_pos_1 = ((200, config.SCREEN_Y / 2))
                new_pos_2 = ((850, config.SCREEN_Y / 2))

                #rock.kill()
                #bullet.kill()

                ship.vel = (0,0)
                ship.pos = new_pos_1
                ship.current_health = config.current_health
                ship.current_fuel = config.current_fuel

                ship2.vel = (0,0)
                ship2.pos = new_pos_2
                ship2.current_health = config.current_health
                ship2.current_fuel = config.current_fuel
            else:
                run = False
        
        if player2_score >= config.win_points:
            if show_game_over(2):
                player1_score = 0
                player2_score = 0
                new_pos_1 = ((200, config.SCREEN_Y / 2))
                new_pos_2 = ((850, config.SCREEN_Y / 2))


                ship2.vel = (0,0)
                ship2.pos = new_pos_2
                ship2.current_health = config.current_health
                ship2.current_fuel = config.current_fuel

        
                ship.vel = (0,0)
                ship.pos = new_pos_1
                ship.current_fuel = config.current_fuel
                ship.current_health = config.current_health
                
            else:
                run = False

        if ship.current_fuel == 0:
            if show_game_over(2):
                player1_score = 0
                player2_score = 0
                new_pos_1 = ((200, config.SCREEN_Y / 2))
                new_pos_2 = ((850, config.SCREEN_Y / 2))

                ship2.vel = (0,0)
                ship2.pos = new_pos_2
                ship2.current_health = config.current_health
                ship2.current_fuel = config.current_fuel

                
                ship.vel = (0,0)
                ship.pos = new_pos_1
                ship.current_fuel = config.current_fuel
                ship.current_health = config.current_health
            else:
                run = False

            
        if ship2.current_fuel == 0:
            if show_game_over(1):
                player1_score = 0
                player2_score = 0
                new_pos_1 = ((200, config.SCREEN_Y / 2))
                new_pos_2 = ((850, config.SCREEN_Y / 2))

                ship.vel = (0,0)
                ship.pos = new_pos_1
                ship.current_health = config.current_health
                ship.current_fuel = config.current_fuel

                ship2.vel = (0,0)
                ship2.pos = new_pos_2
                ship2.current_health = config.current_health
                ship2.current_fuel = config.current_fuel
            else:
                run = False
        
########################################################################################################################################




        all_sprites.update()
        bullets_group.update()
        bullets_group_2.update()


        config.screen.blit(config.background, (0,0))
        all_sprites.draw(config.screen)
        bullets_group.draw(config.screen)
        bullets_group_2.draw(config.screen)
        rock_group.draw(config.screen)
        ship.basic_fuel()
        ship.basic_health()
        ship2.basic_fuel()
        ship2.basic_health()
        score_text1 = config.font_score.render(f"Score: {player1_score}", True, (255,255,255))
        config.screen.blit(score_text1, (10,80))
        score_text2 = config.font_score.render(f"Score: {player2_score}", True, (255,255,255))
        config.screen.blit(score_text2, (890,80))
       
    
     

        pygame.display.flip()
        clock.tick(60)







if __name__ == "__main__":
    loop()
    pygame.quit()