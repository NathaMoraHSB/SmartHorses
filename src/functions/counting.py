#counting.py
from typing import List, Tuple
from src.types import Position, City_matrix

def counting(complete_path, city: City_matrix) -> Tuple[int, int, int, int]:
    sum_right = 0
    sum_left = 0
    sum_up = 0
    sum_down = 0

    number_low_cost = 0
    number_high_cost = 0
    number_medium_cost = 0

    last_point = None
    for point in complete_path:
        if last_point is None:
            last_point = point

        if city[point[0]][point[1]] == 0:
            number_low_cost = number_low_cost + 1
        if city[point[0]][point[1]] == 3:
            number_medium_cost = number_medium_cost + 4

        if city[point[0]][point[1]] == 4:
            number_high_cost = number_high_cost + 7

        if point[1] > last_point[1]:
            sum_right = sum_right + 1
            last_point = point

        if point[1] < last_point[1]:
            sum_left = sum_left + 1
            last_point = point

        if point[0] > last_point[0]:
            sum_down = sum_down + 1
            last_point = point

        if point[0] < last_point[0]:
            sum_up = sum_up + 1
            last_point = point

    return  number_low_cost, number_medium_cost, number_high_cost, sum_right, sum_left, sum_up, sum_down
