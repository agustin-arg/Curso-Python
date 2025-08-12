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
        super().__init__('Destructor', 2)

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
    def place_ships(self):#Permite al jugador colocar sus barcos uno a uno pidiendo por consola la posición y orientación. Usa el método de cada barco para validar y marcar la posición.
        ships = [Destroyer(),Submarine(),Battleship()]
        for ship in ships:
            while True:
                print(f"{self.name}, coloca tu {ship.name} de tamaño {ship.size}.")
                start_row = int(input("Fila inicial: "))
                start_col = int(input("Columna inicial: "))
                direction = input("Dirección (H para horizontal, V para vertical): ").upper()
                if ship.place_ship(start_row, start_col, direction, self.board):
                    self.list_ships.append(ship)
                    self.print_board(self.board)
                    break
                else:
                    print("Posición no válida. Inténtalo de nuevo.")
            
    def print_board (self) #Muestra el tablero en consola.
        pass
    def attack(self): #Permite atacar una posición del tablero enemigo. Marca agua (A) si no hay barco, impacto (T) si acierta. Si hunde un barco, lo indica. Evita atacar dos veces la misma posición.
        pass
    def all_ships_sunk(self): #Devuelve True si todos los barcos del jugador han sido hundidos.
        pass