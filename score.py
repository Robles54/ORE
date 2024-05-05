import pygame

class Score:
    def __init__(self):
        self.count = 0
        self.font = pygame.font.SysFont("comicsans", 50, True, True)

        self.black = (0, 0, 0)

    def show_score(self, screen):
        text = self.font.render("Score: " + str(self.count), 1, self.black)
        screen.blit(text, (100, 100))

    def score_up(self):
        self.count += 1