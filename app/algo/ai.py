"""
ai.py: Implement the AI logic using minimax and alpha-beta pruning.
"""

from algo.board import *
from algo.pieces import Piece
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

def getValidMoves(board: Board) -> list[list[tuple]]:
    """
    Generate all the possible moves from the given board.

    Args:
    board (Board): A chess board as a Board object.

    Returns:
    list[list[tuple]]: List of all the valid moves.
    """
    orderedMoves = []
    if board.currentPlayer == Piece.WHITE:
        for piece in board.listOfWhitePieces:
            piecePossibleMoves = piece.getPossibleMoves(board)
            orderedMoves = piecePossibleMoves[0] + orderedMoves
            orderedMoves += piecePossibleMoves[1]
    else:
        for piece in board.listOfBlackPieces:
            piecePossibleMoves = piece.getPossibleMoves(board)
            orderedMoves = piecePossibleMoves[0] + orderedMoves
            orderedMoves += piecePossibleMoves[1]

    return orderedMoves


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

def minimax(board, depth, alpha, beta):
   if depth == 0 or board.isOver() != 0:
       return None, evaluateBoard(board)

   if board.currentPlayer == Piece.WHITE:
       max_val = -math.inf
       for move in getValidMoves(board=board):
           min_val = minimax(getResultBoard(board, move=move), depth - 1, alpha, beta)[1]
           if min_val > max_val:
               max_val = min_val
               best_move = move
           alpha = max(alpha, min_val)
           if beta <= alpha:
               break
       return best_move, max_val
   else:
       min_val = math.inf
       for move in getValidMoves(board=board):
           max_val = minimax(getResultBoard(board, move=move), depth - 1, alpha, beta)[1]
           if max_val < min_val:
               min_val = max_val
               best_move = move
           beta = min(beta, max_val)
           if beta <= alpha:
               break
       return best_move, min_val
   
def getBestMove(board: Board):
    """
    Find the best possible move from the given board.

    Args:
    board (Board): A chess board as a Board object.

    Returns:
    list(tuple): The best possible move for the given board (A move is represented in this format: [source (tuple), destination (tuple)]).
    """
    # If board is still in the opening phase, search for the best move in the database.
    if board.isInOpeningPhase:
        openingMove = getOpeningMove(board.toString())
        if openingMove != None:
            return openingMove
        else:
            board.isInOpeningPhase = False

    # Else, find the best move using Minimax algorithm with Alpha-beta pruning
    return minimax(board, depth=Board.DEPTH_LIMIT, alpha = -math.inf, beta = math.inf)[0]