class Ship:
    def __init__(self,name,size):
        self.name = name
        self.size = size
        self.positions = []
        self.hits = 0
    def place_ship(self, start_row, start_col, direction, board):
        positions = []
        if direction == 'H':
            if start_col + self.size > len(board[0]):
                return False
            else:
                for i in range(self.size):
                    if board[start_row][start_col+i] != ' ':
                        return False
                    positions.append((start_row,start_col+i))
        elif direction == 'v':
            if start_row + self.size > len(board[0]):
                return False
            else:
                for i in range(self.size):
                    if board[start_row+i][start_col] != ' ':
                        return False
                    positions.append((start_row+i,start_col))
        else:
            return False    
    def hit(self):
        self.hits += 1
        return self.hits == self.size
        
class Destroyer(Ship):
    def __init__(self):
        super().__init__('destructor', 2)

class Submarine(Ship):
    def __init__(self):
        super().__init__('Submarino', 3)
        
class Battleship(Ship):
    def __init__(self):
        super().__init__('Acorazado', 4)
        
class Player():
    def __init__(self,name):
        self.name = name
        self.board = [[' ' for _ in range(10)] for _ in range(10)]
        self.list_ships = []
        self.histboard = [[' ' for _ in range(10)] for _ in range(10)]
    
        