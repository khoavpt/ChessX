import pygame
from algo.board import Board
from algo.pieces import Piece
from states.state import State
from states.playstate import PlayState
import algo.ai as ai
from constants import *

class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption(WINDOW_TITLE)
        self.board = Board(Piece.WHITE)
        self.font = pygame.font.SysFont(FONT, 18, bold=True)
        self.IMAGES = {}
        self.loadImages()
        self.selected = None
        self.lastMove = None
        self.playerColor = Piece.WHITE
        self.state = [PlayState(self.window, self.board, self.font, self.IMAGES)]

    def popState(self):
        self.state.pop()

    def pushState(self, state: State):
        self.state.append(state)

    def getActiveState(self):
        return self.state[-1]

    def loadImages(self):
            pieces = ["wP", "wR", "wN", "wB", "wQ", "wK", "bP", "bR", "bN", "bB", "bQ", "bK"]
            for piece in pieces:
                image = pygame.transform.scale(pygame.image.load(f"assets/{piece}.png"), (SQ_SIZE - 15, SQ_SIZE - 15))
                self.IMAGES[piece] = image

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
    game = Game()
    game.gameLoop()