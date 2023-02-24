import pygame
import random

#Initialize pygame
pygame.init()

#Set display surface
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 400
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Feed the dragon!")

#Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

#Set game values
"""Be sure to set starting lives of player, as well as player and coin velocity, coin acceleration, and buffer distance."""
PLAYER_STARTING_LIVES =5
PLAYER_VELOCITY = 10
COIN_STARTING_VELOCITY=10
COIN_ACCELERATION = .5
BUFFER_DISTANCE = 100

score= 0
player_lives = PLAYER_STARTING_LIVES
coin_velocity = COIN_STARTING_VELOCITY
#Set Colors
PURPLE = (147,112,219)
DARKPURPLE = (148,0,211)
WHITE = (255,255,255)
BLACK = (0,0,0)

#Set Fonts
font = pygame.font.Font("AttackGraffiti.ttf", 32)

#Set Text
score_text = font.render("Score: "+str(score), True, PURPLE, DARKPURPLE)
score_rect = score_text.get_rect()
score_rect.topleft=(10,10)

title_text = font.render("Feed Dragon", True, PURPLE, DARKPURPLE)
title_rect = title_text.get_rect()
title_rect.centerx = WINDOW_WIDTH//2
title_rect.y = 10

continue_text = font.render("Press any key to play again", True, PURPLE, DARKPURPLE)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 32)

game_over_text = font.render("GAMEOVER", True, PURPLE, DARKPURPLE)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

lives_text = font.render("Lives: " + str(player_lives), True, PURPLE, DARKPURPLE)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH - 10, 10)

#Set Sound and Music
coin_sound = pygame.mixer.Sound("sound_1.wav")
miss_sound = pygame.mixer.Sound("sound_2.wav")
miss_sound.set_volume(.1)
pygame.mixer.music.load("music.wav")

#Set Images
dragon_image = pygame.image.load("dragon_right.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.left = 32
dragon_rect.centery = (WINDOW_HEIGHT//2)

coin_image = pygame.image.load("coin.png")
coin_rect = coin_image.get_rect()
coin_rect.bottom = WINDOW_HEIGHT
coin_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
coin_rect.y = random.randint(64, WINDOW_HEIGHT - 32)

#The Main Game Loop
pygame.mixer.music.play(-1, 0.0)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False      
    if player_lives == 0:
      running = False
  #Get a list of all keys being pressed down
    keys = pygame.key.get_pressed()
  #Move the dragon continously
    if keys[pygame.K_UP] and dragon_rect.top > 64:
      dragon_rect.y -= PLAYER_VELOCITY
    if keys[pygame.K_DOWN] and dragon_rect.bottom < WINDOW_HEIGHT:
      dragon_rect.y += PLAYER_VELOCITY
      
    #Move the coin
    if coin_rect.x<0:
      #Player misses coin
      player_lives -= 1
      miss_sound.play()
      coin_rect.x = WINDOW_WIDTH+ BUFFER_DISTANCE
      coin_rect.y = random.randint(64, WINDOW_HEIGHT-32)
    else:
      #Move coin
      coin_rect.x -= coin_velocity
      
    #check for collisions  
    if dragon_rect.colliderect(coin_rect):
      score +=1
      coin_sound.play()
      coin_velocity += COIN_ACCELERATION
      coin_rect.x = WINDOW_WIDTH + BUFFER_DISTANCE
      coin_rect.y = random.randint(64, WINDOW_HEIGHT-32)  
      
    #Update HUD
    score_text = font.render("Score: " + str(score), True, PURPLE, DARKPURPLE)
    lives_text = font.render("Lives: " + str(player_lives), True, PURPLE, DARKPURPLE)

  #Check for game over
    if player_lives ==0:
      display_surface.blit(game_over_text, game_over_rect)
      display_surface.blit(continue_text, continue_rect)
      pygame.display.update()

      #Pause game until player presses a key, then reset the game
      pygame.mixer.music.stop()
      is_paused = True
      while is_paused:
        for event in pygame.event.get():
          #The player wants to play again
          if event.type == pygame.KEYDOWN:
            score = 0
            player_lives = PLAYER_STARTING_LIVES
            dragon_rect.y = WINDOW_HEIGHT//2
            coin_velocity = COIN_STARTING_VELOCITY
            pygame.mixer.music.play(-1,0.0)
            is_paused = False
          #The player wants to quit
          if event.type == pygame.QUIT():
            is_paused = False
            running = False
 
      
       #Fill the display
    display_surface.fill(BLACK)
    #Blit (copy) the text surfaces to the display surface
    display_surface.blit(score_text, score_rect)
    display_surface.blit(lives_text, lives_rect)
    display_surface.blit(title_text, title_rect)
    #Blit assets
    display_surface.blit(dragon_image, dragon_rect)
    display_surface.blit(coin_image, coin_rect)
  
    #Update the display
    pygame.display.update()

    #Tick the clock
    clock.tick(FPS)

#End the game
pygame.quit()