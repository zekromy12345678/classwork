import pygame
import random

# Initialize Pygame
pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Set the width and height of the screen
WIDTH = 800
HEIGHT = 600

# Set the font and font size
FONT = pygame.font.SysFont(None, 32)

# Load the paragraphs from the file into a list
paragraphs = []
with open('madlibs.txt', 'rt') as file:
    for x in file:
        paragraphs.append(x.strip())

# Define functions for counting variables and asking for input
def count_variables(chosenpara):
    variable_counts = {}
    for word in chosenpara.split():
        if '<' in word and '>' in word:
            index1 = word.index("<") +1
            index2 = word.index(">")
            variable = word[index1:index2]
            if variable in variable_counts:
                variable_counts[variable] += 1
            else:
                variable_counts[variable] = 1
    return variable_counts

def askvariablesnreplace(chosenpara, variable_counts):
    c = 0
    for x in variable_counts.keys():
        j = variable_counts[x]
        while c < j:
            response = input(f"Enter a {x}: ")
            chosenpara = chosenpara.replace(f"<{x}>", response , 1)
            c = c+1
        c = 0
    return chosenpara

# Set up the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mad Libs")

# Set up the game loop
done = False
while not done:
    # Set the background color
    screen.fill(WHITE)

    # Choose a random paragraph and count its variables
    chosenpara = paragraphs[random.randint(0,5)]
    variable_counts = count_variables(chosenpara)

    # Ask for input and replace the placeholders in the paragraph
    completed_para = askvariablesnreplace(chosenpara, variable_counts)

    # Render the completed paragraph on the screen
    text = FONT.render(completed_para, True, BLACK)
    text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2))
    screen.blit(text, text_rect)

    # Render the prompt to play again on the screen
    prompt = FONT.render("Press SPACE to play again", True, BLUE)
    prompt_rect = prompt.get_rect(center=(WIDTH/2, HEIGHT-50))
    screen.blit(prompt, prompt_rect)

    # Update the screen
    pygame.display.update()

    # Wait for input to play again or quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            pass

# Quit Pygame
pygame.quit()
