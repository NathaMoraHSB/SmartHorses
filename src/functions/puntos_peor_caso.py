# puntos_peor_caso.py
from construir_arbol import construir_arbol_blanco
from construir_arbol_negro import construir_arbol_negro
from src.functions.mejor_hoja_max_profundidad import mejor_hoja_max_profundidad
from src.functions.quedan_movimientos import quedan_movimientos


def crear_arbol_profundidad_2(matriz_inicial):
    arbol = construir_arbol_blanco(matriz_inicial, profundidad_maxima=2)
    return arbol

def simular_partida(matriz_inicial):
    """
    Simula una partida alternando jugadas entre el caballo blanco y el caballo negro,
    hasta que no queden puntos entre 1 y 10 en la matriz.

    Parámetros:
    matriz_inicial (List[List[int]]): La matriz inicial del juego.

    Retorna:
    List[Nodo]: Lista de nodos de las mejores jugadas en orden secuencial de la partida.
    """
    matriz_actual = matriz_inicial
    turno_blanco = True
    historial_jugadas = []

    while quedan_movimientos(matriz_actual):
        if turno_blanco:

            arbol = construir_arbol_blanco(matriz_actual, profundidad_maxima=2)
            mejor_hoja = mejor_hoja_max_profundidad(arbol, profundidad_objetivo=2)
        else:

            arbol = construir_arbol_negro(matriz_actual, profundidad_maxima=2)
            mejor_hoja = mejor_hoja_max_profundidad(arbol, profundidad_objetivo=2)

        historial_jugadas.append(mejor_hoja)

        matriz_actual = mejor_hoja.matriz
        turno_blanco = not turno_blanco

    return historial_jugadas

