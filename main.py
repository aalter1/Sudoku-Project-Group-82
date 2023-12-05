import pygame
import button
from sudoku_generator import SudokuGenerator

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sudoku")


# game variable
menu_state = "main"

# define the font
font = pygame.font.SysFont("Georgia", 40)

# define the color
TEXT_COL = (255, 255, 255)

# load images
easy_img = pygame.image.load("img/button_easy.png").convert_alpha()
medium_img = pygame.image.load("img/button_medium.png").convert_alpha()
hard_img = pygame.image.load("img/button_hard.png").convert_alpha()
exit_img = pygame.image.load("img/button_exit.png").convert_alpha()
reset_img = pygame.image.load("img/button_reset.png").convert_alpha()
restart_img = pygame.image.load("img/button_restart.png").convert_alpha()

# button instances
easy_button = button.Button(150, 300, easy_img, 1)
medium_button = button.Button(310, 300, medium_img, 1)
hard_button = button.Button(510, 300, hard_img, 1)
exit_button = button.Button(175, 525, exit_img, .75)
reset_button = button.Button(335, 525, reset_img, .75)
restart_button = button.Button(525, 525, restart_img, .75)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


# game loop
run = True
while run:

    screen.fill((52, 78, 91))

  # Menu state and draw buttons
    if menu_state == "main":
      draw_text("Welcome to Sudoku", font, TEXT_COL, 200, 100)
      draw_text("Select Game Mode:", font, TEXT_COL, 220, 200)
      if easy_button.draw(screen):
        menu_state = "easy"
      if medium_button.draw(screen):
        menu_state = "medium"
      if hard_button.draw(screen):
        menu_state = "hard"
    # Easy Mode
    if menu_state == "easy":
      # Sudoku Gen/ Cell and board
      
      if exit_button.draw(screen):
        run = False
      if reset_button.draw(screen):
        pass
      if restart_button.draw(screen):
        pass
      pass
    # Medium Mode
    if menu_state == "medium":
      # Sudoku Gen/ Cell and board
      
      if exit_button.draw(screen):
        run = False
      if reset_button.draw(screen):
        pass
      if restart_button.draw(screen):
        pass
    # Hard Mode
    if menu_state == "hard":
      # Sudoku Gen/ Cell and board
      
      if exit_button.draw(screen):
        run = False
      if reset_button.draw(screen):
        pass
      if restart_button.draw(screen):
        pass
    # Player Winner
    if menu_state == "win":
      draw_text("Game Won!", font, TEXT_COL, 200, 100)
      exit_button = button.Button(335, 300, exit_img, 1)
      if exit_button.draw(screen):
        run = False
    # Player Loser
    if menu_state == "lose":
      draw_text("Game Over :(", font, TEXT_COL, 200, 100)


    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        pass
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
