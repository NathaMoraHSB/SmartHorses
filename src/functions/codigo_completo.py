import random

# Clase Nodo
class Nodo:
    def __init__(self, matriz, puntos_blanco, puntos_negro, dos_x, profundidad, padre=None):
        self.matriz = matriz
        self.puntos_blanco = puntos_blanco
        self.puntos_negro = puntos_negro
        self.dos_x = dos_x
        self.profundidad = profundidad
        self.padre = padre
        self.hijos = []

""""# Genera una matriz aleatoria
def random_matrix(size=8):
    matrix = [[0 for _ in range(size)] for _ in range(size)]
    point_positions = random.sample([(i, j) for i in range(size) for j in range(size)], 10)
    for pos in point_positions:
        matrix[pos[0]][pos[1]] = random.randint(1, 10)

    x2_positions = random.sample([pos for pos in [(i, j) for i in range(size) for j in range(size)] if pos not in point_positions], 4)
    for pos in x2_positions:
        matrix[pos[0]][pos[1]] = 20

    horse_positions = random.sample([pos for pos in [(i, j) for i in range(size) for j in range(size)] if pos not in point_positions and pos not in x2_positions], 2)
    matrix[horse_positions[0][0]][horse_positions[0][1]] = 11
    matrix[horse_positions[1][0]][horse_positions[1][1]] = 12

    return matrix"""

