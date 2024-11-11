# clase_nodo.py
class Nodo:
    def __init__(self, matriz, puntos_acumulados, dos_x, profundidad, padre=None):
        self.matriz = matriz
        self.puntos_acumulados = puntos_acumulados
        self.dos_x = dos_x
        self.profundidad = profundidad
        self.padre = padre
        self.hijos = []
