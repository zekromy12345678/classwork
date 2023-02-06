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

#See all available fonts
fonts = pygame.font.get_fonts()
for font in fonts:
    print(font)

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

    #Update the display
    pygame.display.update()

#end the game
pygame.quit()