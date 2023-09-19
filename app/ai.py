"""
ai.py: Implement the AI logic using minimax and alpha-beta pruning.
"""

from board import Board
from pieces02 import Piece
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

# def isValid(board: Board, move: str) -> bool:
#     """
#     Check if a move is valid or not.

#     Args:
#     board (Board): A chess board as a Board object.
#     move (list[tuple]): The move to be checked (A move is represented in this format: [source (tuple), destination (tuple)])

#     Returns:
#     True if a move is valid, False otherwise.
#     """
#     source = move[0]
#     destination = move[1]

#     # Check if the source position is occupied by a piece.
#     source_piece = board.getPieceAt(source)
#     if source_piece is None:
#         return False

#     # Check if the destination position is empty or occupied by an enemy piece.
#     destination_piece = board.getPieceAt(destination)
#     if destination_piece is not None and destination_piece.color == source_piece.color:
#         return False

def getValidMoves(board: Board) -> list[list[tuple]]:
    """
    Generate all the possible moves from the given board.

    Args:
    board (Board): A chess board as a Board object.

    Returns:
    list[list[tuple]]: List of all the valid moves.
    """
    if board.currentPlayer == Piece.WHITE:
        valid_moves = [move for piece in board.listOfWhitePieces for move in piece.getPossibleMoves(board)]
    else:
        valid_moves = [move for piece in board.listOfBlackPieces for move in piece.getPossibleMoves(board)]

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

# def getMaxValueAndMove(board: Board, currentDepth, alpha_beta):
#     alpha, beta = alpha_beta
#     if board.isOver() or currentDepth == Board.DEPTH_LIMIT:
#         return (evaluateBoard(board=board), None)

#     moves = getValidMoves(board=board)
#     max_val = -math.inf
#     play = moves[0]

#     for move in moves:
#         min_val = getMinValueAndMove(getResultBoard(board, move=move), currentDepth+1, alpha_beta)[0]
#         if min_val > max_val:
#             max_val = min_val
#             play = move
#         alpha = max(alpha, max_val)
#         if beta <= alpha:
#             break

#     alpha_beta[0] = alpha
#     return (max_val, play)

# def getMinValueAndMove(board: Board, currentDepth, alpha_beta):
#     alpha, beta = alpha_beta
#     if board.isOver() or currentDepth == Board.DEPTH_LIMIT:
#         return (evaluateBoard(board=board), None)

#     moves = getValidMoves(board=board)
#     min_val = math.inf
#     play = moves[0]

#     for move in moves:
#         max_val = getMaxValueAndMove(getResultBoard(board, move=move), currentDepth+1, alpha_beta)[0]
#         if max_val < min_val:
#             min_val = max_val
#             play = move
#         beta = min(beta, min_val)
#         if beta <= alpha:
#             break

#     alpha_beta[1] = beta
#     return (min_val, play)

def minimax(board, depth, alpha, beta):
   if depth == 0 or board.isOver():
       return None, evaluateBoard(board)

   if board.currentPlayer == Piece.WHITE:
       max_val = -math.inf
       for move in getValidMoves(board=board):
           min_val = minimax(getResultBoard(board, move=move), depth - 1, alpha, beta)[1]
           if min_val >= max_val:
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
           if max_val <= min_val:
               min_val = max_val
               best_move = move
           beta = min(beta, max_val)
           if beta <= alpha:
               break
       return best_move, min_val
   
def getBestMove(board: Board):
    """
    Find the best possible move from the given board using Minimax algorithm with Alpha-beta pruning

    Args:
    board (Board): A chess board as a Board object.

    Returns:
    list(tuple): The best possible move for the given board (A move is represented in this format: [source (tuple), destination (tuple)]).
    """

    return minimax(board, depth=Board.DEPTH_LIMIT, alpha = -math.inf, beta = math.inf)[0]