from Player import Pacman, Ghost
from board import Board


class Game:

    def __init__(self, num_ghosts):
        self.board = Board(15, 15)
        self.players = []
        #init players
        self.players.append(Pacman())

        for _ in range(num_ghosts):
            self.players.append(Ghost())

        # TODO
        # for p in self.players:
        #     p.draw()

    def concludeState(self):
        #if ghost + pacman have the same state
        for p in self.players:
            if isinstance(p, Pacman):
                continue
            if self.players[0].posX == p.posX and self.players[0].posY == p.posY:
                #Pacman lose
                gameEnd()
            if not self.board.IsThereAnyCoins():
                #Pacman won



    def run(self):
        while True:
            #Move every player
            for p in self.players:
                p.move()

            concludeState()



    def gameEnd(self):
        pass







