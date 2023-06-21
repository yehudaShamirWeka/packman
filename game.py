from Player import Pacman, Ghost
from board import Board
import pygame

class Game:
    def __init__(self, num_ghosts):
        self.board = Board(20, 11)
        self.players = []
        self.players.append(Pacman(1, 1))

    def concludeState(self):
        #if ghost + pacman have the same state

        if not self.board.areThereAnyCoins():
            print('no coins')
            return False

        for p in self.players:
            if isinstance(p, Pacman):
                continue
            if self.players[0].posX == p.posX and self.players[0].posY == p.posY:
                #Pacman lose
                # gameEnd()
                return False

            if not self.board.areThereAnyCoins():
                #Pacman won
                return False

        return True

    def run(self):
        # global screen, clock

        screen = pygame.display.set_mode((1400, 1400))
        clock = pygame.time.Clock()

        running = True
        dt = 0

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("gray")

        gameloop_index = 0
        # player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

        while running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Move every player
            for p in self.players:
                p.move(self.board)

            # print("Drawing %s" % gameloop_index)
            self.board.draw(screen, self.players)

            if not self.concludeState():
                break

            # flip() the display to put your work on screen
            pygame.display.flip()

            # limits FPS to 60
            # dt is delta time in seconds since last frame, used for framerate-
            # independent physics.
            gameloop_index += 1
            dt = clock.tick(10) / 1000

        print("Game ended")
        # pygame.quit()


    def gameEnd(self):
        pass







