# mejor_hoja_max_profundidad.py contiene la función mejor_hoja_max_profundidad

#aquí solo se tiene encuenta la mayor cantidad de puntos que pueda hacer el caballo blanco
def mejor_hoja_max_profundidad(nodo_raiz, profundidad_objetivo):
    # Lista para almacenar los nodos en la profundidad objetivo
    hojas_en_profundidad = []

    def recorrer_nodos(nodo):
        if nodo.profundidad == profundidad_objetivo:
            hojas_en_profundidad.append(nodo)
        for hijo in nodo.hijos:
            recorrer_nodos(hijo)


    recorrer_nodos(nodo_raiz)


    mejor_hoja = max(
        hojas_en_profundidad,
        key=lambda nodo: (nodo.puntos_blanco, nodo.puntos_negro)  # Ordena por puntos blanco, luego puntos negro
    )

    return mejor_hoja
