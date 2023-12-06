import pygame
import button
from sudoku_generator import generate_sudoku
from cell_and_board import Cell, Board
import sys

pygame.init()

draw = True
input_row, input_col = None, None

# screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 700

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
easy_button = button.Button(50, 500, easy_img, 1)
medium_button = button.Button(205, 500, medium_img, 1)
hard_button = button.Button(400, 500, hard_img, 1)
exit_button = button.Button(100, 625, exit_img, .75)
reset_button = button.Button(225, 625, reset_img, .75)
restart_button = button.Button(375, 625, restart_img, .75)

# Function to place text on window
def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

def draw_input_box(value, row, col, initial=False):
  cell_size = 67
  border_thickness = 1

  # Draw the top border
  pygame.draw.rect(screen, (0, 0, 0), (col * cell_size, row * cell_size, cell_size, border_thickness))

    # Draw the left border
  pygame.draw.rect(screen, (0, 0, 0), (col * cell_size, row * cell_size, border_thickness, cell_size))

    # Draw the right border
  pygame.draw.rect(screen, (0, 0, 0), (col * cell_size + cell_size - border_thickness, row * cell_size, border_thickness, cell_size))
  
  # Draw the filled rectangle with different colors for initial and user-modified cells
  if initial:
      pygame.draw.rect(screen, (0, 0, 0), (col * cell_size + border_thickness, row * cell_size + border_thickness,
                                                cell_size - 2 * border_thickness, cell_size - 2 * border_thickness), 1)
  else:
      pygame.draw.rect(screen, (255, 0, 0), (col * cell_size + border_thickness, row * cell_size + border_thickness,
                                                cell_size - 2 * border_thickness, cell_size - 2 * border_thickness), 1)

  font = pygame.font.Font(None, 40)
  text_content = str(value) if value != 0 else ""  # Render an empty string if the value is 0
  text_surface = font.render(text_content, True, (0, 0, 0))
  text_rect = text_surface.get_rect(center=(col * cell_size + cell_size // 2, row * cell_size + cell_size // 2))
  screen.blit(text_surface, text_rect)

board = generate_sudoku(9, 30)

# game loop
run = True
while run:

  # menu color
  screen.fill((52, 78, 91))

  # Menu state and draw buttons
  if menu_state == "main":
    draw_text("Welcome to Sudoku", font, TEXT_COL, 100, 100)
    draw_text("Select Game Mode:", font, TEXT_COL, 110, 200)
    if easy_button.draw(screen):
      menu_state = "easy"
      board = generate_sudoku(9, 30)
      user_modified_board = [[0 for _ in range(9)] for _ in range(9)]
    if medium_button.draw(screen):
      menu_state = "medium"
      board = generate_sudoku(9, 40)
      user_modified_board = [[0 for _ in range(9)] for _ in range(9)]
    if hard_button.draw(screen):
      menu_state = "hard"
      board = generate_sudoku(9, 50)
      user_modified_board = [[0 for _ in range(9)] for _ in range(9)]
  
  # Easy Mode
  if menu_state == "easy":
    board_obj = Board(600, 600, screen, menu_state)
    board_obj.draw()
    for row in range(9):
      for col in range(9):
        cell_value = user_modified_board[row][col]
        initial_value = board[row][col]
        cell = Cell(cell_value, row, col, screen)
        cell.draw()
      
        # implement draw in grid
        if input_row == row and input_col == col:
          draw_input_box(cell_value, row, col)
        
        # Highlight the initially filled cells
        if initial_value != 0:
          draw_input_box(initial_value, row, col, initial=True)
    if exit_button.draw(screen):
      run = False
    if reset_button.draw(screen):
      menu_state = 'main'
      menu_state = 'easy'
    if restart_button.draw(screen):
      menu_state = "main"
  
  # Medium Mode
  if menu_state == "medium":
    board_obj = Board(600, 600, screen, menu_state)
    board_obj.draw()
    for row in range(9):
      for col in range(9):
        cell_value = user_modified_board[row][col]
        initial_value = board[row][col]
        cell = Cell(cell_value, row, col, screen)
        cell.draw()

        # implement draw in grid
        if input_row == row and input_col == col:
          draw_input_box(cell_value, row, col)

        # Highlight the initially filled cells
        if initial_value != 0:
          draw_input_box(initial_value, row, col, initial=True)
    if exit_button.draw(screen):
      run = False
    if reset_button.draw(screen):
      pass
    if restart_button.draw(screen):
      menu_state = "main"
  
  # Hard Mode
  if menu_state == "hard":
    board_obj = Board(600, 600, screen, menu_state)
    board_obj.draw()
    for row in range(9):
      for col in range(9):
        cell_value = user_modified_board[row][col]
        initial_value = board[row][col]
        cell = Cell(cell_value, row, col, screen)
        cell.draw()

        # implement draw in grid
        if input_row == row and input_col == col:
          draw_input_box(cell_value, row, col)

        # Highlight the initially filled cells
        if initial_value != 0:
          draw_input_box(initial_value, row, col, initial=True)
    if exit_button.draw(screen):
      run = False
    if reset_button.draw(screen):
      pass
    if restart_button.draw(screen):
      menu_state = "main"
  
  # Player Winner
  if menu_state == "win":
    draw_text("Game Won!", font, TEXT_COL, 200, 100)
    exit_button = button.Button(335, 300, exit_img, 1)
    if exit_button.draw(screen):
      run = False
  
  # Player Loser
  if menu_state == "lose":
    draw_text("Game Over :(", font, TEXT_COL, 200, 100)
    restart_button = button.Button(335, 300, restart_img, 1)
    if restart_button.draw(screen):
      menu_state = "main"

  # Window functionality/ top right x button
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    elif event.type == pygame.MOUSEBUTTONDOWN:
      mouseX, mouseY = pygame.mouse.get_pos()
      row = mouseY // 66
      col = mouseX // 66

      # Check if the click is within the board boundaries
      if 0 <= row < 9 and 0 <= col < 9 and board[row][col] == 0:
        input_row, input_col = row, col
      else:
        input_row, input_col = None, None
        
    # Allows for digits to be placed in cell    
    elif event.type == pygame.KEYDOWN:
      if input_row is not None and input_col is not None:
        key_name = pygame.key.name(event.key)
        if key_name.isdigit() and 1 <= int(key_name) <= 9:
          user_modified_board[input_row][input_col] = int(key_name)
        elif event.key == pygame.K_RETURN:
          board[input_row][input_col] = user_modified_board[input_row][input_col]
      
  
  pygame.display.flip()
