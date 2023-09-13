"""
game.py: Define the game contain board and pieces.
"""
import pygame
from board import Board
from pieces import Piece

WINDOWWIDTH = 1080
WINDOWHEIGHT = 720
title = "ChessX"
IMAGES = {}

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.start_game = False
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["__", "__", "__", "__", "__", "__", "__", "__"],
            ["__", "__", "__", "__", "__", "__", "__", "__"],
            ["__", "__", "__", "__", "__", "__", "__", "__"],
            ["__", "__", "__", "__", "__", "__", "__", "__"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]
        self.loadImages()


    def loadImages(self):
        pieces = ["wP", "wR", "wN", "wB", "wQ", "wK", "bP", "bR", "bN", "bB", "bQ", "bK"]
        for piece in pieces:
            IMAGES[piece] = pygame.transform.scale(pygame.image.load(piece + ".png"), (80, 80))

    def run(self):
        self.playing = True
        while self.playing:
            # self.clock.tick(FPS)
            self.events()
            # self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)

    def draw(self):
        self.window.fill("green")
        self.draw_board()
        pygame.display.flip()

    def draw_board(self):
        for i in range(8):
            for j in range(8):
                piece = self.board[i][j]
                if piece != "__":
                    self.window.blit(IMAGES[piece], pygame.Rect(j*80, i*80, 80, 80))

game = Game()
while True:
    game.run()