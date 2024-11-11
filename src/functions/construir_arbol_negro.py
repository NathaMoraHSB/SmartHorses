from mover_caballo import mover_caballo
from nodo import Nodo
from encontrar_posicion_caballo import encontrar_posicion_caballo

def construir_arbol_negro(matriz_inicial, profundidad_maxima):
    cola = []

    nodo_raiz = Nodo(matriz_inicial, puntos_blanco=0, puntos_negro=0, dos_x=False, profundidad=0)
    cola.append(nodo_raiz)

    while cola:
        nodo_actual = cola.pop(0)

        if nodo_actual.profundidad >= profundidad_maxima:
            continue

        if nodo_actual.profundidad % 2 == 0:  # Profundidad par -> mueve caballo negro
            valor_caballo = 12
            puntos_blanco = nodo_actual.puntos_blanco
            puntos_negro = nodo_actual.puntos_negro
        else:
            valor_caballo = 11
            puntos_blanco = nodo_actual.puntos_blanco
            puntos_negro = nodo_actual.puntos_negro

        posicion_caballo = encontrar_posicion_caballo(nodo_actual.matriz, valor_caballo)
        if posicion_caballo is None:
            continue

        x, y = posicion_caballo

        movimientos = mover_caballo(nodo_actual.matriz, x, y, nodo_actual.dos_x)

        for nueva_matriz, puntos, dos_x_nuevo in movimientos:

            if valor_caballo == 12:  # Mueve el caballo negro
                nuevo_puntos_negro = puntos_negro + puntos
                nuevo_puntos_blanco = puntos_blanco
            else:  # Mueve el caballo blanco
                nuevo_puntos_blanco = puntos_blanco + puntos
                nuevo_puntos_negro = puntos_negro


            nuevo_nodo = Nodo(nueva_matriz, nuevo_puntos_blanco, nuevo_puntos_negro, dos_x_nuevo, nodo_actual.profundidad + 1, nodo_actual)
            nodo_actual.hijos.append(nuevo_nodo)
            cola.append(nuevo_nodo)

    return nodo_raiz
