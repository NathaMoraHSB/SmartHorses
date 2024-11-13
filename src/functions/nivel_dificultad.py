# nivel_de_dificultad.py
def nivel_de_dificultad(nivel):
    if nivel == 1:
        profundidad_maxima = 2  # Principiante
    elif nivel == 2:
        profundidad_maxima = 4  # Amateur
    elif nivel == 3:
        profundidad_maxima = 6  # Experto
    else:
        raise ValueError("Nivel no válido. Debe ser 1 (Principiante), 2 (Amateur) o 3 (Experto).")

    return profundidad_maxima
