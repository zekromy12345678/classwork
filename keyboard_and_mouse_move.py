import pygame

#Initialize pygame
pygame.init()

#Create our display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Discrete Movement!")

#Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

#Set game values
VELOCITY = 10

#Load images
dragon_image = pygame.image.load("dragon_right.png")
dragon_rect = dragon_image.get_rect()
dragon_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

#The main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Get a list of all keys being pressed down
    keys = pygame.key.get_pressed()
    print(keys)

    #Move the dragon continously
    if keys[pygame.K_LEFT]:
        dragon_rect.x -= VELOCITY
    if keys[pygame.K_RIGHT]:
        dragon_rect.x += VELOCITY
    if keys[pygame.K_UP]:
        dragon_rect.y -= VELOCITY
    if keys[pygame.K_DOWN]:
        dragon_rect.y += VELOCITY

      
    if event.type == pygame.MOUSEBUTTONDOWN:
        print(event)
        mouse_x = event.pos[0]
        mouse_y = event.pos[1]
        dragon_rect.centerx = mouse_x
        dragon_rect.centery = mouse_y

        #Drag the object when the mouse button is clicked
    if event.type == pygame.MOUSEMOTION and event.buttons[0] == 1:
        print(event)
        mouse_x = event.pos[0]
        mouse_y = event.pos[1]
        dragon_rect.centerx = mouse_x
        dragon_rect.centery = mouse_y
      
    #Fill the display
    display_surface.fill((0, 0, 0))

    #Blit assets
    display_surface.blit(dragon_image, dragon_rect)

    #Update the display
    pygame.display.update()

    #Tick the clock
    clock.tick(FPS)

#End the game
pygame.quit()