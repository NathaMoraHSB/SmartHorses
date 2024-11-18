# encontrar_posicion_caballo.py


def encontrar_posicion_caballo(matriz, valor_caballo):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor_caballo:
                return i, j
    return None  # Si no se encuentra el caballo