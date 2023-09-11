"""
board.py: Define the chess board and its operations
"""

class Board():
    def __init__(self) -> None:
        pass
    
    def getCurrentState(self):
        """
        Get the current state of the board

        Args:
        None

        Returns:
        list: The current state of the board as a 8x8 array
        """
        return 
    
    def isEndState(self, state: list[list]) -> bool:
        """
        Check if the current state is the end state (A state is an end state if one of the kings is removed)

        Args:
        state (list[list]): A state of the board as a 8x8 array

        Returns:
        bool: True if the current state is the endstate, False otherwise
        """
        return
    
    def getNeighborState(self, state:list[list]) -> list[list[list]]:
        """
        Generate all neighboring states of a state

        Args:
        state (list[list]): A state of the board as a 8x8 array

        Returns:
        list[list[list]]: A list of neighboring states
        """
        return 
    
    def evaluateState(self, state: list[list]) -> int:
        """
        Evaluate a states of the board (Total value of all the white pieces - Total value of all the black pieces)

        Args: 
        state (list[list]): A state of the board as a 8x8 array

        Returns:
        int: The value of that state
        """
        return
    
    def getNextMove(self, depthLimit: int) -> str:
        """
        Find the best possible move for the current state of the board using Minimax algorithm with Alpha-beta pruning

        Args:
        depthLimit (int): The depth limit for the search tree

        Returns:
        String: The best possible move for the current state of the board (e.g. "e2e4")
        """
        return
    
    def movePiece(self, moveString: str) -> None:
        """
        Perform a move on the board and update all the board attributes

        Args:
        moveString (String): A chess move as a String (e.g. "e2e4")

        Returns:
        None
        """
        return
    
