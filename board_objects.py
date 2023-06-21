import pygame

CELL_SIZE = 40

class Cell:
    collisionable = False
    collectable = False

    def __init__(self):
        pass

    def draw(self, screen, offset_x, offset_y):
        pygame.draw.rect(screen, "black", (offset_x, offset_y, CELL_SIZE, CELL_SIZE))


class Wall(Cell):
    collisionable = True

    def __init__(self):
        super()

    def draw(self, screen, offset_x, offset_y):
        pygame.draw.rect(screen, "blue", (offset_x, offset_y, CELL_SIZE, CELL_SIZE))


class Coin(Cell):
    collectable = True
    score = 1

    def __init__(self):
        super()

    def coin_size(self):
        return CELL_SIZE / 7

    def draw(self, screen, offset_x, offset_y):
        pygame.draw.circle(screen, "yellow", (offset_x + CELL_SIZE / 2, offset_y + CELL_SIZE / 2), self.coin_size())


class SuperCoin(Coin):
    score = 1000
    def coin_size(self):
        return CELL_SIZE / 5