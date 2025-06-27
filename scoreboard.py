import pygame

class Scoreboard:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.font = pygame.font.SysFont("Times New Roman", 48, True)
        
    def txt(self):
        p1score = f"Player 1 Score: {self.game.score1}"
        self.p1simg = self.font.render(p1score, 0, "white", (50,50,50))
        self.p1srect = self.p1simg.get_rect()
        self.p1srect.topleft = self.screen.get_rect().topleft
        p2score = f"Player 2 Score: {self.game.score2}"
        self.p2simg = self.font.render(p2score, 0, "white", (50,50,50))
        self.p2srect = self.p2simg.get_rect()
        self.p2srect.topright = self.screen.get_rect().topright
    
    def draw(self):
        self.screen.blit(self.p1simg, self.p1srect)
        self.screen.blit(self.p2simg, self.p2srect)