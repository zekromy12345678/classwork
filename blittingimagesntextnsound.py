import pygame

#Initialize pygame
pygame.init()

#Create display surface
window_width = 600
window_height = 300
display_surface = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Blitting Images!")

#Create images (surface objects)
dragon_left_image = pygame.image.load("dragon_left.png")
dragon_left_rect = dragon_left_image.get_rect()
dragon_left_rect.topleft = (0,0)

dragon_right_image = pygame.image.load("dragon_right.png")
dragon_right_rect = dragon_right_image.get_rect()
dragon_right_rect.topright = (window_width,0)

#Define colors
GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)
BLACK = (0, 0, 0)


#Define fonts
system_font = pygame.font.SysFont("calibri", 64)
custom_font = pygame.font.Font("AttackGraffiti.ttf", 48)

#Define text
system_text = system_font.render("Dragons Rule!", True, GREEN, DARKGREEN)
system_text_rect = system_text.get_rect()
system_text_rect.center = (window_width//2, window_height//8)

custom_text = custom_font.render("Move the dragon soon!", True, GREEN)
custom_text_rect = custom_text.get_rect()
custom_text_rect.center = (window_width//2, window_height//1.5)

#Load Sound Effects
sound_1 = pygame.mixer.Sound("sound_1.wav")
sound_2 = pygame.mixer.Sound("sound_2.wav")



#The main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Blit (copy) a surface object at the given coordinates of our display
    display_surface.blit(dragon_left_image, dragon_left_rect)
    display_surface.blit(dragon_right_image, dragon_right_rect)

    #Blit (copy) the text surfaces to the display surface
    display_surface.blit(system_text, system_text_rect)
    display_surface.blit(custom_text, custom_text_rect)

    pygame.draw.line(display_surface, (255, 255, 255), (0, 75), (window_width, 75), 4)

    sound_1.play()
    pygame.time.delay(2000)
    sound_2.play()
    pygame.time.delay(2000)

    #Change the volume of a sound effect
    sound_2.set_volume(.1)
    sound_2.play()

    #load background music
    pygame.mixer.music.load("music.wav")

    #Play and stop the music
    pygame.mixer.music.play(-1, 0.0)
    pygame.time.delay(1000)
    sound_2.play()
    pygame.time.delay(5000)
    pygame.mixer.music.stop()

    #Update the display
    pygame.display.update()

#end the game
pygame.quit()