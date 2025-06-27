import pygame

#Menu code

class Menu:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.font = pygame.font.SysFont("Times New Roman", 48)
        self.rect = pygame.rect.Rect(self.screen_rect.width*(1/3), self.screen_rect.height*(1/3), self.screen_rect.width*(1/3), self.screen_rect.height*(1/3),)
        
    def txt(self):
        p1 = "Player 1 Controls:"
        p1ctrls = "Move: WAD|Attack: Q/E|Sheild: S"
        self.p1img = self.font.render(p1, None, "White", "Black")
        self.p1rect = self.p1img.get_rect()
        self.p1rect.topleft = self.rect.topleft
        self.p1cimg = self.font.render(p1ctrls, None, "White", "Black")
        self.p1crect = self.p1cimg.get_rect()
        self.p1crect.topleft = self.p1rect.bottomleft
        #
        p2 = "Player 2 Controls:"
        p2ctrls = "Move: OK;|Attack: I/P|Sheild: L"
        self.p2img = self.font.render(p2, None, "White", "Black")
        self.p2rect = self.p2img.get_rect()
        self.p2rect.topleft = self.p1crect.bottomleft
        self.p2cimg = self.font.render(p2ctrls, None, "White", "Black")
        self.p2crect = self.p2cimg.get_rect()
        self.p2crect.topleft = self.p2rect.bottomleft
        #
        self.playimg = self.font.render("PLAY!", 0, "green", "Black")
        self.playrect = self.playimg.get_rect()
        self.playrect.midtop = self.rect.midbottom
        self.playrect.y += 10

    def draw(self):
        if not self.game.running:
            pygame.draw.rect(self.screen, "black", self.rect)
            self.screen.blit(self.p1img, self.p1rect)
            self.screen.blit(self.p1cimg, self.p1crect)
            self.screen.blit(self.p2img, self.p2rect)
            self.screen.blit(self.p2cimg, self.p2crect)
            self.screen.blit(self.playimg, self.playrect)
        
