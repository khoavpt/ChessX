"""
board.py: Define the chess board and its operations
"""

class Board():
    WHITE = 0
    BLACK = 1
    DEPTH_LIMIT = 10

    def __init__(self, currentPlayer) -> None:
        
        # TODO

        self.currentPlayer = currentPlayer
        self.listOfWhitePieces = []
        self.listOfBlackPieces = []
        self.board = []
    
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
    
    def isEndState(self) -> bool:
        """
        Check if the current state is the end state (A state is an end state if one of the kings is removed).

        Args:
        None

        Returns:
        bool: True if the current state is the endstate, False otherwise.
        """
        # TODO
        return False
    
    
    def movePiece(self, move: str) -> None:
        """
        Perform a move on the board and update all the board attributes

        Args:
        move (str): A chess move as a String (e.g. "e2e4")

        Returns:
        None
        """
        # TODO

        # Switch turn after the move is made.
        if (self.currentPlayer == Board.WHITE):
            self.currentPlayer = Board.BLACK
        else:
            self.currentPlayer = Board.WHITE

        return
