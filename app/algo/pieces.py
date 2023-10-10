from abc import abstractmethod

class Piece:
    WHITE = 0
    BLACK = 1
    def __init__(self, x, y, color, pieceType, value):       
        self.x = x
        self.y = y
        self.pieceType = pieceType
        self.color = color
        self.value = value

    def moveTo(self, coordinate:tuple)->None:
        """
        Move a piece to the given coordinate. 

        Args: 
        coordinate (tuple): A coordinate on the chess board as a tuple.

        Returns:
        None
        """
        self.x = coordinate[0]
        self.y = coordinate[1]

    def getPossibleDiagonalMoves(self, board):
        moves = []

        for dx, dy in [(1, 1), (1, -1), (-1, -1), (-1, 1)]:
            for i in range(1, 8):
                new_x, new_y = self.x + i * dx, self.y + i * dy
                move = [(self.x, self.y), (new_x, new_y)]
                piece = board.getPieceAt((new_x, new_y))
                moves.append(move)

                if piece is not None:
                    break

        return self.getValidMovesFromList(moves, board)                                        

    def getPossibleHorizontalMoves(self, board):
        moves = []

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            for i in range(1, 8):
                new_x, new_y = self.x + i * dx, self.y + i * dy
                move = [(self.x, self.y), (new_x, new_y)]
                piece = board.getPieceAt((new_x, new_y))
                moves.append(move)

                if piece is not None:
                    break

        return self.getValidMovesFromList(moves, board)

    
    def getValidMovesFromList(self, l, board):
        captureMoves = []
        noncaptureMoves = []
        for move in l:
            if 7>= move[1][0] >= 0 and 7>= move[1][1] >= 0:
                destinationPiece = board.getPieceAt(move[1])
                if destinationPiece == None:
                    noncaptureMoves.append(move)
                elif destinationPiece.color != self.color:
                    captureMoves.append(move)
        return captureMoves, noncaptureMoves
    
    def toString(self):
        colorString = "w" if self.color == Piece.WHITE else "b"
        return colorString + self.pieceType
    
    @abstractmethod
    def getPossibleMoves(self, board):
        pass

class Rook(Piece):
    PIECE_TYPE = "R"
    VALUE = 50
    def __init__(self, x, y, color):
        super(Rook, self).__init__(x, y, color, Rook.PIECE_TYPE, Rook.VALUE)
    def getPossibleMoves(self, board):
        return self.getPossibleHorizontalMoves(board)
    def copy(self):
        return Rook(self.x, self.y, self.color)
    
class Knight(Piece):
    PIECE_TYPE = "N"
    VALUE = 30
    def __init__(self, x, y, color):
        super(Knight, self).__init__(x, y, color, Knight.PIECE_TYPE, Knight.VALUE)
    def getPossibleMoves(self, board):
        movesList = [[(self.x, self.y), (self.x+2, self.y+1)], 
                     [(self.x, self.y), (self.x-1, self.y+2)], 
                     [(self.x, self.y), (self.x-2, self.y+1)], 
                     [(self.x, self.y), (self.x+1, self.y-2)],
                     [(self.x, self.y), (self.x+2, self.y-1)],
                     [(self.x, self.y), (self.x+1, self.y+2)],
                     [(self.x, self.y), (self.x-2, self.y-1)],
                     [(self.x, self.y), (self.x-1, self.y-2)]]
        return self.getValidMovesFromList(movesList, board)
    def copy(self):
        return Knight(self.x, self.y, self.color)
    
class Bishop(Piece):
    PIECE_TYPE = "B"
    VALUE = 30
    def __init__(self, x, y, color):
        super(Bishop, self).__init__(x, y, color, Bishop.PIECE_TYPE, Bishop.VALUE)
    def getPossibleMoves(self, board):
        return self.getPossibleDiagonalMoves(board)
    def copy(self):
        return Bishop(self.x, self.y, self.color)
    
class Queen(Piece):
    PIECE_TYPE = "Q"
    VALUE = 90
    def __init__(self, x, y, color):
        super(Queen, self).__init__(x, y, color, Queen.PIECE_TYPE, Queen.VALUE)
        
    def getPossibleMoves(self, board):
        diagonal_capture_moves, diagonal_noncapture_moves = self.getPossibleDiagonalMoves(board)
        horizontal_capture_moves, horizontal_noncapture_moves = self.getPossibleHorizontalMoves(board)

        capture_moves = diagonal_capture_moves + horizontal_capture_moves
        noncapture_moves = diagonal_noncapture_moves + horizontal_noncapture_moves

        return capture_moves, noncapture_moves

    def copy(self):
        return Queen(self.x, self.y, self.color)
    
