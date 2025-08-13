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
            
    def print_board (self): #Muestra el tablero en consola.
        for row in self.board:
            list_board = ''
            for i in row:
                list_board += i
            print(list_board)
    # def print_board(self):  # Muestra el tablero en consola. Esta versión es más "pythónica" y sencilla.
    #     for row in self.board:
    #       print(" ".join(row))
    def attack(self, opponent): #Permite atacar una posición del tablero enemigo. Marca agua (A) si no hay barco, impacto (T) si acierta. Si hunde un barco, lo indica. Evita atacar dos veces la misma posición.
        while True: 
            row_attack = int(input('ingrese el número de fila a atacar'))
            column_attack = int(input('ingrese el número de columna a atacar'))
            if 0 <= row_attack < 10 and 0 <= column_attack < 10:
                if opponent.board[row_attack][column_attack] == ' ':
                    print('AGUA!')
                    self.histboard[row_attack][column_attack] == 'A'
                    opponent.board[row_attack][column_attack] == 'A'
                elif opponent.board[row_attack][column_attack] != 'A':
                    print('TOCADO!')
                    self.histboard[row_attack][column_attack] == 'T'
                    opponent.board[row_attack][column_attack] == 'T'
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
    def all_ships_sunk(self): #Devuelve True si todos los barcos del jugador han sido hundidos.
        list_hits = [ship.hits == ship.size for ship in self.list_ships]
        return list_hits == [True,True,True]
    # La versión correcta es:
    #     return all(ship.hits == ship.size for ship in self.list_ships)
    class BattleshipGame:
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
                    print('Ha ganado el juego el jugador:',{current_player.name})
                    break
                current_player,opponent = opponent,current_player

    # Crear una instancia del juego y jugar
game = BaseException()
game.play()