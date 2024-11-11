#quedan_movimientos

def quedan_movimientos(matriz):
    """
    Verifica si existen valores entre 1 y 10 en la matriz.

    Parámetros:
    matriz (List[List[int]]): La matriz a verificar.

    Retorna:
    bool: True si hay al menos un valor entre 1 y 10, False de lo contrario.
    """
    for fila in matriz:
        for valor in fila:
            if 1 <= valor <= 10:
                return True
    return False
