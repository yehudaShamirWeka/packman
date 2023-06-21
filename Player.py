class Player:
    posX = 0
    posY = 0

    def __init__(self):
        pass



class Pacman(Player):
    def __init__(self):
        pass

    def moveLeft

    # def move(self):


    # def move(self):
    #     keys = pygame.key.get_pressed()
    #     if keys[pygame.K_w]:
    #         player_pos.y -= 300 * dt
    #     if keys[pygame.K_s]:
    #         player_pos.y += 300 * dt
    #     if keys[pygame.K_a]:
    #         player_pos.x -= 300 * dt
    #     if keys[pygame.K_d]:
    #         player_pos.x += 300 * dt





class Ghost(Player):
    def __init__(self):
        # (5,5) is where ghosts start - to improve
        self.posX = 5
        self.posY = 5

    def move(self):
        x =