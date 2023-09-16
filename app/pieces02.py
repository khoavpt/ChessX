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

    def getPossibleDiagonalMoves(self):
        moves = []
        for i in range(1, 8):
            moves.append([(self.x, self.y), (self.x + i, self.y + i)])
            moves.append([(self.x, self.y), (self.x + i, self.y - i)])
            moves.append([(self.x, self.y), (self.x - i, self.y - i)])
            moves.append([(self.x, self.y), (self.x - i, self.y + i)])      
        return self.removeNullFromList(moves)
    
    def getPossibleHorizontalMoves(self): 
        moves = []        
        for i in range(1, 8 - self.x):            
            moves.append([(self.x, self.y), (self.x+i, self.y)])                    
        for i in range(1, self.x + 1):            
            moves.append([(self.x, self.y), (self.x-i, self.y)])    
        for i in range(1, 8 - self.y):
            moves.append([(self.x, self.y), (self.x, self.y+i)])        
        for i in range(1, self.y + 1):           
            moves.append([(self.x, self.y), (self.x, self.y-i)])           
        return self.removeNullFromList(moves)
    
    def removeNullFromList(self, l):
        return [move for move in l if move != 0]
    
    def toString(self):
        colorString = "w" if self.color == Piece.WHITE else "b"
        return colorString + self.pieceType + " "
    
    @abstractmethod
    def getPossibleMoves(self, board):
        pass

class Rook(Piece):
    PIECE_TYPE = "R"
    VALUE = 50
    def __init__(self, x, y, color):
        super(Rook, self).__init__(x, y, color, Rook.PIECE_TYPE, Rook.VALUE)
    def getPossibleMoves(self, board):
        return self.getPossibleHorizontalMoves()
    def copy(self):
        return Rook(self.x, self.y, self.color)
    
class Knight(Piece):
    PIECE_TYPE = "N"
    VALUE = 30
    def __init__(self, x, y, color):
        super(Knight, self).__init__(x, y, color, Knight.PIECE_TYPE, Knight.VALUE)
    def getPossibleMoves(self, board):
        moves = []
        moves.append([(self.x, self.y), (self.x+2, self.y+1)])
        moves.append([(self.x, self.y), (self.x-1, self.y+2)])
        moves.append([(self.x, self.y), (self.x-2, self.y+1)])
        moves.append([(self.x, self.y), (self.x+1, self.y-2)])
        moves.append([(self.x, self.y), (self.x+2, self.y-1)])
        moves.append([(self.x, self.y), (self.x+1, self.y+2)])
        moves.append([(self.x, self.y), (self.x-2, self.y-1)])
        moves.append([(self.x, self.y), (self.x-1, self.y-2)])
        return self.removeNullFromList(moves)
    def copy(self):
        return Knight(self.x, self.y, self.color)
    
class Bishop(Piece):
    PIECE_TYPE = "B"
    VALUE = 30
    def __init__(self, x, y, color):
        super(Bishop, self).__init__(x, y, color, Bishop.PIECE_TYPE, Bishop.VALUE)
    def getPossibleMoves(self, board):
        return self.getPossibleDiagonalMoves()
    def copy(self):
        return Bishop(self.x, self.y, self.color)
    
class Queen(Piece):
    PIECE_TYPE = "Q"
    VALUE = 90
    def __init__(self, x, y, color):
        super(Queen, self).__init__(x, y, color, Queen.PIECE_TYPE, Queen.VALUE)
    def getPossibleMoves(self, board):
        diagonal = self.getPossibleDiagonalMoves()
        horizontal = self.getPossibleHorizontalMoves()
        return horizontal + diagonal
    def copy(self):
        return Queen(self.x, self.y, self.color)
    
class King(Piece):
    PIECE_TYPE = "K"
    VALUE = 900
    def __init__(self, x, y, color):
        super(King, self).__init__(x, y, color, King.PIECE_TYPE, King.VALUE)
    def getPossibleMoves(self, board):
        moves = []
        moves.append([(self.x, self.y), (self.x+1, self.y)])
        moves.append([(self.x, self.y), (self.x+1, self.y+1)])
        moves.append([(self.x, self.y), (self.x, self.y+1)])
        moves.append([(self.x, self.y), (self.x-1, self.y+1)])
        moves.append([(self.x, self.y), (self.x-1, self.y)])
        moves.append([(self.x, self.y), (self.x-1, self.y-1)])
        moves.append([(self.x, self.y), (self.x, self.y-1)])
        moves.append([(self.x, self.y), (self.x+1, self.y-1)])

        return self.removeNullFromList(moves)
        '''moves.append(self.get_castle_kingside_move())
        # moves.append(self.get_castle_queenside_move())
    
    # def get_castle_kingside_move(self, board):
        
    #     piece_in_corner = board.get_piece(self.x+3, self.y)
    #     if (piece_in_corner == 0 or piece_in_corner.piece_type != Rook.PIECE_TYPE):
    #         return 0

        
    #     if (piece_in_corner.color != self.color):
    #         return 0
        
        
    #     if (self.color == Piece.WHITE and board.white_king_moved):
    #         return 0
        
    #     if (self.color == Piece.BLACK and board.black_king_moved):
    #         return 0

        
    #     if (board.get_piece(self.x+1, self.y) != 0 or board.get_piece(self.x+2, self.y) != 0):
    #         return 0
        
    #     return Move(self.x, self.y, self.x+2, self.y)
    # #Nhập thành bên có hậu
    # def get_castle_queenside_move(self, board):
        
    #     piece_in_corner = board.get_piece(self.x-4, self.y)
    #     if (piece_in_corner == 0 or piece_in_corner.piece_type != Rook.PIECE_TYPE):
    #         return 0

        
    #     if (piece_in_corner.color != self.color):
    #         return 0
        
        
    #     if (self.color == Piece.WHITE and board.white_king_moved):
    #         return 0
        
    #     if (self.color == Piece.BLACK and board.black_king_moved):
    #         return 0

        
    #     if (board.get_piece(self.x-1, self.y) != 0 or board.get_piece(self.x-2, self.y) != 0 or board.get_piece(self.x-3, self.y) != 0):
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

        
        if (board.getPieceAt(self.x, self.y+direction) == 0):
            moves.append([(self.x, self.y), (self.x, self.y + direction)])

        
        if (self.isStartingPosition() and board.getPieceAt(self.x, self.y+ direction) == 0 and board.getPieceAt(self.x, self.y + direction*2) == 0):
            moves.append([(self.x, self.y), (self.x, self.y + direction * 2)])

        
        piece = board.getPieceAt(self.x + 1, self.y + direction)
        if (piece != 0):
            moves.append([(self.x, self.y), (self.x + 1, self.y + direction)])

        piece = board.getPieceAt(self.x - 1, self.y + direction)
        if (piece != 0):
            moves.append([(self.x, self.y), (self.x - 1, self.y + direction)])

        return self.removeNullFromList(moves)

    def copy(self):
        return Pawn(self.x, self.y, self.color)
    
    
    
    
