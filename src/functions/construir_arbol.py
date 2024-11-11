# construir_arbol.py
from mover_caballo import mover_caballo
from nodo import Nodo
from encontrar_posicion_caballo import encontrar_posicion_caballo

def construir_arbol(matriz_inicial, profundidad_maxima):
    # Cola para manejar los nodos. Empieza con la raíz del árbol
    cola = []

    # Nodo raíz
    nodo_raiz = Nodo(matriz_inicial, 0, False, 0)
    cola.append(nodo_raiz)

    while cola:
        nodo_actual = cola.pop(0)

        # Si se ha alcanzado la profundidad máxima, no expandir más este nodo
        if nodo_actual.profundidad >= profundidad_maxima:
            continue

        # Determina cuál caballo debe moverse en esta profundidad
        if nodo_actual.profundidad % 2 == 0:  # Profundidad par -> mueve caballo blanco
            valor_caballo = 11
        else:  # Profundidad impar -> mueve caballo negro
            valor_caballo = 12

        # Encuentra la posición del caballo correspondiente
        posicion_caballo = encontrar_posicion_caballo(nodo_actual.matriz, valor_caballo)
        if posicion_caballo is None:
            continue  # Si no encuentra el caballo, salta este nodo

        x, y = posicion_caballo

        # Genera todos los posibles movimientos desde el nodo actual para el caballo correspondiente
        movimientos = mover_caballo(nodo_actual.matriz, x, y, nodo_actual.dos_x)

        for nueva_matriz, puntos, dos_x_nuevo in movimientos:
            puntos_acumulados = nodo_actual.puntos_acumulados + puntos
            nuevo_nodo = Nodo(nueva_matriz, puntos_acumulados, dos_x_nuevo, nodo_actual.profundidad + 1, nodo_actual)
            nodo_actual.hijos.append(nuevo_nodo)
            cola.append(nuevo_nodo)

    return nodo_raiz