import random
from collections import deque


# Clase Nodo
class Nodo:
    def __init__(self, matriz, puntos_blanco=0, puntos_negro=0, dos_x_blanco=False, dos_x_negro=False, profundidad=0, utilidad=0, padre=None):
        self.matriz = matriz
        self.puntos_blanco = puntos_blanco
        self.puntos_negro = puntos_negro
        self.dos_x_blanco = dos_x_blanco
        self.dos_x_negro = dos_x_negro
        self.profundidad = profundidad
        self.padre = padre
        self.hijos = []
        self.utilidad = utilidad


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

def crear_nodo_raiz(matriz):
    nodo_raiz = Nodo(matriz)
    return nodo_raiz

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
        resultados.append((nueva_matriz, puntos, dos_x))

    return resultados

def generar_hijos(nodo, valor_caballo):

    posicion_caballo = encontrar_posicion_caballo(nodo.matriz, valor_caballo)
    if not posicion_caballo:
        print("no se encontró la posición del caballo")
        return []  # No se encontró el caballo en el tablero

    x, y = posicion_caballo
    por_dos = nodo.dos_x_blanco if valor_caballo == 11 else nodo.dos_x_negro
    hijos = []

    posibles_movimientos = mover_caballo(nodo.matriz, x, y, por_dos)

    for nueva_matriz, puntos, dos_x in posibles_movimientos:

        if valor_caballo == 11:  # Caballo blanco
            puntos_blanco = nodo.puntos_blanco + puntos
            puntos_negro = nodo.puntos_negro
            dos_x_blanco = dos_x
            dos_x_negro = nodo.dos_x_negro
        else:
            puntos_blanco = nodo.puntos_blanco
            puntos_negro = nodo.puntos_negro + puntos
            dos_x_blanco = nodo.dos_x_blanco
            dos_x_negro = dos_x

        # Crea el nodo hijo
        nodo_hijo = Nodo(
            nueva_matriz,
            puntos_blanco,
            puntos_negro,
            dos_x_blanco,
            dos_x_negro,
            nodo.profundidad + 1,
            0,  # La utilidad se calculará después
            nodo
        )
        hijos.append(nodo_hijo)
        nodo.hijos.append(nodo_hijo)
    return hijos

def crear_arbol(matriz, profundidad_maxima):

    nodo_raiz = crear_nodo_raiz(matriz)
    _expandir_nodo(nodo_raiz, profundidad_maxima)
    return nodo_raiz

def _expandir_nodo(nodo, profundidad_maxima):
    if nodo.profundidad >= profundidad_maxima:
        return

    if nodo.profundidad < profundidad_maxima:
        nodo.utilidad = -20000 if nodo.profundidad % 2 == 0 else 20000

    valor_caballo = 11 if nodo.profundidad % 2 == 0 else 12

    hijos = generar_hijos(nodo, valor_caballo)

    for hijo in hijos:
        _expandir_nodo(hijo, profundidad_maxima)

def utilidad_1(nodo):
    utilidad = nodo.puntos_blanco - nodo.puntos_negro

    if nodo.dos_x_blanco:
        utilidad += 10

    nodo.utilidad = utilidad
    return utilidad

def utilidad_2(nodo):
    utilidad = nodo.puntos_blanco - nodo.puntos_negro

    if nodo.dos_x_blanco:
        utilidad += 5

    nodo.utilidad = utilidad
    return utilidad

def asignar_utilidad_y_encolar(nodo_raiz, profundidad_maxima):
    cola = deque()

    def recorrer_y_asignar(nodo):
        if nodo.profundidad == profundidad_maxima:
            utilidad_1(nodo)

        cola.append(nodo)

        for hijo in nodo.hijos:
            recorrer_y_asignar(hijo)

    recorrer_y_asignar(nodo_raiz)
    return cola

def utilidad_min(nodos_hijos):
    if not nodos_hijos:
        return None  # Si no hay hijos, no se puede calcular la utilidad mínima

    # Encontrar el nodo con la utilidad mínima
    min_utilidad = min(nodo.utilidad for nodo in nodos_hijos)
    return min_utilidad


def utilidad_max(nodos_hijos):
    if not nodos_hijos:
        return None  # Si no hay hijos, no se puede calcular la utilidad máxima


    max_utilidad = max(nodo.utilidad for nodo in nodos_hijos)
    return max_utilidad

