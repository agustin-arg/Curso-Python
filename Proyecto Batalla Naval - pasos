# Proyecto: Batalla Naval (Battleship) en Python

## Descripción del Proyecto
En este proyecto, crearás un juego de Batalla Naval (Battleship) en Python, donde dos jugadores colocan sus barcos en un tablero y se turnan para atacar las posiciones del oponente hasta que uno de los jugadores hunda todos los barcos del otro.

Este proyecto te permitirá practicar:
- Manipulación de listas
- Programación orientada a objetos (clases y métodos)
- Gestión de la interacción entre múltiples clases
- Lógica de juegos

---

## Paso 1: Define la Clase Ship

### Objetivo
Crear la clase base `Ship` que representará todos los barcos del juego.

### Implementación
```python
class Ship:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.positions = []  # Lista vacía para las posiciones del barco
        self.hits = 0        # Contador de impactos inicializado en 0
```

### Métodos requeridos:

#### Método `place_ship`
- **Propósito**: Coloca el barco en el tablero según la posición inicial y dirección
- **Parámetros**: `board`, `start_row`, `start_col`, `direction`
- **Funcionalidad**:
  - Verifica si el barco cabe en el tablero
  - Valida que las posiciones estén libres (' ')
  - Actualiza el tablero con el símbolo del barco (`self.name[0]`)
  - Almacena las posiciones en `self.positions`
  - Devuelve `True` si se coloca exitosamente, `False` en caso contrario

#### Método `hit`
- **Propósito**: Registra un impacto en el barco
- **Funcionalidad**:
  - Incrementa `self.hits`
  - Devuelve `True` si el barco ha sido hundido (`self.hits == self.size`)

---

## Paso 2: Define Clases Específicas de Barcos

### Subclases de Ship
Crea las siguientes clases que hereden de `Ship`:

```python
class Destroyer(Ship):
    def __init__(self):
        super().__init__('Destructor', 2)

class Submarine(Ship):
    def __init__(self):
        super().__init__('Submarino', 3)

class Battleship(Ship):
    def __init__(self):
        super().__init__('Acorazado', 4)
```

---

## Paso 3: Define la Clase Player

### Objetivo
Crear la clase `Player` que maneje la lógica de cada jugador.

### Atributos iniciales
```python
class Player:
    def __init__(self, name):
        self.name = name
        self.board = [[' ' for _ in range(10)] for _ in range(10)]  # Tablero 10x10
        self.ships = []      # Lista de barcos del jugador
        self.hits = [[' ' for _ in range(10)] for _ in range(10)]  # Tablero de ataques
```

### Métodos requeridos:

#### Método `place_ships`
- Crea instancias de `Destroyer`, `Submarine` y `Battleship`
- Solicita al jugador la posición (fila, columna) y dirección (H/V)
- Usa `place_ship` para colocar cada barco
- Repite si la colocación falla

#### Método `print_board`
- Imprime el tablero actual del jugador
- Muestra las posiciones de los barcos o los impactos

#### Método `attack`
- Solicita coordenadas de ataque al jugador
- Valida las coordenadas
- Verifica si es impacto o agua
- Actualiza los tableros correspondientes
- Verifica si el barco impactado ha sido hundido

#### Método `all_ships_sunk`
- Devuelve `True` si todos los barcos han sido hundidos

---

## Paso 4: Define la Clase BattleshipGame

### Objetivo
Crear la clase principal que maneje la lógica del juego completo.

```python
class BattleshipGame:
    def __init__(self):
        self.player1 = Player("Jugador 1")
        self.player2 = Player("Jugador 2")
```

### Método `play`
**Flujo del juego**:
1. Solicita a cada jugador colocar sus barcos
2. Alterna turnos entre jugadores para atacar
3. Verifica condiciones de victoria después de cada ataque
4. Declara ganador cuando todos los barcos de un jugador sean hundidos

---

## Paso 5: Ejecuta el Juego

### Código principal
```python
# Crear instancia del juego e iniciar
game = BattleshipGame()
game.play()
```

---

## Características del Juego Final

### Funcionalidades
- ✅ Tableros de 10x10 para cada jugador
- ✅ Tres tipos de barcos con diferentes tamaños
- ✅ Colocación manual de barcos por cada jugador
- ✅ Sistema de turnos alternados
- ✅ Detección de impactos y barcos hundidos
- ✅ Condición de victoria automática

### Elementos de aprendizaje
- **Programación Orientada a Objetos**: Clases, herencia, métodos
- **Estructuras de datos**: Listas bidimensionales, listas de objetos
- **Lógica de juegos**: Turnos, validaciones, condiciones de victoria
- **Interacción con usuario**: Input/output, validación de datos

---

## ¡Diviértete creando tu propio juego de Batalla Naval! 🚢⚓
