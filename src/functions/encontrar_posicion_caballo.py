# encontrar_posicion_caballo.py


def encontrar_posicion_caballo(matriz, valor_caballo):
    """
    Encuentra la posición (x, y) de un caballo en la matriz.

    Parámetros:
    matriz (List[List[int]]): La matriz en la que buscar.
    valor_caballo (int): El valor del caballo (11 para blanco, 12 para negro).

    Retorna:
    Tuple[int, int]: Las coordenadas (x, y) del caballo, o None si no se encuentra.
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor_caballo:
                return i, j
    return None  # Si no se encuentra el caballo