import pygame

from board_objects import *

class Board:
    def __init__(self, x, y):
        self.x = x
        self.coins = 0
        self.score = 0
        self.y = y
        self.board = [[None for _ in range(self.y)] for i in range(self.x)]
        self.init()

    def init(self, ):
        board_string = '''
####################
# ***#********#****#
#*##*#*######*#*##*#
#*#**************#*#
#*#*##*##**##*##*#*#
#******#****#******#
#*#*##*######*##*#*#
#*#**************#*#
#*##*#*######*#*##*#
#****#********#***@#
####################

        
        '''


        for y, line in enumerate(board_string.strip().splitlines()):
            for x, c in enumerate(line.strip()):
                if c == '#':
                    self.board[x][y] = Wall()
                elif c == '*':
                    self.board[x][y] = Coin()
                    self.coins += 1
                elif c == '@':
                    self.board[x][y] = SuperCoin()
                    self.coins += 1
                elif c == ' ':
                    self.board[x][y] = Cell()


    def draw(self, screen, players):
        screen.fill("black")
        for i in range(self.x):
            for j in range(self.y):
                #print(f'i={i}, j={j}')
                if self.board[i][j] is not None:
                    self.board[i][j].draw(screen, i * CELL_SIZE, j * CELL_SIZE)

        for p in players:
            p.draw(screen, p.posX * CELL_SIZE, p.posY * CELL_SIZE)

        # print score
        font = pygame.font.SysFont(None, 60)
        img = font.render(f"SCORE: {self.score}", True, "yellow")
        screen.blit(img, (600, 600))

    def draw_win(self, screen):
        # print score
        font = pygame.font.SysFont(None, 200)
        img = font.render(f"YOU WIN!!!!!!!!!!!! : {self.score}", True, "yellow")
        screen.blit(img, (200, 200))


    def areThereAnyCoins(self):
        return self.coins != 0

    def is_collisionable(self, x, y):
        if self.board[x][y] is not None and self.board[x][y].collisionable:
            return True
        return False

    def is_collectable(self, x, y):
        if self.board[x][y] and self.board[x][y].collectable:
            return True
        return False

    def collect_coins(self, x, y):
        if self.board[x][y] is not None and self.board[x][y].collectable:
            self.score += self.board[x][y].score
            self.coins -= 1
            self.board[x][y] = Cell()

        print(f"score={self.score}")
        print(f"coins={self.coins}")