matriz_prueba = [
    [8, 0, 0, 0, 4, 0, 0, 20],
    [0, 20, 0, 0, 0, 12, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 11, 0, 0, 0, 0, 20, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [20, 0, 0, 0, 0, 0, 0, 0]
]

# Encuentra la posición del caballo
def encontrar_posicion_caballo(matriz, valor_caballo):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor_caballo:
                return i, j
    return None

# Calcula movimientos posibles del caballo
def movimientos_posibles(x, y, n, matrix):
    movimientos = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    movimientos_validos = []
    for dx, dy in movimientos:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and matrix[nx][ny] not in [11, 12]:
            movimientos_validos.append((nx, ny))
    return movimientos_validos

# Verifica si quedan movimientos
def quedan_movimientos(matriz):
    for fila in matriz:
        for valor in fila:
            if 1 <= valor <= 10:
                return True
    return False

# Construye el árbol de decisiones
def mover_caballo(matrix, x, y, por_dos=False, posicion_previa=None):
    n = len(matrix)
    movimientos_validos = movimientos_posibles(x, y, n, matrix)
    valor_caballo = matrix[x][y]
    resultados = []

    for nx, ny in movimientos_validos:
        if posicion_previa is not None and (nx, ny) == posicion_previa:
            print(f"Movimiento ignorado: regresar a posición previa {(nx, ny)} desde {(x, y)}")
            continue

        nueva_matriz = [fila[:] for fila in matrix]

        if matrix[nx][ny] == 20:
            puntos = 0
            dos_x = True
        else:
            puntos = matrix[nx][ny]
            dos_x = False

        if por_dos:
            puntos *= 2

        nueva_matriz[x][y] = 0
        nueva_matriz[nx][ny] = valor_caballo

        print(f"Generando movimiento a posición {(nx, ny)} desde {(x, y)} con puntos: {puntos}")
        resultados.append((nueva_matriz, puntos, dos_x))

    return resultados

def construir_arbol(matriz_inicial, profundidad_maxima, valor_caballo_inicial, puntos_blanco=0, puntos_negro=0, dos_x=False):
    cola = []
    nodos_visitados = set()

    nodo_raiz = Nodo(matriz_inicial, puntos_blanco=puntos_blanco, puntos_negro=puntos_negro, dos_x=dos_x, profundidad=0)
    cola.append((nodo_raiz, None))
    print("Iniciando construcción del árbol con nodo raíz")

    while cola:
        nodo_actual, posicion_previa = cola.pop(0)

        if nodo_actual.profundidad >= profundidad_maxima:
            print(f"Nodo alcanzó profundidad máxima: {nodo_actual.profundidad}")
            continue

        estado_actual = tuple(map(tuple, nodo_actual.matriz))
        if (estado_actual, nodo_actual.profundidad) in nodos_visitados:
            print("Estado ya visitado en esta profundidad, omitiendo")
            continue
        nodos_visitados.add((estado_actual, nodo_actual.profundidad))

        valor_caballo = valor_caballo_inicial if nodo_actual.profundidad % 2 == 0 else (12 if valor_caballo_inicial == 11 else 11)
        posicion_caballo = encontrar_posicion_caballo(nodo_actual.matriz, valor_caballo)

        if posicion_caballo is None:
            print(f"No se encontró el caballo {valor_caballo} en el estado actual. Saltando nodo.")
            continue

        x, y = posicion_caballo
        print(f"Expandiendo nodo en profundidad {nodo_actual.profundidad}, posición del caballo: {(x, y)}")

        movimientos = mover_caballo(nodo_actual.matriz, x, y, nodo_actual.dos_x, posicion_previa)

        for nueva_matriz, puntos, dos_x_nuevo in movimientos:
            nuevo_puntos_blanco = nodo_actual.puntos_blanco + puntos if valor_caballo == 11 else nodo_actual.puntos_blanco
            nuevo_puntos_negro = nodo_actual.puntos_negro + puntos if valor_caballo == 12 else nodo_actual.puntos_negro
            nuevo_nodo = Nodo(nueva_matriz, nuevo_puntos_blanco, nuevo_puntos_negro, dos_x_nuevo, nodo_actual.profundidad + 1, nodo_actual)

            print(f"Creando nodo en profundidad {nuevo_nodo.profundidad} - Puntos Blanco: {nuevo_puntos_blanco}, Puntos Negro: {nuevo_puntos_negro}")

            nodo_actual.hijos.append(nuevo_nodo)
            cola.append((nuevo_nodo, posicion_caballo))

    return nodo_raiz

# Heurística de IA1: maximiza puntos blancos
def heuristic_ia1(nodo):
    return nodo.puntos_blanco

# Heurística de IA2: estrategia combinada
def heuristic_ia2(nodo):
    return nodo.puntos_blanco + nodo.puntos_negro * 0.5 + (10 if nodo.dos_x else 0)

# Encuentra la mejor hoja con heurística variable
def mejor_hoja_max_profundidad(nodo_raiz, profundidad_objetivo, heuristic):
    hojas_en_profundidad = []
    def recorrer_nodos(nodo):
        if nodo.profundidad == profundidad_objetivo:
            hojas_en_profundidad.append(nodo)
        for hijo in nodo.hijos:
            recorrer_nodos(hijo)
    recorrer_nodos(nodo_raiz)
    return max(hojas_en_profundidad, key=heuristic, default=None)

# Define la profundidad según el nivel de dificultad
def nivel_de_dificultad(nivel):
    if nivel == 1:
        return 2
    elif nivel == 2:
        return 4
    elif nivel == 3:
        return 6
    else:
        raise ValueError("Nivel no válido. Debe ser 1 (Principiante), 2 (Amateur) o 3 (Experto).")

# Simula una partida entre IA1 y IA2
def simular_partida(matriz_inicial, nivel, ia1_heuristic, ia2_heuristic):
    profundidad_maxima = nivel_de_dificultad(nivel)
    matriz_actual = matriz_inicial
    turno_blanco = True
    puntos_blanco = puntos_negro = 0
    dos_x = False
    turno = 1
    while quedan_movimientos(matriz_actual):
        print(f"Turno {turno}: {'Blanco' if turno_blanco else 'Negro'}")
        heuristic = ia1_heuristic if turno_blanco else ia2_heuristic
        arbol = construir_arbol(matriz_actual, profundidad_maxima, 11 if turno_blanco else 12, puntos_blanco, puntos_negro, dos_x)
        mejor_hoja = mejor_hoja_max_profundidad(arbol, profundidad_maxima, heuristic)
        if mejor_hoja is None:
            break
        matriz_actual = mejor_hoja.matriz
        puntos_blanco = mejor_hoja.puntos_blanco
        puntos_negro = mejor_hoja.puntos_negro
        dos_x = mejor_hoja.dos_x
        turno_blanco = not turno_blanco
        turno += 1
    ganador = "Blanco" if puntos_blanco > puntos_negro else ("Negro" if puntos_negro > puntos_blanco else "Empate")
    return ganador, puntos_blanco, puntos_negro

# Ejecuta varias simulaciones y registra resultados
def ejecutar_simulaciones(num_simulaciones, nivel):
    resultados = {"IA1_wins": 0, "IA2_wins": 0, "Empates": 0}
    for _ in range(num_simulaciones):
        matriz_inicial = matriz_prueba
        ganador, puntos_blanco, puntos_negro = simular_partida(matriz_inicial, nivel, heuristic_ia1, heuristic_ia2)
        if ganador == "Blanco":
            resultados["IA1_wins"] += 1
        elif ganador == "Negro":
            resultados["IA2_wins"] += 1
        else:
            resultados["Empates"] += 1
    return resultados



# Ejecuta la simulación si el script se ejecuta directamente
if __name__ == "__main__":
    nivel = 1  # Cambia el nivel según corresponda (1, 2 o 3)
    num_simulaciones = 1
    resultados = ejecutar_simulaciones(num_simulaciones, nivel)
    print(f"Resultados de {num_simulaciones} simulaciones en nivel {nivel}:")
    print(f"IA1 ganó {resultados['IA1_wins']} veces, IA2 ganó {resultados['IA2_wins']} veces, Empates: {resultados['Empates']}")
