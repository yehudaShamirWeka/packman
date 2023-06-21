import pygame

from board_objects import CELL_SIZE


class Player:
    def __init__(self, initPosX, initPosY):
        self.posX = initPosX
        self.posY = initPosY

    def posLeft(self):
        return self.posX, self.posY - 1

    def posRight(self):
        return self.posX, self.posY + 1

    def posUp(self):
        return self.posX - 1, self.posY

    def posDown(self):
        return self.posX + 1, self.posY

DIRECTION_UP = 0
DIRECTION_RIGHT = 1
DIRECTION_DOWN = 2
DIRECTION_LEFT = 3

class Pacman(Player):
    def __init__(self, initPosX, initPosY):
        self.direction = DIRECTION_RIGHT
        super().__init__(initPosX, initPosY)

    def pos(self):
        return (self.posX, self.posY)

    def move(self, board):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.direction = DIRECTION_LEFT
        elif keys[pygame.K_s]:
            self.direction = DIRECTION_RIGHT
        elif keys[pygame.K_a]:
            self.direction = DIRECTION_UP
        elif keys[pygame.K_d]:
            self.direction = DIRECTION_DOWN

        newX, newY = self.posByDirection(self.direction)

        # print ("trying to move (dir=%s): %s -> %s" % (self.direction, self.pos(), (newX, newY)))

        if board.is_collisionable(newX, newY):
            # print("collisiion")
            return

        print ('collecting coins')
        board.collect_coins(newX, newY)

        # move
        self.posX = newX
        self.posY = newY



    def posByDirection(self, direction):
        POS = {
            DIRECTION_UP : self.posUp,
            DIRECTION_LEFT: self.posLeft,
            DIRECTION_DOWN: self.posDown,
            DIRECTION_RIGHT: self.posRight,
        }

        return POS[direction]()

    def draw(self, screen, offset_x, offset_y):
        pygame.draw.circle(screen, "green", (offset_x + CELL_SIZE / 2, offset_y + CELL_SIZE / 2), 5)
        # pygame.draw.rect(screen, "yellow", (offset_x, offset_y, CELL_SIZE, CELL_SIZE))




class Ghost(Player):
    def __init__(self):
        # (5,5) is where ghosts start - to improve
        self.posX = 5
        self.posY = 5
#    if my can_move == False, randomize (0,4) choose that direction
#     def move(self):
#         x =

    def draw(self, screen, offset_x, offset_y):
        pygame.draw.circle(screen, "purple", (offset_x + CELL_SIZE / 2, offset_y + CELL_SIZE / 2), 5)

