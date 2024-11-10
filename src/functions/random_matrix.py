import random

def random_matrix(size=8):
    matrix = [[0 for _ in range(size)] for _ in range(size)]

    point_positions = random.sample([(i, j) for i in range(size) for j in range(size)], 10)
    for pos in point_positions:
        matrix[pos[0]][pos[1]] = random.randint(1, 10)

    x2_positions = random.sample([pos for pos in [(i, j) for i in range(size) for j in range(size)] if pos not in point_positions], 4)
    for pos in x2_positions:
        matrix[pos[0]][pos[1]] = 20

    horse_positions = random.sample([pos for pos in [(i, j) for i in range(size) for j in range(size)] if pos not in point_positions and pos not in x2_positions], 2)
    matrix[horse_positions[0][0]][horse_positions[0][1]] = 11
    matrix[horse_positions[1][0]][horse_positions[1][1]] = 12

    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

smart_horses_matrix = random_matrix()
print_matrix(smart_horses_matrix)
