import pygame
import sudoku_generator
font = pygame.font.SysFont("Georgia", 40)

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

  def draw(self):
    pygame.draw.rect(self.screen, (255, 0, 0), (0, 0, self.row, self.col), 1)

def draw(self):
    pygame.draw.rect(self.screen, (255, 255, 255), (self.col * 67, self.row * 66, 60, 60))

class Board:
  def __init__(self, width, height, screen, difficulty):
    self.width = width
    self.height = height
    self.screen = screen
    self.difficulty = difficulty

  def draw(self):
    # draws outer border and outer grid
    pygame.draw.rect(self.screen, (0, 0, 0), (0, 0, self.width, self.height), 4)
    pygame.draw.line(self.screen, (0, 0, 0), (0, 200), (self.width, 200), 4)
    pygame.draw.line(self.screen, (0, 0, 0), (0, 400), (self.width, 400), 4)
    pygame.draw.line(self.screen, (0, 0, 0), (200, 0), (200, self.height), 4)
    pygame.draw.line(self.screen, (0, 0, 0), (400, 0), (400, self.height), 4)
    # draws inner grid using loop
    i = 1
    while (i * 66) < 620:
      pygame.draw.line(self.screen, (0, 0, 0), (i * 67, 0), (i * 67, self.height), 2)
      pygame.draw.line(self.screen, (0, 0, 0), (0, i * 66), (self.width, i * 66), 2)
      i += 1

    for row in range(10):
      for col in range(10):
        cell = Cell(0, row, col, self.screen)
        grid.draw()
                      
    
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
  
  