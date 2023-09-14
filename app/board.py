"""
board.py: Define the chess board and its operations
"""
from pieces import *

class Board():
    WHITE = 0
    BLACK = 1
    DEPTH_LIMIT = 10

    def __init__(self, currentPlayer) -> None:
        
        # TODO

        self.currentPlayer = currentPlayer
        self.listOfWhitePieces = []
        self.listOfBlackPieces = []  
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

        boardCopy.board = [[piece for piece in row] for row in self.board]

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
            if piece.row == coordinate[0] & piece.column == coordinate[1]:
                return piece
        for piece in self.listOfBlackPieces:
            if piece.row == coordinate[0] & piece.column == coordinate[1]:
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
            return False
        return True
    
    
    def movePiece(self, move: str) -> None:
        """
        Perform a move on the board and update all the board attributes

        Args:
        move (str): A chess move as a String (e.g. "e2e4")

        Returns:
        None
        """
        source = move[0]
        destination = move[1]

        piece = self.getPieceAt(source)
        piece.moveTo(destination)

        pieceAtDestination = self.getPieceAt(destination)

        # If there's a piece at the destination, remove it.
        if pieceAtDestination != None:
            if piece.color == Board.WHITE & pieceAtDestination.color == Board.BLACK:
                self.listOfBlackPieces.remove(pieceAtDestination)
            else:
                self.listOfWhitePieces.remove(pieceAtDestination)

        # Switch turn after the move is made.
        if (self.currentPlayer == Board.WHITE):
            self.currentPlayer = Board.BLACK
        else:
            self.currentPlayer = Board.WHITE

        return
