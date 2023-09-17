"""
board.py: Define the chess board and its operations
"""
from pieces02 import *

class Board():
    DEPTH_LIMIT = 8

    def __init__(self, currentPlayer) -> None:
        
        # TODO

        self.currentPlayer = currentPlayer

        # Initialize pieces
        self.listOfWhitePieces = [Rook(x=7, y=7, color=Piece.WHITE),
                                  Rook(x=0, y=7, color=Piece.WHITE),
                                  Knight(x=1, y=7, color=Piece.WHITE),
                                  Knight(x=6, y=7, color=Piece.WHITE),
                                  Bishop(x=2, y=7, color=Piece.WHITE),
                                  Bishop(x=5, y=7, color=Piece.WHITE),
                                  Queen(x=3, y=7, color=Piece.WHITE),
                                  King(x=4, y=7, color=Piece.WHITE)]
                                

        self.listOfBlackPieces = [Rook(x=0, y=0, color=Piece.BLACK),
                                  Rook(x=7, y=0, color=Piece.BLACK),
                                  Knight(x=1, y=0, color=Piece.BLACK),
                                  Knight(x=6, y=0, color=Piece.BLACK),
                                  Bishop(x=2, y=0, color=Piece.BLACK),
                                  Bishop(x=5, y=0, color=Piece.BLACK),
                                  Queen(x=3, y=0, color=Piece.BLACK),
                                  King(x=4, y=0, color=Piece.BLACK)]

        for i in range(8):
            self.listOfWhitePieces.append(Pawn(i, 6, Piece.WHITE))
            self.listOfBlackPieces.append(Pawn(i, 1, Piece.BLACK))

    def copy(self):
        """
        Create a copy of the current board.

        Args:
        None

        Returns:
        Board: A copy of the current board.
        """

        boardCopy = Board(currentPlayer=self.currentPlayer)

        boardCopy.listOfWhitePieces = [piece.copy() for piece in self.listOfWhitePieces]
        boardCopy.listOfBlackPieces = [piece.copy() for piece in self.listOfBlackPieces]

        # boardCopy.board = [[piece for piece in row] for row in self.board]

        return boardCopy
    
    def getPieceAt(self, coordinate: tuple) -> Piece:
        """
        Return a chess piece at the given coodinate

        Args:
        coodinate (tuple): A coodinate on the chess board as a tuple (row, column).

        Returns:
        Piece: If there exist a piece on the given coordinate, return it. Otherwise return None
        """
        for piece in self.listOfWhitePieces:
            if piece.x == coordinate[0] and piece.y == coordinate[1]:
                return piece
        for piece in self.listOfBlackPieces:
            if piece.x == coordinate[0] and piece.y == coordinate[1]:
                return piece
        return None

    def isOver(self) -> bool:
        """
        Check if the current state of the board is the end state (A state is an end state if one of the kings is removed).

        Args:
        None

        Returns:
        bool: True if the current state is the endstate, False otherwise.
        """
        kingsCount = 0
        for piece in self.listOfWhitePieces:
            if type(piece) == King:
                kingsCount += 1
        
        for piece in self.listOfBlackPieces:
            if type(piece) == King:
                kingsCount += 1

        if kingsCount != 2:
            return True
        return False
    
    
    def movePiece(self, move: list[tuple]) -> None:
        """
        Perform a move on the board and update all the board attributes

        Args:
        move (list[tuple]): The move to be checked (A move is represented in this format: [source (tuple), destination (tuple)])

        Returns:
        None
        """
        source = move[0]
        destination = move[1]

        piece = self.getPieceAt(source)
        pieceAtDestination = self.getPieceAt(destination)
        piece.moveTo(destination)

        # If there's a different colored piece at the destination, remove it.
        if pieceAtDestination != None:
            if piece.color == Piece.WHITE and pieceAtDestination.color == Piece.BLACK:
                self.listOfBlackPieces.remove(pieceAtDestination)
            else:
                self.listOfWhitePieces.remove(pieceAtDestination)

        # Switch turn after the move is made.
        if (self.currentPlayer == Piece.WHITE):
            self.currentPlayer = Piece.BLACK
        else:
            self.currentPlayer = Piece.WHITE

        return
