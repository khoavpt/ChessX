"""
game.py: Define the game contain board and pieces.
"""
import pygame
from board import Board
from pieces import Piece

WINDOWWIDTH = 640
WINDOWHEIGHT = 640
title = "ChessX"
IMAGES = {}

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.start_game = False
        self.board = Board(Board.WHITE)
        self.loadImages()
        self.is_selected = None


    def loadImages(self):
        pieces = ["wP", "wR", "wN", "wB", "wQ", "wK", "bP", "bR", "bN", "bB", "bQ", "bK"]
        for piece in pieces:
            IMAGES[piece] = pygame.transform.scale(pygame.image.load("assets/" + piece + ".png"), (80, 80))

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(20)
            self.events()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos =  pygame.mouse.get_pos()
                self.handleClick(mouse_pos[1]//80, mouse_pos[0]//80)

    def handleClick(self, row, col):
        if self.board.currentPlayer == Board.WHITE:
            if (self.is_selected == None):
                if(self.board.getPieceAt(tuple(row, col)) in self.board.listOfWhitePieces):
                    self.is_selected = (row, col)
            elif (self.is_selected == (row, col)):
                self.is_selected == (-1, -1)
            else:
                self.move((row, col))
                self.is_selected = (-1, -1)

    def move(self, after):
        move = [self.is_selected, after]
        self.board.movePiece(move)

    def draw(self):
        self.window.fill("black")
        self.draw_board()
        self.draw_pieces()
        pygame.display.flip()

    def draw_pieces(self):
        for piece in self.board.listOfWhitePieces:
            self.window.blit(IMAGES[piece.name], pygame.Rect(piece.x*80, piece.y*80, 80, 80))
        for piece in self.board.listOfBlackPieces:
            self.window.blit(IMAGES[piece.name], pygame.Rect(piece.x*80, piece.y*80, 80, 80))

    def draw_board(self):
        for i in range(8):
            for j in range(8):
                if ((i+j) % 2 == 0):
                    pygame.draw.rect(self.window, pygame.Color("white"), pygame.Rect(j*80, i*80, 80, 80))
                else:
                    pygame.draw.rect(self.window, pygame.Color("gray"), pygame.Rect(j*80, i*80, 80, 80))


game = Game()
while True:
    game.run()