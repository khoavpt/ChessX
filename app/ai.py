"""
ai.py: Implement the AI logic using minimax and alpha-beta pruning.
"""

from board import Board
import math

def evaluateBoard(board: Board) -> int:
    """
    Evaluate a board (Total value of all the white pieces - Total value of all the black pieces)

    Args:
    board (Board): A chess board as a Board object.

    Returns:
    int: The evaluation score of the board.
    """
    boardScore = 0

    for piece in board.listOfWhitePieces:
        boardScore += piece.value

    for piece in board.listOfBlackPieces:
        boardScore -= piece.value

    return boardScore

def isValid(board: Board, move: str) -> bool:
    """
    Check if a move is valid or not.

    Args:
    board (Board): A chess board as a Board object.
    move (list[tuple]): The move to be checked (A move is represented in this format: [source (tuple), destination (tuple)])

    Returns:
    True if a move is valid, False otherwise.
    """
    source = move[0]
    destination = move[1]

    # A move is invalid if: The piece at the source position is not the same color as the current player OR the destination is already occupied with pieces of the same side as the curent player
    if board.getPieceAt(source).color != board.currentPlayer or board.getPieceAt(destination).color == board.currentPlayer:
        return False
    return True

def getValidMoves(board: Board) -> list[str]:
    """
    Generate all the possible moves from the given board.

    Args:
    board (Board): A chess board as a Board object.

    Returns:
    list[list[tuple]]: List of all the valid moves.
    """
    if board.currentPlayer == Board.WHITE:
        valid_moves = [move for piece in board.listOfWhitePieces for move in piece.getPossibleMoves() if isValid(board, move)]
    else:
        valid_moves = [move for piece in board.listOfBlackPieces for move in piece.getPossibleMoves() if isValid(board, move)]

    return valid_moves

def getResultBoard(board:Board, move):
    """
    Get the resulting board after a move is made.

    Args:
    board (Board): The current board.
    move (list[tuple]): The move to be checked (A move is represented in this format: [source (tuple), destination (tuple)])

    Returns:
    Board: The resulting board after the move.
    """
    resultBoard = board.copy()
    resultBoard.movePiece(move)
    return resultBoard


def getMaxValueAndMove(board: Board, currentDepth):
    if board.isEndState() or currentDepth == Board.DEPTH_LIMIT:
        return evaluateBoard(board=board)

    moves = getValidMoves(board=board)
    max = -math.inf
    play = moves[0]

    for move in moves:
        min = getMinValueAndMove(getResultBoard(board, move=move), currentDepth+1)[0]
        if min > max:
            max = min
            play = move

    return (max, play)


def getMinValueAndMove(board: Board, currentDepth):
    if board.isEndState() or currentDepth == Board.DEPTH_LIMIT:
        return evaluateBoard(board=board)

    moves = getValidMoves(board=board)
    min = math.inf
    play = moves[0]

    for move in moves:
        max = getMaxValueAndMove(getResultBoard(board, move=move), currentDepth+1)[0]
        if max < min:
            min = max
            play = move

    return (min, play)

def getBestMove(board: Board):
    """
    Find the best possible move from the given board using Minimax algorithm with Alpha-beta pruning

    Args:
    board (Board): A chess board as a Board object.

    Returns:
    list(tuple): The best possible move for the given board (A move is represented in this format: [source (tuple), destination (tuple)]).
    """
    
    if (board.currentPlayer == Board.WHITE):
        return getMaxValueAndMove(board=board, currentDepth=0)[1]
    else:
        return getMinValueAndMove(board=board, currentDepth=0)[1]