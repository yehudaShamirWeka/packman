
CELL_SIZE = 5
class Cell:

    def __init__(self, offset_x, offset_y):
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.pygame = pygame
        self.screen = screen

class Wall(Cell):
    def __init__(self, offset_x, offset_y):
        super(offset_x, offset_y)

    def draw(self, pygame, screen):
        pygame.draw.rect(screen, "blue", (self.offset_x, self.offset_y, CELL_SIZE, CELL_SIZE))
class Coin(Cell):
    def __init__(self, offset_x, offset_y):
        super(offset_x, offset_y)

    def draw(self, pygame, screen):
        pygame.draw.circle(screen, "yellow", (self.offset_x, self.offset_y, CELL_SIZE, CELL_SIZE))