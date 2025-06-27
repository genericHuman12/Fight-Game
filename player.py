import pygame
from time import time

class Player:
    def __init__(self, game, pn):
        self.shootedl = False
        self.shootedr = False
        self.game = game
        self.screen = game.screen
        self.frame = 1
        self.grav = 3
        self.up = 0    
        if pn ==2:
            self.sheet = pygame.image.load("Fight Game\images\Player2sprites.png").convert_alpha()
        elif pn == 1:
            self.sheet = pygame.image.load("Fight Game\images\Player1sprites.png").convert_alpha()
        self.choose_img()
        self.rect = self.image.get_rect()
        self.rect.x = self.screen.get_rect().width/2 + self.rect.width
        self.rect.y = self.screen.get_rect().height/2
        self.movleft = False
        self.movright = False
        self.sheild = self.extract_img(self.sheet, 130, 0, 40, 60)
        self.sheilded = False
        self.sheild_rect = self.sheild.get_rect()
        self.shot = self.extract_img(self.sheet, 305, 51, 50, 42)
        self.shot_rect = self.shot.get_rect()
        self.attackedr = False
        self.attackedl = False

    def extract_img(self, sheet, startx, starty, width, hieght):
        #Get Images
        img = pygame.Surface((width, hieght)).convert_alpha()
        img.fill((123,0,255))
        img.blit(sheet, (0,0), ((startx, starty, width, hieght)))
        img = pygame.transform.scale(img, (width*3, hieght*3))
        img.set_colorkey((123,0,255))
        self.now = time()
        self.legth = 0
        self.new_frame = 0
        self.waiting = False
        return img

    def choose_img(self):
        #Changes the images
        if self.frame == 1:
            self.image = self.extract_img(self.sheet, 5, 8, 55, 52)
        elif self.frame == 2:
            self.image = self.extract_img(self.sheet, 65, 8, 55, 52)
        elif self.frame == 3:
            self.image = self.extract_img(self.sheet, 180, 6, 60, 54)
        elif self.frame == 4:
            self.image = self.extract_img(self.sheet, 240, 6, 60, 54)
        if self.shootedl:
            self.shot = self.extract_img(self.sheet, 305, 51, 50, 42)
        elif self.shootedr:
            self.shot = self.extract_img(self.sheet, 365, 51, 50, 42)

    def place(self):
        #Makes it so that the player stays in one place
        posx, posy = self.rect.x, self.rect.y
        self.rect=self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy      

    def update(self):
        #Does all the update stuff
        if self.frame == (1 or 3):
            self.sheild_rect.right = self.rect.right
        if self.frame == (2 or 4):
            self.sheild_rect.left = self.rect.left
        self.sheild_rect.bottom = self.rect.bottom
        self.wait(self.now, self.legth, self.new_frame)
        if self.game.running:
            if self.movleft:
                self.rect.x -= 2
            if self.movright:
                self.rect.x += 2
        if self.rect.y < self.screen.get_rect().height*3/4:
            self.rect.y += self.grav
        self.rect.y -= self.up
        if self.up > 0:
            self.up -= self.grav 
        if self.sheilded:
            self.attackedl=False
            self.attackedr=False
            self.movleft = False
            self.movright = False
        self.shooting()       
        self.attackl()
        self.attackr()
    
    def draw(self):
        #puts it on the screen
        self.screen.blit(self.image, self.rect)
        if self.sheilded:
            self.screen.blit(self.sheild, self.sheild_rect)
        if self.shootedl or self.shootedr:
            self.screen.blit(self.shot, self.shot_rect)
            print("drawing shot at", self.shot_rect.topleft)

    def wait(self, start, length, frame):
        if self.waiting:
            now = time()
            if round((now - start),2) == float(length):
                self.frame = frame
#all the attacks
    def attackr(self):
        if self.attackedr:
            self.movleft = False
            self.movright = False
            self.sheilded = False
            self.frame = 4
            self.choose_img()
            self.place()

    
    def attackl(self):
        if self.attackedl:
            self.movleft = False
            self.movright = False
            self.sheilded = False
            self.frame = 3
            self.choose_img()
            self.place()           

    def shootl(self):
        self.shootedl = True
        self.shot = self.extract_img(self.sheet, 305, 51, 50, 42)
        self.shot_rect = self.shot.get_rect()  # Reset rect position
        self.shot_rect.centery = self.rect.centery
        self.shot_rect.right = self.rect.left
        self.frame = 1

    def shooting(self):
        if self.shootedl:
            self.shot_rect.x -= 10
            if self.shot_rect.right < 0:
                self.shootedl = False
        elif self.shootedr:
            self.shot_rect.x += 10
            if self.shot_rect.left > self.screen.get_rect().width:
                self.shootedr = False
