import pygame
from algo.board import Board
from algo.pieces import Piece
import algo.ai as ai
from constants import *

class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption(WINDOW_TITLE)
        self.playerColor = None
        self.state = []
        self.images = {}
        self.font = None
        self.loadFont()
        self.loadImages()

    def loadImages(self) -> None:
        pieces = ["wP", "wR", "wN", "wB", "wQ", "wK", "bP", "bR", "bN", "bB", "bQ", "bK"]
        for piece in pieces:
            image = pygame.transform.scale(pygame.image.load(f"assets/{piece}.png"), (SQ_SIZE - 10, SQ_SIZE - 10))
            self.images[piece] = image
    
    def loadFont(self) -> None:
        self.font = pygame.font.SysFont(FONT, 18, bold=True)

    def popState(self):
        self.state.pop()

    def pushState(self, state):
        self.state.append(state)

    def getActiveState(self):
        return self.state[-1]

    def gameLoop(self):
        while(True):
            activeState = self.getActiveState()
            if (activeState == None):
                continue
            
            activeState.update()

            self.window.fill("black")
            activeState.draw()
            pygame.display.flip()

if __name__ == "__main__":
    from states.playstate import PlayState
    from states.startstate import StartState

    game = Game()
    game.state = [StartState(game)]
    game.gameLoop()