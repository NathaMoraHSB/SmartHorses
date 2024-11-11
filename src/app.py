#app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from src.functions.random_matrix import random_matrix

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

def run_simulation():
    global matrix


    report = {
        "result": "decir quien gano",
        "Puntos IA 1": 0,
        "Puntos totales IA 2": 0,
    }

    return jsonify({
        "simulation": [matrix],#el conjunto de matrices para simular el juego
        "report": report
    })


if __name__ == '__main__':
    app.run(debug=True)
