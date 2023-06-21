import pygame

from board_objects import *

class Board:
    def __init__(self, x, y):
        self.x = x
        self.coins = 0
        self.y = y
        self.board = [[None for _ in range(self.y)] for i in range(self.x)]
        # self.screen_w = screen.get_width()
        # self.scree_h = screen.creen.get_height()
        self.init()

    def init(self, ):
        #Draw walls TODO
        board_string = '''
#############
#***********#
#***********#
#***********#
#############

         
        '''

        for y, line in enumerate(board_string.strip().splitlines()):
            print(line)
            for x, c in enumerate(line.strip()):
                if c == '#':
                    self.board[x][y] = Wall()
                elif c == '*':
                    self.board[x][y] = Coin()
                    self.coins += 1


        #Create array of players

    def draw(self, screen):
        for i in range(self.x):
            for j in range(self.y):
                #print(f'i={i}, j={j}')
                if self.board[i][j] is not None:
                    self.board[i][j].draw(screen, i * CELL_SIZE, j * CELL_SIZE)













    def areThereAnyCoins(self):
        return self.coins == 0