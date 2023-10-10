import pygame
from constants import *


class Main():
    def __init__(self) -> None:
        pygame.init()
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption(WINDOW_TITLE)
        self.state = []
        self.images = {}
        self.font = self.loadFont()

    def loadImages(self) -> None:
        pieces = ["wP", "wR", "wN", "wB", "wQ", "wK", "bP", "bR", "bN", "bB", "bQ", "bK"]
        for piece in pieces:
            image = pygame.transform.scale(pygame.image.load(f"assets/{piece}.png"), (SQ_SIZE - 15, SQ_SIZE - 15))
            self.images[piece] = image
    
    def loadFont(self) -> None:
        self.font = pygame.font.SysFont(FONT, 18, bold=True)

    def popState(self):
        self.state.pop()

    def pushState(self, state):
        self.state.append(state)

    def getActiveState(self):
        return self.state[-1]

    def mainLoop(self):
        while(True):
            activeState = self.getActiveState()
            if (activeState == None):
                continue
            
            activeState.update()

            self.window.fill("black")
            activeState.draw()
            pygame.display.flip()


if __name__ == "__main__":
    main = Main()
    main.mainLoop
