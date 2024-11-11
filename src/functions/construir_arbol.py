# construir_arbol.py
from .mover_caballo import mover_caballo
from .nodo import Nodo
from .encontrar_posicion_caballo import encontrar_posicion_caballo

def construir_arbol(matriz_inicial, profundidad_maxima, valor_caballo_inicial, puntos_blanco=0, puntos_negro=0, dos_x=False):
    cola = []
    nodo_raiz = Nodo(matriz_inicial, puntos_blanco=puntos_blanco, puntos_negro=puntos_negro, dos_x=dos_x, profundidad=0)
    cola.append(nodo_raiz)

    while cola:
        nodo_actual = cola.pop(0)

        if nodo_actual.profundidad >= profundidad_maxima:
            continue

        # Alternar el valor del caballo en función de la profundidad
        if nodo_actual.profundidad % 2 == 0:
            valor_caballo = valor_caballo_inicial
        else:
            valor_caballo = 12 if valor_caballo_inicial == 11 else 11  # Alterna entre caballos

        # Obtener la posición del caballo en turno
        posicion_caballo = encontrar_posicion_caballo(nodo_actual.matriz, valor_caballo)
        if posicion_caballo is None:
            print(f"No se encontró el caballo {valor_caballo} en la matriz. Saltando nodo.")
            continue

        x, y = posicion_caballo
        movimientos = mover_caballo(nodo_actual.matriz, x, y, nodo_actual.dos_x)

        # Actualizar puntos según el caballo que se mueve
        for nueva_matriz, puntos, dos_x_nuevo in movimientos:
            if valor_caballo == 11:  # Caballo blanco
                nuevo_puntos_blanco = nodo_actual.puntos_blanco + puntos
                nuevo_puntos_negro = nodo_actual.puntos_negro
            else:  # Caballo negro
                nuevo_puntos_blanco = nodo_actual.puntos_blanco
                nuevo_puntos_negro = nodo_actual.puntos_negro + puntos

            # Crear un nuevo nodo hijo
            nuevo_nodo = Nodo(nueva_matriz, nuevo_puntos_blanco, nuevo_puntos_negro, dos_x_nuevo, nodo_actual.profundidad + 1, nodo_actual)
            nodo_actual.hijos.append(nuevo_nodo)
            cola.append(nuevo_nodo)

    return nodo_raiz


def construir_arbol_blanco(matriz_inicial, profundidad_maxima, puntos_blanco, puntos_negro, dos_x):
    arbol= construir_arbol(matriz_inicial, profundidad_maxima, valor_caballo_inicial=11, puntos_blanco=puntos_blanco, puntos_negro=puntos_negro, dos_x=dos_x)
    return arbol

def construir_arbol_negro(matriz_inicial, profundidad_maxima, puntos_blanco, puntos_negro, dos_x):
    arbol= construir_arbol(matriz_inicial, profundidad_maxima, valor_caballo_inicial=12, puntos_blanco=puntos_blanco, puntos_negro=puntos_negro, dos_x=dos_x)
    return arbol

def imprimir_arbol(nodo, nivel=0):
    if nodo is None:
        print("arbol nulo")
        return

    # Imprime la información del nodo actual con indentación para visualizar la jerarquía
    print("  " * nivel + f"Nivel {nivel} | Puntos Blanco: {nodo.puntos_blanco}, Puntos Negro: {nodo.puntos_negro}, Profundidad: {nodo.profundidad}")

    # Llama recursivamente a esta función para imprimir todos los hijos del nodo actual
    for hijo in nodo.hijos:
        imprimir_arbol(hijo, nivel + 1)