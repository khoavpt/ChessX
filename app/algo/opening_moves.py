import random
# '': [],
openingMovesDatabase = {
    # Starting moves for white
    'bRbNbBbQbKbBbNbR/bPbPbPbPbPbPbPbP/8/8/8/8/wPwPwPwPwPwPwPwP/ b': ['e2e4','d2d4'],
    # White starts with e4
    'bRbNbBbQbKbBbNbR/bPbPbPbPbPbPbPbP/8/8/4wP3/8/wPwPwPwP1wPwPwP/ b': ['c7c5', 'e7e5'],
    # White starts with d4
    'bRbNbBbQbKbBbNbR/bPbPbPbPbPbPbPbP/8/8/3wP4/8/wPwPwP1wPwPwPwP/ b': ['g8f6','d7d5',],
    # w:e4 b:c5 
    'bRbNbBbQbKbBbNbR/bPbP1bPbPbPbPbP/8/2bP5/4wP3/8/wPwPwPwP1wPwPwP/ w':['g1f3','b1c3'],
    # w:e4 b:e5 
    'bRbNbBbQbKbBbNbR/bPbPbPbP1bPbPbP/8/4bP3/4wP3/8/wPwPwPwP1wPwPwP/ w': ['g1f3', 'f1c4'],
    # w:d4 b:Nf6 
    'bRbNbBbQbKbB1bR/bPbPbPbPbPbPbPbP/5bN2/8/3wP4/8/wPwPwP1wPwPwPwP/ w': ['c2c4','g1f3'],
    # w:d4 b:d5 
    'bRbNbBbQbKbBbNbR/bPbPbP1bPbPbPbP/8/3bP4/3wP4/8/wPwPwP1wPwPwPwP/ w': ['c2c4','c1g5'],
    # w:e4 b:c5 w:Nf3
    'bRbNbBbQbKbBbNbR/bPbP1bPbPbPbPbP/8/2bP5/4wP3/5wN2/wPwPwPwP1wPwPwP/ b': ['d7d6','b8c6',],
    # w:e4 b:c5 w:c3
    'bRbNbBbQbKbBbNbR/bPbP1bPbPbPbPbP/8/2bP5/4wP3/2wP5/wPwP1wP1wPwPwP/ b': ['g8f6', 'd7d5'],
    # w:e4 b:c5 w:Nc3
    'bRbNbBbQbKbBbNbR/bPbP1bPbPbPbPbP/8/2bP5/4wP3/2wN5/wPwPwPwP1wPwPwP/ b': ['b8c6','e7e6'],
    # w:e4 b:e5 w:Nf3
    'bRbNbBbQbKbBbNbR/bPbPbPbP1bPbPbP/8/4bP3/4wP3/5wN2/wPwPwPwP1wPwPwP/ b': ['b8c6','g8f6'],
    # w:e4 b:e5 w:Bc4
    'bRbNbBbQbKbBbNbR/bPbPbPbP1bPbPbP/8/4bP3/2wB1wP3/8/wPwPwPwP1wPwPwP/ b': ['b8c6','g8f6'],
    # w:d4 b:Nf6 w:c4
    'bRbNbBbQbKbB1bR/bPbPbPbPbPbPbPbP/5bN2/8/2wPwP4/8/wPwP2wPwPwPwP/ b': ['e7e6','g7g6'],
    # w:d4 b:Nf6 w:Nf3
    'bRbNbBbQbKbB1bR/bPbPbPbPbPbPbPbP/5bN2/8/3wP4/5wN2/wPwPwP1wPwPwPwP/ b': ['g7g6','e7e6'],
    # w:d4 b:Nf6 w:Nc3
    'bRbNbBbQbKbB1bR/bPbPbPbPbPbPbPbP/5bN2/8/3wP4/2wN5/wPwPwP1wPwPwPwP/ b': ['d7d5'],
    # w:d4 b:d5 w:Bg5
    'bRbNbBbQbKbBbNbR/bPbPbP1bPbPbPbP/8/3bP2wB1/3wP4/8/wPwPwP1wPwPwPwP/ b': ['h7h6','c7c6'],
    # w:d4 b:d5 w:Nc3
    'bRbNbBbQbKbBbNbR/bPbPbP1bPbPbPbP/8/3bP4/3wP4/2wN5/wPwPwP1wPwPwPwP/ b': ['g8f6', 'c8f5']
}

def notationToMove(moveString):
    """
    Convert a move notation (eg: 'e7e6') into a list of tuples: [source (tuple), destination (tuple)])

    Args:
    moveString(String): A string represent a chess move (eg: 'e7e6')

    Returns:
    list[tuple]: A move represented in this format: [source (tuple), destination (tuple)]
    """
    source_x = ord(moveString[0]) - ord('a')
    source_y = 7 - int(moveString[1]) + 1
    destination_x = ord(moveString[2]) - ord('a')
    destination_y = 7 - int(moveString[3]) + 1
    move = [(source_x, source_y), (destination_x, destination_y)]
    return move

def getOpeningMove(boardString):
    """
    Choose the best move for the opening phase

    Args:
    boardString(String): A state of the board as a string.

    Returns:
    list[tuple] or None: Return a move if the state of the board is in openingMovesDatabase, None otherwise 
    """
    if boardString in openingMovesDatabase:
        movesList = openingMovesDatabase[boardString]
        return notationToMove(random.choice(movesList))
    return None