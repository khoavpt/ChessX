from game import Game
from states.state import State
from states.endstate import EndState
from constants import *
import pygame
from algo.pieces import Piece
from algo.board import Board
from algo import ai

class PlayState(State):
    def __init__(self, game: Game) -> None:
        super().__init__(game)
        self.board = Board(Piece.WHITE, game.playerColor)
        self.selected = None
        self.lastMove = None
        self.font = pygame.font.SysFont(FONT, 18, bold=True)

    def update(self) -> None:
        if self.board.isOver() == 1:
            if self.game.playerColor == Piece.WHITE:
                self.game.pushState(EndState(self.game, 'h'))
            else:
                self.game.pushState(EndState(self.game, 'a'))
        elif self.board.isOver() == -1:
            if self.game.playerColor == Piece.WHITE:
                self.game.pushState(EndState(self.game, 'a'))
            else:
                self.game.pushState(EndState(self.game, 'h'))


        if self.board.currentPlayer != self.game.playerColor:
            move = ai.getBestMove(self.board)
            self.move(move)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.board = Board(Piece.WHITE)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.board.currentPlayer == self.game.playerColor:
                    row = mouse_pos[0] // SQ_SIZE
                    col = mouse_pos[1] // SQ_SIZE
                    if self.game.playerColor == Piece.BLACK:
                        row = 7 - row
                        col = 7 - col
                    if not self.selected:
                        piece = self.board.getPieceAt((row, col))
                        if piece is not None:
                            if piece.color == self.game.playerColor:
                                self.selected = piece        
                        
                    else:
                        selectedPiece = self.selected
                        possibleMoves = selectedPiece.getPossibleMoves(self.board)[0] + selectedPiece.getPossibleMoves(self.board)[1]
                        for move in possibleMoves:
                            if (row, col) == move[1]:
                                move = [(self.selected.x, self.selected.y), (row, col)]
                                self.move(move)
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

            posX = selectedPiece.x
            posY = selectedPiece.y
            if self.game.playerColor == Piece.BLACK:
                posX = 7 - posX
                posY = 7 - posY
            pygame.draw.rect(self.game.window, pygame.Color(color), pygame.Rect(posX*SQ_SIZE, posY*SQ_SIZE, SQ_SIZE, SQ_SIZE))

    def drawPieces(self):
        for piece in self.board.listOfWhitePieces:
            image = self.game.images[f"w{piece.pieceType}"]

            # Tính toán vị trí để đặt hình ảnh vào giữa ô vuông
            if self.game.playerColor == Piece.WHITE:
                x = piece.x * SQ_SIZE + (SQ_SIZE - image.get_width()) // 2
                y = piece.y * SQ_SIZE + (SQ_SIZE - image.get_height()) // 2
            else:
                x = (7-piece.x) * SQ_SIZE + (SQ_SIZE - image.get_width()) // 2
                y = (7-piece.y) * SQ_SIZE + (SQ_SIZE - image.get_height()) // 2
            
            self.game.window.blit(self.game.images[f"w{piece.pieceType}"], pygame.Rect(x, y, SQ_SIZE, SQ_SIZE))

        for piece in self.board.listOfBlackPieces:
            image = self.game.images[f"b{piece.pieceType}"]
            # Tính toán vị trí để đặt hình ảnh vào giữa ô vuông
            if self.game.playerColor == Piece.WHITE:
                x = piece.x * SQ_SIZE + (SQ_SIZE - image.get_width()) // 2
                y = piece.y * SQ_SIZE + (SQ_SIZE - image.get_height()) // 2
            else:
                x = (7-piece.x) * SQ_SIZE + (SQ_SIZE - image.get_width()) // 2
                y = (7-piece.y) * SQ_SIZE + (SQ_SIZE - image.get_height()) // 2
            self.game.window.blit(self.game.images[f"b{piece.pieceType}"], pygame.Rect(x, y, SQ_SIZE, SQ_SIZE))

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

                posX = destination[0]
                posY = destination[1]
                if self.game.playerColor == Piece.BLACK:
                    posX = 7 - posX
                    posY = 7 - posY
                pygame.draw.rect(self.game.window, color, pygame.Rect(posX*SQ_SIZE, posY*SQ_SIZE, SQ_SIZE, SQ_SIZE))

            nonCaptureMoves = piece.getPossibleMoves(self.board)[1]
            for move in nonCaptureMoves:
                destination = move[1]
                color = ()
                if (destination[0] + destination[1]) % 2 == 0:
                    color = (136, 240, 252)
                else:
                    color = (98, 202, 215)

                posX = destination[0]
                posY = destination[1]
                if self.game.playerColor == Piece.BLACK:
                    posX = 7 - posX
                    posY = 7 - posY
                pygame.draw.rect(self.game.window, color, pygame.Rect(posX*SQ_SIZE, posY*SQ_SIZE, SQ_SIZE, SQ_SIZE))

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

                posX = pos[0]
                posY = pos[1]
                if self.game.playerColor == Piece.BLACK:
                    posX = 7 - posX
                    posY = 7 - posY
                pygame.draw.rect(self.game.window, color, pygame.Rect(posX*SQ_SIZE, posY*SQ_SIZE, SQ_SIZE, SQ_SIZE))

    def drawBoardGame(self):
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    pygame.draw.rect(self.game.window, WHITE, pygame.Rect(col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                else:
                    pygame.draw.rect(self.game.window, GRAY, pygame.Rect(col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))

                # row coordinates
                if col == 0:
                    # color
                    color = GRAY if row % 2 == 0 else WHITE
                    # label
                    if self.game.playerColor == Piece.WHITE:
                        lbl = self.font.render(str(ROWS-row), 1, color)
                    else:
                        lbl = self.font.render(str(row + 1), 1, color)
                    lbl_pos = (4, 4 + row * SQ_SIZE)
                    # blit
                    self.game.window.blit(lbl, lbl_pos)

                # col coordinates
                if row == 7:
                    # color
                    color = GRAY if (row + col) % 2 == 0 else WHITE
                    # label
                    if self.game.playerColor == Piece.WHITE:
                        lbl = self.font.render(ALPHACOLS[col], 1, color)
                    else:
                        lbl = self.font.render(ALPHACOLS[7 - col], 1, color)
                    lbl_pos = (col * SQ_SIZE + SQ_SIZE - 15, WINDOW_HEIGHT - 18)
                    # blit
                    self.game.window.blit(lbl, lbl_pos)