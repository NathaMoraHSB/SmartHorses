#mover_caballo
from movimientos_posibles import movimientos_posibles

def mover_caballo(matrix, x, y, por_dos=False):
    """
    Genera una lista de matrices resultantes al mover el caballo desde la posición (x, y)
    a cada movimiento posible.

    Parámetros:
    matriz (List[List[int]]): La matriz inicial.
    x (int): posición en el eje x (fila) del caballo.
    y (int): posición en el eje y (columna) del caballo.

    Retorna:
    List[List[List[int]]]: Lista de matrices, cada una representando un movimiento posible del caballo.
    """
    n = len(matrix)
    movimientos_validos = movimientos_posibles(x, y, n, matrix)
    valor_caballo = matrix[x][y]
    resultados = []

    for nx, ny in movimientos_validos:
        # Crea una copia de la matriz actual
        nueva_matriz = [fila[:] for fila in matrix]
        # Guarda los puntos y el estado de dos_x
        if matrix[nx][ny] == 20:
            puntos = 0  # Las casillas de valor 20 no suman puntos
            dos_x = True
        else:
            puntos = matrix[nx][ny]
            dos_x = False

        # Aplica la multiplicación por dos si por_dos es True
        if por_dos:
            puntos *= 2

        # Mueve el caballo a la nueva posición
        nueva_matriz[x][y] = 0  # Limpia la posición original
        nueva_matriz[nx][ny] = valor_caballo  # Coloca el caballo en la nueva posición

        # Agrega la nueva matriz, los puntos y el estado de dos_x a la lista de resultados
        resultados.append((nueva_matriz, puntos, dos_x))

    return resultados