class King(Piece):
    PIECE_TYPE = "K"
    VALUE = 900
    def __init__(self, x, y, color):
        super(King, self).__init__(x, y, color, King.PIECE_TYPE, King.VALUE)
    def getPossibleMoves(self, board):
        moves = [[(self.x, self.y), (self.x+1, self.y)],
                 [(self.x, self.y), (self.x+1, self.y+1)],
                 [(self.x, self.y), (self.x, self.y+1)],
                 [(self.x, self.y), (self.x-1, self.y+1)],
                 [(self.x, self.y), (self.x-1, self.y)],
                 [(self.x, self.y), (self.x-1, self.y-1)],
                 [(self.x, self.y), (self.x, self.y-1)],
                 [(self.x, self.y), (self.x+1, self.y-1)]]

        return self.getValidMovesFromList(moves, board)
        '''moves.append(self.get_castle_kingside_move())
        # moves.append(self.get_castle_queenside_move())
    
    # def get_castle_kingside_move(self, board):
        
    #     piece_in_corner = board.getPieceAt(self.x+3, self.y)
    #     if (piece_in_corner == 0 or piece_in_corner.piece_type != Rook.PIECE_TYPE):
    #         return 0

        
    #     if (piece_in_corner.color != self.color):
    #         return 0
        
        
    #     if (self.color == Piece.WHITE and board.white_king_moved):
    #         return 0
        
    #     if (self.color == Piece.BLACK and board.black_king_moved):
    #         return 0

        
    #     if (board.getPieceAt(self.x+1, self.y) != 0 or board.getPieceAt(self.x+2, self.y) != 0):
    #         return 0
        
    #     return Move(self.x, self.y, self.x+2, self.y)
    # #Nhập thành bên có hậu
    # def get_castle_queenside_move(self, board):
        
    #     piece_in_corner = board.getPieceAt(self.x-4, self.y)
    #     if (piece_in_corner == 0 or piece_in_corner.piece_type != Rook.PIECE_TYPE):
    #         return 0

        
    #     if (piece_in_corner.color != self.color):
    #         return 0
        
        
    #     if (self.color == Piece.WHITE and board.white_king_moved):
    #         return 0
        
    #     if (self.color == Piece.BLACK and board.black_king_moved):
    #         return 0

        
    #     if (board.getPieceAt(self.x-1, self.y) != 0 or board.getPieceAt(self.x-2, self.y) != 0 or board.getPieceAt(self.x-3, self.y) != 0):
    #         return 0
        
    #     return Move(self.x, self.y, self.x-2, self.y)'''


    def copy(self):
        return King(self.x, self.y, self.color)
    
class Pawn(Piece):
    PIECE_TYPE = "P"
    VALUE = 10
    def __init__(self, x, y, color):
        super(Pawn, self).__init__(x, y, color, Pawn.PIECE_TYPE, Pawn.VALUE)

    def isStartingPosition(self):
        if (self.color == Piece.BLACK):
            return self.y == 1
        else:
            return self.y == 8 - 2

    def getPossibleMoves(self, board):
        moves = []        
        direction = -1
        if (self.color == Piece.BLACK):
            direction = 1
        
        if (self.isStartingPosition() and board.getPieceAt((self.x, self.y+ direction)) == None and board.getPieceAt((self.x, self.y + direction*2)) == None):
            moves.append([(self.x, self.y), (self.x, self.y + direction * 2)])

        if (board.getPieceAt((self.x, self.y+direction)) == None):
            moves.append([(self.x, self.y), (self.x, self.y + direction)])

        piece = board.getPieceAt((self.x + 1, self.y + direction))
        if (piece != None and piece.color != self.color):
            moves.append([(self.x, self.y), (self.x + 1, self.y + direction)])

        piece = board.getPieceAt((self.x - 1, self.y + direction))
        if (piece != None and piece.color != self.color):
            moves.append([(self.x, self.y), (self.x - 1, self.y + direction)])

        return self.getValidMovesFromList(moves, board)

    def copy(self):
        return Pawn(self.x, self.y, self.color)
    
    
    
    
