import pygame
import sys
from time import time
from player import Player
from scoreboard import Scoreboard
from menu import Menu

class Fight:
    def __init__(self):
        #Defines variables
        pygame.init()
        self.running = False
        self.screen = pygame.display.set_mode((1200, 800))
        self.screen_rect = self.screen.get_rect()
        self.screen_width = self.screen_rect.width
        self.screen_hieght = self.screen_rect.height
        self.player = Player(self, 1)
        self.player2 = Player(self, 2)
        self.score1 = 0
        self.score2 = 0
        self.scorboard = Scoreboard(self)
        self.menu = Menu(self)
        self.reset()

    def run(self):
        #main loop
        while True:
            self.check_events()
            self.player.update()
            self.player.choose_img()
            self.player2.update()
            self.player2.choose_img()
            self.check_collide()
            self.scorboard.txt()
            self.menu.txt()
            self.update_screen()
    
    def update_screen(self):
        #draws the things on the screen
        self.screen.fill((50,50,50))
        self.player.draw()
        self.player2.draw()
        self.scorboard.draw()
        self.menu.draw()
        pygame.display.flip()
    
    def check_events(self):
        #Checks key presses and mouse clicks
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if self.running:
                    self.check_downs(event)
            if event.type == pygame.KEYUP:
                self.check_ups(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.check_mouse(mouse_pos)

    def check_mouse(self, pos):
        #checks mouse clicks
        if self.menu.playrect.collidepoint(pos) and not self.running:
            self.running = True

    def check_downs(self, event):
        #checks the keypresse
        if event.key == pygame.K_b:
            sys.exit()
        if event.key == pygame.K_d:
            self.player.frame = 2
            self.player.choose_img()
            self.player.movright = True
        if event.key == pygame.K_a:
            self.player.frame = 1
            self.player.choose_img()
            self.player.movleft = True
        if event.key == pygame.K_w:
            self.player.up = 48
        if event.key == pygame.K_e:
            self.player.attackedr = True
        if event.key == pygame.K_q:
            self.player.attackedl = True
        if event.key == pygame.K_s:
            self.player.sheilded = True
        if event.key == pygame.K_x:
            self.player.shootl()
        if event.key == pygame.K_SEMICOLON:
            self.player2.frame = 2
            self.player2.choose_img()
            self.player2.movright = True
        if event.key == pygame.K_k:
            self.player2.frame = 1
            self.player2.choose_img()
            self.player2.movleft = True
        if event.key == pygame.K_o:
            self.player2.up = 48
        if event.key == pygame.K_p:
            self.player2.attackedr = True
        if event.key == pygame.K_i:
            self.player2.attackedl = True
        if event.key == pygame.K_l:
            self.player2.sheilded = True
        if event.key == pygame.K_COMMA:
            self.player2.shootl()
    
    def check_ups(self, event):
        if event.key == pygame.K_d:
            self.player.movright = False
        if event.key == pygame.K_a:
            self.player.movleft = False
        if event.key == pygame.K_s:
            self.player.sheilded = False
        if event.key == pygame.K_SEMICOLON:
            self.player2.movright = False
        if event.key == pygame.K_k:
            self.player2.movleft = False
        if event.key == pygame.K_l:
            self.player2.sheilded = False
        if event.key == pygame.K_q:
            self.player.attackedl = False
            self.player.frame = 1
            self.player.choose_img()
        if event.key == pygame.K_e:
            self.player.attackedr = False
            self.player.frame = 2
            self.player.choose_img()
        if event.key == pygame.K_i:
            self.player2.attackedl = False
            self.player2.frame = 1
            self.player2.choose_img()
        if event.key == pygame.K_p:
            self.player2.attackedr = False
            self.player2.frame = 2
            self.player2.choose_img()
    
    def check_collide(self):
        #Checks collisions between all things
        if self.player.rect.right >= self.screen.get_rect().right:
            self.player.movright = False
        if self.player.rect.left <= self.screen.get_rect().left:
            self.player.movleft = False
        if self.player2.rect.right >= self.screen.get_rect().right:
            self.player2.movright = False
        if self.player2.rect.left <= self.screen.get_rect().left:
            self.player2.movleft = False
        self.check_player_collide()
    
    def check_player_collide(self):
        #player collisions
        if self.player.rect.colliderect(self.player2.rect):
            if not self.player2.sheilded:
                if self.player.attackedl or self.player.attackedr:
                    if not self.player2.attackedr and not self.player2.attackedl:
                        self.score1 += 1
                        self.reset()
                    else:
                        self.reset()
            if not self.player.sheilded:
                if self.player2.attackedl or self.player2.attackedr:
                    if not self.player.attackedr and not self.player.attackedl:
                        self.score2 += 1
                        self.reset()
                    else:
                        self.reset()
    
    def reset(self):
        #positions the players when the game restarts 
        self.player.rect.x = self.screen_rect.width/2 - (self.player.rect.width*2)
        self.player.rect.y = self.screen_hieght/2
        self.player2.rect.x = self.screen_rect.width/2 + self.player2.rect.width
        self.player2.rect.y = self.screen_hieght/2
        self.player2.frame = 1
        self.player.frame = 2


ffight = Fight().run()