# clase_nodo.py

class Nodo:
    def __init__(self, matriz, puntos_blanco, puntos_negro, dos_x, profundidad, padre=None):
        self.matriz = matriz
        self.puntos_blanco = puntos_blanco
        self.puntos_negro = puntos_negro
        self.dos_x = dos_x
        self.profundidad = profundidad
        self.padre = padre
        self.hijos = []
