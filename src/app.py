#app.py
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
CORS(app, resources={r"/*": {"origins": "*"}})

# Inicializar la variable global de la matriz como None
matrix = None

#matrix = random_matrix()

@app.route('/api/start', methods=['POST'])
def start_matrix():
    global matrix

    matrix = [
        [8, 0, 0, 0, 4, 0, 0, 20],
        [0, 20, 1, 0, 0, 12, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 0],
        [0, 7, 0, 0, 3, 0, 20, 0],
        [0, 11, 0, 0, 0, 0, 0, 0],
        [10, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 2, 0],
        [20, 0, 0, 0, 0, 0, 0, 0]
    ]
    if matrix:
        return jsonify({"matrix": matrix})
    else:
        return jsonify({"error": "File not found"}), 404



#se recibe matriz inicial y todos los valores puntos caballo negro y caballo blanco, dos_x caballo blanco
#@app.route('/api/machineMove', methods=['POST'])
#def machine_move():

@app.route('/api/human-move', methods=['POST'])
def human_move():
    global matrix
    data = request.get_json()

    matrix = data["matrix"]
    row = data["selectedCell"]["row"]
    col = data["selectedCell"]["col"]
    por_dos = data["dos_x_negro"]
    puntos_negro = data["blackHorsePoints"]

    puntos_blanco = data["whiteHorsePoints"]
    dos_x_blanco = data["dos_x_blanco"]
    difficulty_level = data["difficultyLevel"]

    pos_x, pos_y = encontrar_posicion_caballo(matrix, 12)

    if pos_x is None or pos_y is None:
        return jsonify({"error": "No se encontró la posición del caballo negro en la matriz."}), 400

    resultado = mover_caballo(matrix, pos_x, pos_y, por_dos)

    nueva_matriz = None
    puntos_movimiento = 0
    dos_x_tomado = False

    for matriz, puntos_mov, dos_x in resultado:
        if matriz[row][col] == 12:
            nueva_matriz = matriz
            puntos_movimiento = puntos_mov
            dos_x_tomado = dos_x
            break

    if nueva_matriz is None:
        return jsonify({"error": "Movimiento no válido para el caballo negro."}), 400

    puntos_negro += puntos_movimiento
    # Actualizar la variable global matrix con la nueva matriz
    matrix = nueva_matriz
    response = {
        "message": "Movimiento realizado",
        "matrix": nueva_matriz,
        "blackHorsePoints": puntos_negro,
        "dos_x_negro": dos_x_tomado,
        "whiteHorsePoints": puntos_blanco,
        "dos_x_blanco": dos_x_blanco,
        "difficultyLevel": difficulty_level
    }

    print(response)

    return jsonify(response), 200



if __name__ == '__main__':
    app.run(debug=True)