def podar_arbol_en_cola(cola):
    profundidad_maxima = max(nodo.profundidad for nodo in cola)
    if profundidad_maxima % 2 != 0:
        print("La profundidad máxima no es par, ajustando el proceso.")
        return

    while profundidad_maxima > 1:
        nivel_utilidad = "min" if profundidad_maxima % 2 == 0 else "max"
        padres_visitados = set()

        for nodo in list(cola):  # Crear una copia para poder modificar `cola` en el lugar
            if nodo.profundidad == profundidad_maxima:
                padre = nodo.padre
                if padre and padre not in padres_visitados:
                    hijos_utilidades = [hijo.utilidad for hijo in padre.hijos if hijo.profundidad == profundidad_maxima]
                    padre.utilidad = min(hijos_utilidades) if nivel_utilidad == "min" else max(hijos_utilidades)
                    padres_visitados.add(padre)
                cola.remove(nodo)  # Remover nodos en profundidad máxima directamente en `cola`

        profundidad_maxima -= 1

def seleccionar_mejor_nodo(cola):
    # Suponiendo que 'utilidad' es el atributo que queremos maximizar
    mejor_nodo = None
    mejor_utilidad = float('-inf')  # Inicializar con el valor más bajo posible

    for nodo in cola:
        if nodo.utilidad > mejor_utilidad:
            mejor_utilidad = nodo.utilidad
            mejor_nodo = nodo

    return mejor_nodo

def jugada_ia(matriz):
    # Paso 1: Crear el nodo raíz con la matriz proporcionada
    nodo_raiz = crear_nodo_raiz(matriz)

    # Paso 2: Crear el árbol hasta la profundidad máxima deseada (4 en este caso)
    profundidad_maxima = 4
    arbol = crear_arbol(nodo_raiz.matriz, profundidad_maxima)

    # Paso 3: Asignar utilidades en los nodos de máxima profundidad y encolar todo el árbol
    cola = asignar_utilidad_y_encolar(arbol, profundidad_maxima)

    # Paso 4: Podar el árbol en la cola, reduciendo la profundidad intercalando min y max
    podar_arbol_en_cola(cola)

    # Paso 5: Seleccionar el nodo de mejor utilidad
    mejor_nodo = seleccionar_mejor_nodo(cola)

    return mejor_nodo

# Heurística de IA1: maximiza puntos blancos
def heuristic_ia1(nodo):
    return nodo.puntos_blanco

# Heurística de IA2: estrategia combinada
def heuristic_ia2(nodo):
    return nodo.puntos_blanco + nodo.puntos_negro * 0.5 + (10 if nodo.dos_x else 0)



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
"""def simular_partida(matriz_inicial, nivel, ia1_heuristic, ia2_heuristic):
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
    return resultados"""

def imprimir_arbol(nodo, nivel=0):
    # Imprime la información del nodo actual
    indent = "  " * nivel
    print(f"{indent}Nodo en profundidad {nodo.profundidad} - Puntos Blanco: {nodo.puntos_blanco}, Puntos Negro: {nodo.puntos_negro}, Utilidad: {nodo.utilidad}")
    print(f"{indent}dos_x_blanco: {nodo.dos_x_blanco}, dos_x_negro: {nodo.dos_x_negro}")
    for fila in nodo.matriz:
        print(f"{indent}{fila}")
    print("\n")

    # Llama recursivamente para imprimir los hijos
    for hijo in nodo.hijos:
        imprimir_arbol(hijo, nivel + 1)


def main():
    global matriz_prueba
    # Paso 1: Crear el nodo raíz con la matriz de prueba
    nodo_raiz = crear_nodo_raiz(matriz_prueba)

    # Paso 2: Crear el árbol hasta la profundidad máxima deseada (4 en este caso)
    profundidad_maxima = 4
    arbol= crear_arbol(nodo_raiz.matriz, profundidad_maxima)

    # Paso 3: Asignar utilidades en los nodos de máxima profundidad y encolar todo el árbol
    cola = asignar_utilidad_y_encolar(arbol, profundidad_maxima)

    # Paso 4: Podar el árbol en la cola, reduciendo la profundidad intercalando min y max
    podar_arbol_en_cola(cola)
    mejor_nodo = seleccionar_mejor_nodo(cola)

    # Imprimir la información del mejor nodo
    print("Nodo de mejor utilidad:")
    print(f"Utilidad: {mejor_nodo.utilidad}, Puntos Blanco: {mejor_nodo.puntos_blanco}, Puntos Negro: {mejor_nodo.puntos_negro}")
    print("Matriz:")
    for fila in mejor_nodo.matriz:
        print(fila)

# Ejecutar la función principal si el script se ejecuta directamente
if __name__ == "__main__":
    main()

