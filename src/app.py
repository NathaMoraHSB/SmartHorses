#app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from src.functions.random_matrix import random_matrix
from src.functions.simular_partida import simular_partida


app = Flask(__name__)
CORS(app)
CORS(app, resources={r"/*": {"origins": "*"}})

#matrix = random_matrix()
matrix =  [
    [8, 0, 0, 0, 4, 0, 0, 20],
    [0, 20, 1, 0, 0, 12, 0, 0],
    [0, 0, 0, 9, 0, 0, 0, 0],
    [0, 7, 0, 0, 3, 0, 20, 0],
    [0, 11, 0, 0, 0, 0, 0, 0],
    [10, 0, 0, 0, 6, 0, 0, 0],
    [0, 0, 5, 0, 0, 0, 2, 0],
    [20, 0, 0, 0, 0, 0, 0, 0]
]


@app.route('/api/start', methods=['POST'])
def start_matrix():
    if matrix:
        return jsonify({"matrix": matrix})
    else:
        return jsonify({"error": "File not found"}), 404

@app.route('/api/partidaIaVSIa', methods=['POST'])
def run_simulation():

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


    historial_jugadas = simular_partida(matriz_inicial)


    report = {
        "result": "",
        "Puntos IA 1, caballo blanco": 0,
        "Puntos IA 2, caballo negro": 0
    }

    simulacion = []

    for nodo in historial_jugadas:
        simulacion.append(nodo.matriz)  # Agrega la matriz actual a la simulación
        report["Puntos IA 1, caballo blanco"] = nodo.puntos_blanco
        report["Puntos IA 2, caballo negro"] = nodo.puntos_negro

    # Determina el ganador según los puntos finales
    if report["Puntos IA 1, caballo blanco"] > report["Puntos IA 2, caballo negro"]:
        report["result"] = "Gana el caballo blanco"
    elif report["Puntos IA 1, caballo blanco"] < report["Puntos IA 2, caballo negro"]:
        report["result"] = "Gana el caballo negro"
    else:
        report["result"] = "Empate"

    print("repor", report)
    print("simulation", simulacion)

    # Retorna el conjunto de matrices de la simulación y el reporte final
    return jsonify({
        "simulation": simulacion,
        "report": report
    })

#se recibe matriz inicial y todos los valores puntos caballo negro y caballo blanco, dos_x caballo blanco
#@app.route('/api/machineMove', methods=['POST'])
#def machine_move():

@app.route('/api/human-move', methods=['POST'])
def human_move():
    # Obtener los datos enviados desde el frontend
    data = request.get_json()

    # Imprimir los datos en consola
    print("Datos recibidos desde el frontend:", data)

    # Responder al frontend con un mensaje de confirmación y los mismos datos
    response = {
        "message": "Datos recibidos",
        "data": data
    }

    # Retornar la respuesta como JSON
    return jsonify(response), 200



if __name__ == '__main__':
    app.run(debug=True)
