#movimientos_posibles

def movimientos_posibles(x, y, n,  matrix):
    """
    Calcula los movimientos válidos de un caballo desde una posición (x, y) en una matriz de tamaño n x n.

    Parámetros:
    x (int): posición en el eje x (fila).
    y (int): posición en el eje y (columna).
    n (int): tamaño de la matriz (n x n).

    Retorna:
    List[Tuple[int, int]]: lista de posiciones válidas a las que el caballo puede moverse.
    """
    movimientos = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]

    movimientos_validos = []

    for dx, dy in movimientos:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and matrix[nx][ny] not in [11, 12]:
            movimientos_validos.append((nx, ny))

    return movimientos_validos
