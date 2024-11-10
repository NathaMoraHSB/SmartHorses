#valid_position.py

from src.types import City_matrix

def valid_position(x: int, y: int, city: City_matrix) -> bool:
    rows = len(city)
    columns = len(city[0])

    if 0 <= x < rows and 0 <= y < columns and city[x][y] != 1:
        return True
