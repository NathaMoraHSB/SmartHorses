from src.functions.construir_arbol import construir_arbol_blanco, construir_arbol_negro
from src.functions.mejor_hoja_max_profundidad import mejor_hoja_max_profundidad
from src.functions.quedan_movimientos import quedan_movimientos

matriz_inicial = [
    [8, 0, 0, 0, 4, 0, 0, 20],
    [0, 20, 1, 0, 0, 12, 0, 0],
    [0, 0, 0, 9, 0, 0, 0, 0],
    [0, 7, 0, 0, 3, 0, 20, 0],
    [0, 11, 0, 0, 0, 0, 0, 0],
    [10, 0, 0, 0, 6, 0, 0, 0],
    [0, 0, 5, 0, 0, 0, 2, 0],
    [20, 0, 0, 0, 0, 0, 0, 0]
]

matriz_prueba = [
    [8, 0, 0, 0, 4, 0, 0, 20],
    [0, 20, 0, 0, 0, 12, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 20, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [20, 0, 0, 0, 0, 0, 0, 0]
]

def simular_partida(matriz_inicial):
    matriz_actual = matriz_inicial
    turno_blanco = True
    historial_jugadas = []

    puntos_blanco = 0
    puntos_negro = 0
    dos_x = False

    turno = 0  # Contador de turnos para facilitar el seguimiento
    while quedan_movimientos(matriz_actual):
        print(f"\n--- Turno {turno} ---")
        print(f"Turno del {'caballo blanco' if turno_blanco else 'caballo negro'}")
        print("Matriz actual antes del movimiento:")
        for fila in matriz_actual:
            print(fila)


        if turno_blanco:
            arbol = construir_arbol_blanco(
                matriz_actual, profundidad_maxima=2,
                puntos_blanco=puntos_blanco, puntos_negro=puntos_negro, dos_x=dos_x
            )
        else:
            arbol = construir_arbol_negro(
                matriz_actual, profundidad_maxima=2,
                puntos_blanco=puntos_blanco, puntos_negro=puntos_negro, dos_x=dos_x
            )

        mejor_hoja = mejor_hoja_max_profundidad(arbol, profundidad_objetivo=2)
        if mejor_hoja is None:
            print("No se encontraron nodos en profundidad 2. Terminando la simulación.")
            break

        # Actualiza el estado del juego con el mejor movimiento seleccionado
        matriz_actual = mejor_hoja.matriz
        puntos_blanco = mejor_hoja.puntos_blanco
        puntos_negro = mejor_hoja.puntos_negro
        dos_x = mejor_hoja.dos_x

        for fila in matriz_actual:
            print(fila)

        historial_jugadas.append(mejor_hoja)

        # Alterna el turno entre caballos
        turno_blanco = not turno_blanco
        turno += 1  # Incrementa el turno

    print("\n--- Fin de la simulación ---")
    print("Historial de jugadas:")
    for i, nodo in enumerate(historial_jugadas):
        print(f"\nJugada {i + 1}:")
        for fila in nodo.matriz:
            print(fila)
        print(f"Puntos acumulados - Blanco: {nodo.puntos_blanco}, Negro: {nodo.puntos_negro}")

    return historial_jugadas


def imprimir_arbol(nodo, nivel=0):
    if nodo is None:
        return

    # Imprime la información del nodo actual con indentación para visualizar la jerarquía
    print("  " * nivel + f"Nivel {nivel} | Puntos Blanco: {nodo.puntos_blanco}, Puntos Negro: {nodo.puntos_negro}, Profundidad: {nodo.profundidad}")

    # Llama recursivamente a esta función para imprimir todos los hijos del nodo actual
    for hijo in nodo.hijos:
        imprimir_arbol(hijo, nivel + 1)

# Ejecuta la simulación si el script se ejecuta directamente
if __name__ == "__main__":
    print("Ejecutando simulación con la matriz inicial:")
    for fila in matriz_inicial:
        print(fila)

    historial_jugadas = simular_partida(matriz_inicial)

    print("\nResultado de la simulación:")
    for i, nodo in enumerate(historial_jugadas):
        print(f"\nJugada {i+1}:")
        for fila in nodo.matriz:
            print(fila)
        print(f"Puntos Blanco: {nodo.puntos_blanco}, Puntos Negro: {nodo.puntos_negro}")
