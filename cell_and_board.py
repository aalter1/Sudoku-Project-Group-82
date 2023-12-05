import pygame


class Cell:
  def __init__(self, value, row, col, screen):
    self.value = value
    self.row = row
    self.col = col
    self.screen = screen

  def set_cell_value(self, value):
    self.value = value
    
  def set_sketched_value(self, value):
    self.value = value

  def draw(self, screen):
    pass
# Add the following method to the Cell class in cell_and_board.py

def draw(self):
    pygame.draw.rect(self.screen, (255, 255, 255), (self.col * 67, self.row * 66, 60, 60))
    # pygame.draw.rect(screen, (255, 255, 255), (100, 100, 100, 100), 1)

class Board:
  def __init__(self, width, height, screen, difficulty):
    self.width = width
    self.height = height
    self.screen = screen
    self.difficulty = difficulty

  def draw(self, screen):
    # draws outer border and outer grid
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 600, 600), 4)
    pygame.draw.line(screen, (0, 0, 0), (0, 200), (600, 200), 4)
    pygame.draw.line(screen, (0, 0, 0), (0, 400), (600, 400), 4)
    pygame.draw.line(screen, (0, 0, 0), (200, 0), (200, 600), 4)
    pygame.draw.line(screen, (0, 0, 0), (400, 0), (400, 600), 4)
    # draws inner grid using loop
    i = 1
    while (i * 66) < 620:
      pygame.draw.line(screen, (0, 0, 0), (i * 67, 0), (i * 67, 600), 2)
      pygame.draw.line(screen, (0, 0, 0), (0, i * 66), (600, i * 66), 2)
      i += 1
  
  def select(self, row, col):
    pass

  def click(self, x, y):
    pass

  def clear(self):
    pass

  def sketch(self, value):
    pass

  def place_number(self, value):
    pass

  def reset_to_original(self):
    pass

  def is_full(self):
    pass

  def update_board(self):
    pass

  def find_empty(self):
    pass

  def check_board(self):
    pass
  
  