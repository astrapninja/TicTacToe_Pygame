import pygame, sys
from settings import *

class Square(pygame.sprite.Sprite):
    def __init__(self, x, y, row, col):
        super().__init__()
        self.image = None
        if row == 0:
            if col == 0:
                self.image = pygame.image.load('Graphics\Assets\TopLeft.png')
            elif col == 1:
                self.image = pygame.image.load('Graphics\Assets\TopMiddle.png')
            elif col == 2:
                self.image = pygame.image.load('Graphics\Assets\TopRight.png')
        elif row == 1:
            if col == 0:
                self.image = pygame.image.load('Graphics\Assets\MiddleLeft.png')
            elif col == 1:
                self.image = pygame.image.load('Graphics\Assets\Middle.png')
            elif col == 2:
                self.image = pygame.image.load('Graphics\Assets\MiddleRight.png')
        elif row == 2:
            if col == 0:
                self.image = pygame.image.load('Graphics\Assets\BottomLeft.png')
            elif col == 1:
                self.image = pygame.image.load('Graphics\Assets\BottomMiddle.png')
            elif col == 2:
                self.image = pygame.image.load('Graphics\Assets\BottomRight.png')
        self.rect = self.image.get_rect(topleft = (x, y))

class UI():
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.font = pygame.font.Font(None, 32)
        self.title_surf = self.font.render("TicTacToe", True, (0, 55, 55))
        self.squares = pygame.sprite.Group()
        self.background = pygame.image.load('Graphics\Backgrounds\Background.png')
        self.background_rect = self.background.get_rect(topleft = (0,0))
        for row in range(3):
            for col in range(3):
                self.squares.add(Square((self.screen.get_width()/2 - 80*1.5)+(80*col), (self.screen.get_height()/8)+(80*row), row, col))
    
    def title_screen(self):
        self.screen.blit(self.background, self.background_rect)
        self.screen.blit(self.title_surf, ((self.screen.get_width()/2)-self.title_surf.get_width()/2,(self.screen.get_height()/8)-self.title_surf.get_height()/2))
        self.play_button = pygame.draw.rect(self.screen, (0, 0, 0), [(self.screen.get_width()/2)-(self.screen.get_width()/8)/2, (self.screen.get_height()/2)-(self.screen.get_height()/8)/2, self.screen.get_width()/8, self.screen.get_height()/8])
    
    def game(self):
        self.screen.blit(self.background, self.background_rect)
        self.squares.draw(self.screen)

    def display(self):
        pass