#app.py
from flask import Flask, request, jsonify
from flask_cors import CORS



from algorithms.a_star_search import a_star_search

from src.functions.random_matrix import random_matrix

app = Flask(__name__)
CORS(app)
CORS(app, resources={r"/*": {"origins": "*"}})

uploaded_matrix = None


@app.route('/api/start', methods=['POST'])
def start_simulation():
    matrix = random_matrix()

    if matrix:
        return jsonify({"matrix": matrix})
    else:
        return jsonify({"error": "File not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)