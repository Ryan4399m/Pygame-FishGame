import pygame
import sys
import random
from pygame import mixer
pygame.init()
pygame.font.init()
mixer.init()

def update_position(x, y, speed, direction):
    if direction == "right":
        x += speed
    elif direction == "left":
        x -= speed
    elif direction == "down":
        y += speed
    elif direction == "up":
        y -= speed
    return x, y

BROWN = (154, 58, 42)
PINK = (252, 76, 134)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

def main ():
    info = pygame.display.Info()
    SCREEN_WIDTH = info.current_w
    SCREEN_HEIGHT = info.current_h
    IMAGE_WIDTH = 5000
    IMAGE_HEIGHT = 2813
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    clock = pygame.time.Clock()

    # Sounds
    munchsound = pygame.mixer.Sound('Assets/bite.mp3')
    boingsound = pygame.mixer.Sound('Assets/boing (2).mp3')
    boingsound.set_volume(0.2)
    FART_SOUND = [pygame.mixer.Sound('Assets/fart-01.mp3'), pygame.mixer.Sound('Assets/fart-02.mp3'),
                pygame.mixer.Sound('Assets/fart-03.mp3'), pygame.mixer.Sound('Assets/fart-04.mp3'),
                pygame.mixer.Sound('Assets/fart-05.mp3'), ]
    enemyhit = pygame.mixer.Sound('Assets/enemyhit.wav')
    enemyhit.set_volume(0.4)
    enemykill = pygame.mixer.Sound('Assets/pop.mp3')
    levelup = pygame.mixer.Sound('Assets/level up.mp3')
    levelup.set_volume(0.2)
    laugh = pygame.mixer.Sound('Assets/laugh.mp3')

    
    background_images = [
        pygame.image.load("Assets/background (1).png").convert_alpha(),
        pygame.image.load("Assets/background (2).png").convert_alpha(),
        pygame.image.load("Assets/background (3).png").convert_alpha(),
        pygame.image.load("Assets/background (4).png").convert_alpha(),
        pygame.image.load("Assets/background (5).png").convert_alpha(),
        pygame.image.load("Assets/background (6).png").convert_alpha(),
        pygame.image.load("Assets/background (7).png").convert_alpha(),
        pygame.image.load("Assets/background (8).png").convert_alpha(),
    ]

    bg_x = [0] * len(background_images)
    bg_y = [0] * len(background_images)

    font = pygame.font.Font("Assets/font2.ttf", SCREEN_WIDTH//40)
    font2 = pygame.font.Font("Assets/font2.ttf", SCREEN_WIDTH//80)
    small_op = pygame.image.load("Assets/enemyup.png").convert_alpha()
    small_op = pygame.transform.scale(small_op, (SCREEN_WIDTH // 10, SCREEN_HEIGHT // 5.6))
    moving_op = pygame.image.load("Assets/op1.png").convert_alpha()
    moving_op = pygame.transform.scale(small_op, (SCREEN_WIDTH // 10, SCREEN_HEIGHT // 5.6))
    moving_op = pygame.transform.rotate(small_op, 270)
    moving_opl = pygame.image.load("Assets/op1.png").convert_alpha()
    moving_opl = pygame.transform.scale(small_op, (SCREEN_WIDTH // 10, SCREEN_HEIGHT // 5.6))
    moving_opl = pygame.transform.rotate(small_op, 90)
    moving_opd = pygame.image.load("Assets/op1.png").convert_alpha()
    moving_opd = pygame.transform.scale(small_op, (SCREEN_WIDTH // 10, SCREEN_HEIGHT // 5.6))
    moving_opd = pygame.transform.rotate(small_op, 180)
    moving_opu = pygame.image.load("Assets/op1.png").convert_alpha()
    moving_opu = pygame.transform.scale(small_op, (SCREEN_WIDTH // 10, SCREEN_HEIGHT // 5.6))
    final_op =pygame.image.load("Assets/op1.png").convert_alpha()
    final_op = pygame.transform.scale(small_op, (SCREEN_WIDTH // 10, SCREEN_HEIGHT // 5.6))
    chili_image = pygame.image.load("Assets/chili.png").convert_alpha()
    health_image = pygame.image.load("Assets/health.png").convert_alpha()
    health_image = pygame.transform.scale(health_image, (SCREEN_WIDTH // 20, SCREEN_HEIGHT // 11.2))
    player_image = pygame.image.load("Assets/player.png").convert_alpha()
    player_image = pygame.transform.scale(player_image, (SCREEN_WIDTH // 10, SCREEN_HEIGHT // 5.6))
    player_original = player_image
    player_hitbox = player_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    # random coords for the different objects
    chili_x = random.randint(200, 2700)
    chili_y = random.randint(200, 1500)
    op_x = random.randint(200, 2700)
    op_y = random.randint(200, 1500)
    health_x = random.randint(200, 2700)
    health_y = random.randint(200, 2700)
    op2_x= random.randint(200, 2700)
    op2_y= random.randint(200, 1500)
    op3_x= random.randint(200, 2700)
    op3_y= random.randint(200, 1500)
    op4_x= random.randint(200, 2700)
    op4_y= random.randint(200, 1500)
    op5_x= random.randint(200, 2700)
    op5_y= random.randint(200, 1500)
    f_x = -1000
    f_y = -500
    

    op2_speed = 20
    health_speed = 2
    op_speed = 2
    chili_speed = 2
    bg_speeds = [1, 2, 3, 4, 5, 6, 7, 12]
    player_speed = 2
    current_direction = None
    f1 = 2

    lives = 10
    
    score = 0
    totalscore = 0
    level = 0
    levelchange = False
    mixer.music.load('Assets/aquagrabber.mp3')
    mixer.music.set_volume(0.5)
    mixer.music.play(-1)

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_d:
                    current_direction = "right"
                    player_image = pygame.transform.rotate(player_original, 270)
                    player_hitbox = player_image.get_rect(center=player_hitbox.center)
                elif event.key == pygame.K_a:
                    current_direction = "left"
                    player_image = pygame.transform.rotate(player_original, 90)
                    player_hitbox = player_image.get_rect(center=player_hitbox.center)
                elif event.key == pygame.K_s:
                    current_direction = "down"
                    player_image = pygame.transform.rotate(player_original, 180)
                    player_hitbox = player_image.get_rect(center=player_hitbox.center)
                elif event.key == pygame.K_w:
                    current_direction = "up"
                    player_image = player_original
                    player_hitbox = player_image.get_rect(center=player_hitbox.center)
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                small_op_hitbox = small_op.get_rect(center=((op_x - bg_x[7]), (op_y - bg_y[7])))
                op2_rect = moving_op.get_rect(center=((op2_x - bg_x[7]), (op2_y - bg_y[7])))
                op3_rect = moving_opl.get_rect(center=((op3_x - bg_x[7]), (op3_y - bg_y[7])))
                op4_rect = moving_opd.get_rect(center=((op4_x - bg_x[7]), (op4_y - bg_y[7])))
                op5_rect = moving_opu.get_rect(center=((op5_x - bg_x[7]), (op5_y - bg_y[7])))
                f_rect = final_op.get_rect(center=((f_x - bg_x[7]), f_y - bg_y[7]))
                if small_op_hitbox.collidepoint(event.pos):
                    score += 1
                    totalscore += 1
                    op_x = random.randint(200, 2700)
                    op_y = random.randint(200, 1500)
                    enemykill.play()
                if op2_rect.collidepoint(event.pos):
                    score += 1
                    totalscore += 1
                    op2_x = 5000
                    op2_y = random.randint(-500, 2000)
                    enemykill.play()
                if op3_rect.collidepoint(event.pos):
                    score += 1
                    totalscore += 1
                    op3_x = -2000
                    op3_y = random.randint(-500, 2000)
                    enemykill.play()
                if op4_rect.collidepoint(event.pos):
                    score += 1
                    totalscore += 1
                    op4_x = random.randint(1000, 2000)
                    op4_y = -1000
                    enemykill.play()
                if op5_rect.collidepoint(event.pos):
                    score += 1
                    totalscore += 1
                    op5_x = random.randint(800, 2500)
                    op5_y = 2813
                    enemykill.play()
                if f_rect.collidepoint(event.pos):
                    if lives > 0:
                        lives -= 1
                    else:
                        screen.fill(BLACK)
                        for i in FART_SOUND:
                            i.play()
                        gameover_text = font.render("GAME OVER", 1, WHITE)
                        screen.blit(gameover_text, (SCREEN_WIDTH // 2 - gameover_text.get_width()/2, SCREEN_HEIGHT // 2 - gameover_text.get_height()))
                        highest_level_text = font.render("DIED AT LEVEL " + str(level), 1, WHITE)
                        screen.blit(highest_level_text, (SCREEN_WIDTH // 2 - highest_level_text.get_width()/2, SCREEN_HEIGHT // 2 - highest_level_text.get_height()/8))
                        totalscore = 0
                        pygame.display.update()
                        pygame.time.delay(3000)
                        break
                    f1 += 1
                    final_op = pygame.transform.scale(small_op, (SCREEN_WIDTH // 10*f1, SCREEN_HEIGHT // 5.6*f1))
                    f_x = random.randint(-1000, 4000)
                    f_y = random.randint(-500, 2000)
                    laugh.play()
                    
        for i in range(len(background_images)):
            bg_x[i], bg_y[i] = update_position(bg_x[i], bg_y[i], bg_speeds[i] * player_speed, current_direction)
        for i in range(len(background_images) - 1):
            screen.blit(background_images[i], ((SCREEN_WIDTH // 2 - IMAGE_WIDTH // 2) - bg_x[i],
                                            (SCREEN_HEIGHT // 2 - IMAGE_HEIGHT // 2) - bg_y[i]))
        # different blit for the last layer since it has diff dimensions than the rest
        screen.blit(background_images[7], ((SCREEN_WIDTH // 2 - 7500 // 2) - bg_x[i],
                                        (SCREEN_HEIGHT // 2 - 4816 // 2) - bg_y[i]))

        chili_x, chili_y = update_position(chili_x, chili_y, chili_speed, current_direction)
        #the objects need to move relative to the players direction so the bg_x and y is subtracted from its coords
        chili_rect = chili_image.get_rect(center=(chili_x - bg_x[7], chili_y - bg_y[7]))
        screen.blit(chili_image, chili_rect)

        op_x, op_y = update_position(op_x, op_y, op_speed, current_direction)
        op_rect = small_op.get_rect(center=(op_x - bg_x[7], op_y - bg_y[7]))
        screen.blit(small_op, op_rect)

        if score % 5 == 0:
            score = 0
            #adding a level change variable makes sure that it doesnt continously increase the level number if the if statment is true
            if not levelchange:
                level += 1 
                levelchange = True
                levelup.play()
        else:
            levelchange = False
            
        if  lives < 10:
            health_x, health_y = update_position(health_x, health_y, health_speed, current_direction)
            health_rect = health_image.get_rect(center=(health_x - bg_x[7], health_y - bg_y[7]))
            screen.blit(health_image, health_rect)
            if player_hitbox.colliderect(health_rect):
                lives += 1
                health_x = random.randint(200, 2700)
                health_y = random.randint(200, 1500)
                munchsound.play()
        
        if totalscore > 10:
           
            op2_x, op2_y = update_position(op2_x, op2_y, op2_speed, "left")
            op2_rect = moving_op.get_rect(center=(op2_x - bg_x[7], op2_y - bg_y[7]))
            screen.blit(moving_op, op2_rect)
            if player_hitbox.colliderect(op2_rect):
                lives -= 1
                op2_x = 5000
                op2_y = random.randint(-500, 2000)
                enemyhit.play()
            if op2_x < -2000:
                op2_x = 5000
                op2_y = random.randint(-500, 2000)
            
        if totalscore > 15:
            op2_speed = 25
            health_speed = 3
            op_speed = 3
            chili_speed = 3
            player_speed = 3
        
            op3_x, op3_y = update_position(op3_x, op3_y, op2_speed, "right")
            op3_rect = moving_opl.get_rect(center=(op3_x - bg_x[7], op3_y - bg_y[7]))
            screen.blit(moving_opl, op3_rect)
            if player_hitbox.colliderect(op3_rect):
                lives -= 1
                op3_x = -2000
                op3_y = random.randint(-500, 2000)
                enemyhit.play()
            if op3_x > 5000:
                op3_x = -2000
                op3_y = random.randint(-500, 2000)

        if totalscore > 20:
           
            op4_x, op4_y = update_position(op4_x, op4_y, op2_speed, "down")
            op4_rect = moving_opd.get_rect(center=(op4_x - bg_x[7], op4_y - bg_y[7]))
            screen.blit(moving_opd, op4_rect)
            if player_hitbox.colliderect(op4_rect):
                lives -= 1
                op4_x = random.randint(-1000, 4000)
                op4_y = -1000
                enemyhit.play()
            if op4_y > 2813:
                op4_x = random.randint(-1000, 4000)
                op4_y = -1000

        if totalscore > 25:
            op2_speed = 28
            health_speed = 4
            op_speed = 4
            chili_speed = 4
            player_speed = 4
        
            op5_x, op5_y = update_position(op5_x, op5_y, op2_speed, "up")
            op5_rect = moving_opu.get_rect(center=(op5_x - bg_x[7], op5_y - bg_y[7]))
            screen.blit(moving_opu, op5_rect)
            if player_hitbox.colliderect(op5_rect):
                lives -= 1
                op5_x = random.randint(-1000, 4000)
                op5_y = 2813
                enemyhit.play()
            if op5_y < -1000:
                op5_x = random.randint(-1000, 4000)
                op5_y = 2813

        if totalscore > 30:
            f_x, f_y = update_position(f_x, f_y, op2_speed, None)
            f_rect = final_op.get_rect(center=((f_x) - bg_x[7], (f_y) - bg_y[7]))
            screen.blit(final_op, f_rect)
            if player_hitbox.colliderect(f_rect):
                laugh.play()
                if lives > 0:
                    lives -= 1
                else:
                    screen.fill(BLACK)
                    for i in FART_SOUND:
                        i.play()
                    gameover_text = font.render("GAME OVER", 1, WHITE)
                    screen.blit(gameover_text, (SCREEN_WIDTH // 2 - gameover_text.get_width()/2, SCREEN_HEIGHT // 2 - gameover_text.get_height()))
                    highest_level_text = font.render("DIED AT LEVEL " + str(level), 1, WHITE)
                    screen.blit(highest_level_text, (SCREEN_WIDTH // 2 - highest_level_text.get_width()/2, SCREEN_HEIGHT // 2 - highest_level_text.get_height()/8))
                    totalscore = 0
                    pygame.display.update()
                    pygame.time.delay(3000)
                    break
                f1 += 1
                final_op = pygame.transform.scale(small_op, (SCREEN_WIDTH // 10*f1, SCREEN_HEIGHT // 5.6*f1))
                f_x = random.randint(-1000, 4000)
                f_y = random.randint(-500, 2000)
        

        if player_hitbox.colliderect(chili_rect):
            chili_x = random.randint(200, 2700)
            chili_y = random.randint(200, 1500)
            player_speed += 0.2
            munchsound.play()
        
        if player_hitbox.colliderect(op_rect):
            lives -= 1
            op_x = random.randint(200, 2700)
            op_y = random.randint(200, 1500)
            enemyhit.play()
        
            # gameover 
        if lives < 1 :
                screen.fill(BLACK)
                for i in FART_SOUND:
                    i.play()
                gameover_text = font.render("GAME OVER", 1, WHITE)
                screen.blit(gameover_text, (SCREEN_WIDTH // 2 - gameover_text.get_width()/2, SCREEN_HEIGHT // 2 - gameover_text.get_height()))
                highest_level_text = font.render("DIED AT LEVEL " + str(level), 1, WHITE)
                screen.blit(highest_level_text, (SCREEN_WIDTH // 2 - highest_level_text.get_width()/2, SCREEN_HEIGHT // 2 - highest_level_text.get_height()/8))
                totalscore = 0
                pygame.display.update()
                pygame.time.delay(3000)
                break
        #border restrictions
        if bg_x[0] > 330:

            current_direction = "left"
            player_image = pygame.transform.rotate(player_original, 90)
            player_hitbox = player_image.get_rect(center=player_hitbox.center)
            boingsound.play()
        if bg_x[0] < -330:

            current_direction = "right"
            player_image = pygame.transform.rotate(player_original, 270)
            player_hitbox = player_image.get_rect(center=player_hitbox.center)
            boingsound.play()
        if bg_y[0] > 180:

            current_direction = "up"
            player_image = player_original
            player_hitbox = player_image.get_rect(center=player_hitbox.center)
            boingsound.play()
        if bg_y[0] < -180:

            current_direction = "down"
            player_image = pygame.transform.rotate(player_original, 180)
            player_hitbox = player_image.get_rect(center=player_hitbox.center)
            boingsound.play()

        

        screen.blit(player_image, player_hitbox)
        H2p1 =  font2.render("Click on orange enemies     ", 1, WHITE)
        H2p2 =  font2.render("Red peppers increase speed", 1, WHITE)
        H2p3 =  font2.render("Health kits heal 1 life    ", 1, WHITE)
        H2p4 =  font2.render("Watch out for imposters     ", 1, WHITE)
        H2p5 =  font2.render("WASD to move     ", 1, WHITE)
        Livestext = font.render("Health: " + str(lives), 1, RED)
        Leveltext = font.render("Level: " + str(level), 1, YELLOW)
        Quittext = font2.render("Press ESC to Quit", 1, WHITE)
        screen.blit(H2p5, (10, SCREEN_HEIGHT - H2p5.get_height()*5 - 10))
        screen.blit(H2p1, (10, SCREEN_HEIGHT - H2p1.get_height()*4))
        screen.blit(H2p2, (10, SCREEN_HEIGHT - H2p2.get_height()*3))
        screen.blit(H2p3, (10, SCREEN_HEIGHT - H2p3.get_height()*2))
        screen.blit(H2p4, (10, SCREEN_HEIGHT - H2p4.get_height()*1))

        screen.blit(Livestext, (SCREEN_WIDTH - Livestext.get_width() - 10, 10))
        screen.blit(Leveltext, (10,10))
        screen.blit(Quittext, (SCREEN_WIDTH/2 - Quittext.get_width()/2,10))
        pygame.display.update()
        clock.tick(60)
    main()
if __name__ == "__main__":
    main()