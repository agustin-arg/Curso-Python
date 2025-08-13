class Ship:
    '''
    Comportamiento de todos los barcos
    '''
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
        elif direction == 'V':  
            if start_row + self.size > len(board):
                return False
            else:
                for i in range(self.size):
                    if board[start_row+i][start_col] != ' ':
                        return False
                    positions.append((start_row+i,start_col))
        else:
            return False
        # Actualiza el tablero y guarda posiciones
        for pos in positions:
            board[pos[0]][pos[1]] = self.name[0]
        self.positions = positions
        return True
    
    def hit(self):
        self.hits += 1
        return self.hits == self.size


#Los tres tipos de barcos disponibles
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
    '''
    Datos del jugador, Sus tableros y los impactos que recibio
    Movimientos que puede hacer, poner sus barco y atacar
    Comprobar si sigue en juego
    '''
    def __init__(self,name):
        self.name = name
        self.board = [[' ' for _ in range(10)] for _ in range(10)]
        self.list_ships = []
        self.histboard = [[' ' for _ in range(10)] for _ in range(10)]

    def place_ships(self):
        ships = [Destroyer(),Submarine(),Battleship()]
        for ship in ships:
            while True:
                print(f"{self.name}, coloca tu {ship.name} de tamaño {ship.size}.")
                start_row = int(input("Fila inicial: "))
                start_col = int(input("Columna inicial: "))
                direction = input("Dirección (H para horizontal, V para vertical): ").upper()
                if ship.place_ship(start_row, start_col, direction, self.board):
                    self.list_ships.append(ship)
                    self.print_board() 
                    break
                else:
                    print("Posición no válida. Inténtalo de nuevo.")
    
    def print_board(self):
        for row in self.board:
            print(" ".join(row))
    
    def attack(self, opponent):
        while True:
            row_attack = int(input('ingrese el número de fila a atacar'))
            column_attack = int(input('ingrese el número de columna a atacar'))
            if 0 <= row_attack < 10 and 0 <= column_attack < 10:
                if opponent.board[row_attack][column_attack] == ' ':
                    print('AGUA!')
                    self.histboard[row_attack][column_attack] = 'A'   
                    opponent.board[row_attack][column_attack] = 'A'  
                    break
                elif opponent.board[row_attack][column_attack] != 'A':
                    print('TOCADO!')
                    self.histboard[row_attack][column_attack] = 'T'  
                    opponent.board[row_attack][column_attack] = 'T'  
                    for ship in opponent.list_ships:
                        if (row_attack,column_attack) in ship.positions:
                            if ship.hit():
                                print(f"¡Hundido! Has hundido el {ship.name}.")
                            break
                    break
                else:
                    print("Ya has atacado esta posición. Intenta de nuevo.")
            else:
                print("Posición no válida. Intenta de nuevo.")
    
    def all_ships_sunk(self):
        return all(ship.hits == ship.size for ship in self.list_ships)


class BattleshipGame:
    '''
    Controla el juego
    '''
    def __init__(self):
        self.player1 = Player("Jugador 1")
        self.player2 = Player("Jugador 2")
    
    def play(self):
        print("Bienvenido al juego de Batalla Naval!")
        print("Jugador 1 coloca sus barcos.")
        self.player1.place_ships()
        print("Jugador 2 coloca sus barcos.")
        self.player2.place_ships()
        current_player = self.player1
        opponent = self.player2
        while True:
            current_player.attack(opponent)
            if opponent.all_ships_sunk():
                print('Ha ganado el juego el jugador:', current_player.name)
                break
            current_player,opponent = opponent,current_player

# Crear una instancia del juego y jugar
game = BattleshipGame() 
game.play()