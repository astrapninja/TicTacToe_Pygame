import pygame, sys
from ui import *
from settings import *

class Game:
    def __init__(self):
        pygame.init()

        self.state = "Title Screen"
        self.states = [
            "Title Screen",
            "Title Screen Transistion",
            "Game",
            "Game Transition",
        ]
        self.running = True
        self.screen = pygame.display.set_mode((screenX, screenY))
        self.clock = pygame.time.Clock()
        self.ui = UI()
        pygame.display.set_caption("TicTacToe")

    def changeState(self, State):
        self.state = State

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                elif self.running == False:
                    pygame.quit()
                    sys.exit()

            keys = pygame.key.get_pressed()
            if self.running == True:
                if self.state == "Title Screen":
                    self.ui.title_screen()
                    if keys[pygame.K_ESCAPE]:
                        self.running = False
                        print("pressed")
                    elif keys[pygame.K_KP_ENTER] or keys[pygame.K_RETURN]:
                        self.changeState("Game")
                        print(self.state)
                        
                elif self.state == "Game":
                    self.ui.game()

            pygame.display.update()
            self.clock.tick(FPS)


game = Game()

if __name__ == "__main__":
    game.run()