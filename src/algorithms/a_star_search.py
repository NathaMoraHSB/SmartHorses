# a_star_search.py
from queue import PriorityQueue
from typing import List, Tuple
import time

# Definiciones de tipos personalizados
Posicion = Tuple[int, int]
Camino = List[Posicion]
Derecha = List[Posicion]
Ciudad = List[List[int]]

# Constantes
DIRECCIONES = [(-1, 0), (1, 0), (0, -1), (0, 1)]
COSTOS = {0: 1, 3: 4, 4: 7}

# Función para calcular la distancia de Manhattan
def distancia_manhattan(nodo: Posicion, destino: Posicion) -> int:
    return abs(nodo[0] - destino[0]) + abs(nodo[1] - destino[1])

# Función para validar si una posición es válida
def es_posicion_valida(x: int, y: int, ciudad: Ciudad) -> bool:
    filas = len(ciudad)
    columnas = len(ciudad[0])
    return 0 <= x < filas and 0 <= y < columnas and ciudad[x][y] != 1

# Implementación del algoritmo A* (A-Star)
def a_star_search(ciudad: Ciudad, inicio: Posicion, fin: Posicion) -> Tuple[Camino, int, int, float, int]:
    print ("posision inicial", inicio, "posicion final", fin)
    start_time = time.time()
    pq = PriorityQueue()
    pq.put((0 + distancia_manhattan(inicio, fin), 0, inicio, [], 0))  # (f(n), g(n), posición, camino, profundidad_actual)
    visitado = {}
    nodos_expandidos = 0
    profundidad_maxima = 0  # Para almacenar la profundidad máxima alcanzada en cualquier rama
    while not pq.empty():
        f, g, (x, y), camino, profundidad_actual = pq.get()

        # Actualizar la profundidad máxima explorada
        profundidad_maxima = max(profundidad_maxima, profundidad_actual)

        if (x, y) == fin:
            return camino + [(x, y)], nodos_expandidos, profundidad_maxima, time.time() - start_time, g

        if (x, y) in visitado and visitado[(x, y)] <= g:
            continue

        visitado[(x, y)] = g
        nodos_expandidos += 1

        for dx, dy in DIRECCIONES:
            nx, ny = x + dx, y + dy
            if es_posicion_valida(nx, ny, ciudad):
                nuevo_costo = g + COSTOS.get(ciudad[nx][ny], 1)  # g(n) acumulado
                heuristica = distancia_manhattan((nx, ny), fin)  # h(n)
                pq.put((nuevo_costo + heuristica, nuevo_costo, (nx, ny), camino + [(x, y)], profundidad_actual + 1))  # Incrementar profundidad




    return None, nodos_expandidos, profundidad_maxima, time.time() - start_time, 0
