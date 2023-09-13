import pygame, sys
from ui import *
from settings import *

class Game():
    def __init__(self):
        pygame.init()

        self.state = "Title Screen"
        self.states = ["Title Screen", "Title Screen Transistion", "Game", "Game Transition"]
        self.running = False
        self.screen = pygame.display.set_mode((screenX, screenY))
        self.clock = pygame.time.Clock()
        self.ui = UI()
        pygame.display.set_caption("TicTacToe")

    def run(self):
        if self.running == False:
            self.running = True
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                        pygame.quit()
                        sys.exit()
                
                if self.running == True:
                    if self.state == "Title Screen":
                        self.ui.title_screen()
                
                pygame.display.update()
                self.clock.tick(FPS)

game = Game()

if __name__ == "__main__":
    game.run()