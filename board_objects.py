import pygame

CELL_SIZE = 40
class Cell:

    def __init__(self):
        pass


class Wall(Cell):
    def __init__(self):
        super()

    def draw(self, screen, offset_x, offset_y):
        pygame.draw.rect(screen, "blue", (offset_x, offset_y, CELL_SIZE, CELL_SIZE))


class Coin(Cell):
    def __init__(self):
        super()

    def coin_size(self):
        return CELL_SIZE / 7
    def draw(self, screen, offset_x, offset_y):

        pygame.draw.circle(screen, "yellow", (offset_x + CELL_SIZE / 2, offset_y + CELL_SIZE / 2), self.coin_size())
        # pygame.draw.rect(screen, "yellow", (offset_x, offset_y, CELL_SIZE, CELL_SIZE))
