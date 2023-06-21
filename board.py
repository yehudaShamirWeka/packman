import pygame

from cell import *


class Board:



    def __init__(self, x, y, screen, pygame):
        self.x = x
        self.y = y
        self.screen = screen
        self.pygame = pygame
        self.board = [[None for _ in range(self.y)] for i in range(self.x)]
        # self.screen_w = screen.get_width()
        # self.scree_h = screen.creen.get_height()
        self.init()

    def init(self, ):
        #Draw walls TODO
        self.board[10][10] = Wall()
        self.board[10][11] = Wall()
        self.board[10][12] = Wall()
        self.board[10][13] = Wall()
        self.board[10][14] = Wall()

        # Draw coins
        for i in range(self.x):
            for j in range(self.y):

                # if now wall do coin
                if not isinstance(self.board[i][j], Wall):
                    self.board[i][j] = Coin()

                self.board[i][j].draw(screen, )

        #Create array of players




