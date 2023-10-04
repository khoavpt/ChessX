import pygame
from board import Board
from pieces02 import Piece
import ai

# Constants
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 640
WINDOW_TITLE = "ChessX"
SQ_SIZE = 80
ROWS = 8
COLS = 8
FPS = 30
WHITE = (255, 255, 255)
GRAY = (169, 169, 169)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
ALPHACOLS = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H'}

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption(WINDOW_TITLE)
        self.clock = pygame.time.Clock()
        self.board = Board(Piece.WHITE)
        self.font = pygame.font.SysFont('monospace', 18, bold=True)
        self.loadImages()
        self.selected = None
        self.lastMove = None
        self.highlights = []

    def loadImages(self):
            pieces = ["wP", "wR", "wN", "wB", "wQ", "wK", "bP", "bR", "bN", "bB", "bQ", "bK"]
            for piece in pieces:
                image = pygame.transform.scale(pygame.image.load(f"assets/{piece}.png"), (SQ_SIZE - 15, SQ_SIZE - 15))
                IMAGES[piece] = image

    def gameLoop(self):
        while True:
            self.drawBoardGame()
            self.drawPossibleMoves()
            self.drawSelectedPiece()    
            self.drawLastMove()
            self.drawPieces()

            if self.board.currentPlayer == Piece.BLACK:
                move = ai.getBestMove(self.board)
                pygame.time.delay(1000)
                self.move(move)
                print(self.board.toString())
                

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit(0)

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.board.currentPlayer == Piece.WHITE:
                        row = mouse_pos[0] // SQ_SIZE
                        col = mouse_pos[1] // SQ_SIZE
                        if not self.selected:
                            piece = self.board.getPieceAt((row, col))
                            if piece in self.board.listOfWhitePieces:
                                self.selected = piece        
                            
                        else:
                            selectedPiece = self.selected
                            possibleMoves = selectedPiece.getPossibleMoves(self.board)[0] + selectedPiece.getPossibleMoves(self.board)[1]
                            for move in possibleMoves:
                                if (row, col) == move[1]:
                                    move = [(self.selected.x, self.selected.y), (row, col)]
                                    self.move(move)
                                    print(self.board.toString())
                            self.selected = None
                                    

            pygame.display.flip()

    def move(self, move):
        self.lastMove = move
        self.board.movePiece(move)
        self.drawBoardGame()
        self.drawLastMove()
        self.drawPieces()

    def drawSelectedPiece(self):
        if self.selected:
            selectedPiece = self.selected
            pygame.draw.rect(self.window, pygame.Color("yellow"), pygame.Rect(selectedPiece.x*SQ_SIZE, selectedPiece.y*SQ_SIZE, SQ_SIZE, SQ_SIZE))

    def drawPieces(self):
        for piece in self.board.listOfWhitePieces:
            image = IMAGES[f"w{piece.pieceType}"]
            # Tính toán vị trí để đặt hình ảnh vào giữa ô vuông
            x = piece.x * SQ_SIZE + (SQ_SIZE - image.get_width()) // 2
            y = piece.y * SQ_SIZE + (SQ_SIZE - image.get_height()) // 2
            self.window.blit(IMAGES[f"w{piece.pieceType}"], pygame.Rect(x, y, SQ_SIZE, SQ_SIZE))

        for piece in self.board.listOfBlackPieces:
            image = IMAGES[f"b{piece.pieceType}"]
            # Tính toán vị trí để đặt hình ảnh vào giữa ô vuông
            x = piece.x * SQ_SIZE + (SQ_SIZE - image.get_width()) // 2
            y = piece.y * SQ_SIZE + (SQ_SIZE - image.get_height()) // 2
            self.window.blit(IMAGES[f"b{piece.pieceType}"], pygame.Rect(x, y, SQ_SIZE, SQ_SIZE))

    def drawPossibleMoves(self):
        if self.selected:
            piece = self.selected
            possibleMoves = piece.getPossibleMoves(self.board)[0]+ piece.getPossibleMoves(self.board)[1]
            for move in possibleMoves:
                destination = move[1]
                pygame.draw.rect(self.window, pygame.Color("red"), pygame.Rect(destination[0]*SQ_SIZE, destination[1]*SQ_SIZE, SQ_SIZE, SQ_SIZE))

    def drawLastMove(self):
        if self.lastMove:
            source = self.lastMove[0]
            destination = self.lastMove[1]

            for pos in [source, destination]:
                pygame.draw.rect(self.window, pygame.Color("yellow"), pygame.Rect(pos[0]*SQ_SIZE, pos[1]*SQ_SIZE, SQ_SIZE, SQ_SIZE))

    def drawBoardGame(self):
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    pygame.draw.rect(self.window, WHITE, pygame.Rect(col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                else:
                    pygame.draw.rect(self.window, GRAY, pygame.Rect(col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))

                # row coordinates
                if col == 0:
                    # color
                    color = GRAY if row % 2 == 0 else WHITE
                    # label
                    lbl = self.font.render(str(ROWS-row), 1, color)
                    lbl_pos = (4, 4 + row * SQ_SIZE)
                    # blit
                    self.window.blit(lbl, lbl_pos)

                # col coordinates
                if row == 7:
                    # color
                    color = GRAY if (row + col) % 2 == 0 else WHITE
                    # label
                    lbl = self.font.render(ALPHACOLS[col], 1, color)
                    lbl_pos = (col * SQ_SIZE + SQ_SIZE - 15, WINDOW_HEIGHT - 18)
                    # blit
                    self.window.blit(lbl, lbl_pos)

if __name__ == "__main__":
    IMAGES = {}
    game = Game()
    game.gameLoop()