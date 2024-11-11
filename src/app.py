#app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from src.functions.random_matrix import random_matrix
from src.functions.puntos_peor_caso import simular_partida

app = Flask(__name__)
CORS(app)
CORS(app, resources={r"/*": {"origins": "*"}})

matrix = random_matrix()


@app.route('/api/start', methods=['POST'])
def start_simulation():
    if matrix:
        return jsonify({"matrix": matrix})
    else:
        return jsonify({"error": "File not found"}), 404

@app.route('/api/partida', methods=['POST'])
def run_simulation():

    matriz_inicial = [
        [8, 0, 0, 0, 4, 0, 0, 20],
        [0, 20, 1, 0, 0, 12, 0, 0],
        [0, 0, 0, 9, 0, 0, 0, 0],
        [7, 0, 3, 0, 20, 0, 0, 0],
        [10, 0, 0, 6, 0, 0, 0, 0],
        [20, 5, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
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

    # Retorna el conjunto de matrices de la simulación y el reporte final
    return jsonify({
        "simulation": simulacion,
        "report": report
    })


if __name__ == '__main__':
    app.run(debug=True)
