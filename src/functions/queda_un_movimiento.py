#queda_un_movimiento.py
def queda_un_solo_movimiento(matriz):
    """
    Verifica si queda solo un movimiento posible en la matriz y retorna su posición.

    Parámetros:
    matriz (List[List[int]]): La matriz a verificar.

    Retorna:
    tuple or None: Las coordenadas (fila, columna) si hay exactamente un valor entre 1 y 10,
                   None si no hay movimientos o si hay más de uno.
    """
    posicion_movimiento = None
    conteo_movimientos = 0

    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            valor = matriz[fila][columna]
            if 1 <= valor <= 10:
                conteo_movimientos += 1
                posicion_movimiento = (fila, columna)
                if conteo_movimientos > 1:
                    # Si encontramos más de un movimiento, retornamos None
                    return None

    # Retorna la posición si encontramos exactamente un movimiento, None de lo contrario
    return posicion_movimiento if conteo_movimientos == 1 else None
