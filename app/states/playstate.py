from states.state import State
from constants import *
import pygame
from algo.pieces import Piece
from algo.board import Board
from algo import ai

class PlayState(State):
    def __init__(self, window, board: Board, font, images) -> None:
        super().__init__(window)
        self.board = board
        self.font = font
        self.selected = None
        self.lastMove = None
        self.playerColor = Piece.WHITE
        self.IMAGES = images


    def update(self) -> None:
        if self.board.currentPlayer == Piece.BLACK:
            move = ai.getBestMove(self.board)
            self.move(move)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.__init__()

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
    
    def draw(self) -> None:
        self.drawBoardGame()
        self.drawSelectedPiece()    
        self.drawLastMove()
        self.drawPossibleMoves()
        self.drawPieces()
    
    def move(self, move):
        self.lastMove = move
        self.board.movePiece(move)
        self.drawBoardGame()
        self.drawLastMove()
        self.drawPieces()

    def drawSelectedPiece(self):
        if self.selected:
            selectedPiece = self.selected
            if (selectedPiece.x + selectedPiece.y) % 2 == 0:
                color = (244, 240, 173)
            else:
                color = (206, 202, 136)
            pygame.draw.rect(self.window, pygame.Color(color), pygame.Rect(selectedPiece.x*SQ_SIZE, selectedPiece.y*SQ_SIZE, SQ_SIZE, SQ_SIZE))

    def drawPieces(self):
        for piece in self.board.listOfWhitePieces:
            image = self.IMAGES[f"w{piece.pieceType}"]
            # Tính toán vị trí để đặt hình ảnh vào giữa ô vuông
            x = piece.x * SQ_SIZE + (SQ_SIZE - image.get_width()) // 2
            y = piece.y * SQ_SIZE + (SQ_SIZE - image.get_height()) // 2
            self.window.blit(self.IMAGES[f"w{piece.pieceType}"], pygame.Rect(x, y, SQ_SIZE, SQ_SIZE))

        for piece in self.board.listOfBlackPieces:
            image = self.IMAGES[f"b{piece.pieceType}"]
            # Tính toán vị trí để đặt hình ảnh vào giữa ô vuông
            x = piece.x * SQ_SIZE + (SQ_SIZE - image.get_width()) // 2
            y = piece.y * SQ_SIZE + (SQ_SIZE - image.get_height()) // 2
            self.window.blit(self.IMAGES[f"b{piece.pieceType}"], pygame.Rect(x, y, SQ_SIZE, SQ_SIZE))

    def drawPossibleMoves(self):
        if self.selected:
            piece = self.selected
            captureMoves = piece.getPossibleMoves(self.board)[0]
            for move in captureMoves:
                destination = move[1]
                color = ()
                if (destination[0] + destination[1]) % 2 == 0:
                    color = (255, 128, 128)
                else:
                    color = (218, 90, 90)
                pygame.draw.rect(self.window, color, pygame.Rect(destination[0]*SQ_SIZE, destination[1]*SQ_SIZE, SQ_SIZE, SQ_SIZE))

            nonCaptureMoves = piece.getPossibleMoves(self.board)[1]
            for move in nonCaptureMoves:
                destination = move[1]
                color = ()
                if (destination[0] + destination[1]) % 2 == 0:
                    color = (136, 240, 252)
                else:
                    color = (98, 202, 215)
                pygame.draw.rect(self.window, color, pygame.Rect(destination[0]*SQ_SIZE, destination[1]*SQ_SIZE, SQ_SIZE, SQ_SIZE))

    def drawLastMove(self):
        if self.lastMove:
            source = self.lastMove[0]
            destination = self.lastMove[1]

            for pos in [source, destination]:
                color = ()
                if (pos[0] + pos[1]) % 2 == 0:
                    color = (244, 240, 173)
                else:
                    color = (206, 202, 136)
                pygame.draw.rect(self.window, color, pygame.Rect(pos[0]*SQ_SIZE, pos[1]*SQ_SIZE, SQ_SIZE, SQ_SIZE))

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