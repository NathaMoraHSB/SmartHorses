#dimulateMovenent.py
from src.functions.matrixUtils import find_start_and_destination
  # Asegúrate de importar la función

# Función para imprimir la matriz
def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))
    print("\n")  # Línea en blanco para separar cada estado de la matriz

def simulate_movement(matrix, path, label):

    original_matrix = [row[:] for row in matrix]

    simulation_steps = []  # Lista para almacenar los estados de la matriz

    # Encuentra las posiciones de inicio, pasajero y destino
    positions = find_start_and_destination(matrix)
    start = positions["start"]

    # Limpiar la casilla de inicio al inicio de la simulación
    if start is not None:
        x_start, y_start = start
        matrix[x_start][y_start] = 0  # Cambia el valor de la posición inicial a 0 (celda vacía)

    # Guardamos la posición del vehículo antes del primer movimiento
    prev_position = None  # Empezamos sin una posición previa

    for position in path:
        # Limpiamos la posición anterior del carro (representado por 2)
        if prev_position is not None:  # Solo limpiamos si ya tenemos una posición previa
            x_prev, y_prev = prev_position
            # Si el valor original es 3 o 4, restauramos el tráfico original
            if original_matrix[x_prev][y_prev] in [3, 4, 6]:
                matrix[x_prev][y_prev] = original_matrix[x_prev][y_prev]  # Restaurar el valor original
            else:
                matrix[x_prev][y_prev] = 0  # De lo contrario, lo limpiamos como una celda vacía

        # Actualizamos la posición actual del vehículo
        x, y = position
        matrix[x][y] = 2  # Representamos el vehículo en la nueva posición

        # Copiamos el estado actual de la matriz y lo agregamos a la lista
        simulation_steps.append([row[:] for row in matrix])  # Hacemos una copia profunda de la matriz

        # Actualizamos la posición previa
        prev_position = position

    # Asegurarse de que la última posición del vehículo no deje rastros al final
    x_final, y_final = path[-1]
    if original_matrix[x_final][y_final] in [3, 4]:
        matrix[x_final][y_final] = original_matrix[x_final][y_final]  # Restaurar el tráfico en la última posición
    else:
        matrix[x_final][y_final] = 0  # Limpiar la última posición si no es tráfico

    return simulation_steps
