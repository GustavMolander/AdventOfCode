import time
from time import sleep


with open("2024/aoc12_data_1.data", "r") as f:
    data = f.read()
data = data.split("\n")
DIMENSIONS = len(data)


node_info = {} # (x,y) : (fences, node_type)
counted_nodes = {} # (x,y) : 1


def check_outide_bounds(x, y):
    if x < 0 or x >= DIMENSIONS or y < 0 or y >= DIMENSIONS:
        return True
    return False

def build_fences(data):
    for y in range(DIMENSIONS):
        for x in range(DIMENSIONS):
            fences = 0
            for direction in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
                if check_outide_bounds(x+direction[0], y+direction[1]):
                    fences += 1
                elif data[y][x] != data[y+direction[1]][x+direction[0]]:
                    fences += 1
            node_info[(x, y)] = (fences, data[y][x])


def calculate_field(x, y, node_type):
    if (x, y) in counted_nodes:
        # already counted
        return (0, 0)

    counted_nodes[(x, y)] = 1
    fences_n_area = (node_info[(x, y)][0], 1)

    for direction in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
        new_x, new_y = x+direction[0], y+direction[1]
        if not check_outide_bounds(new_x, new_y):
            if node_info[(new_x, new_y)][1] == node_type:
                new_fences, new_area = calculate_field(new_x, new_y, node_type)
                fences_n_area = (fences_n_area[0] + new_fences, fences_n_area[1] + new_area)

    return fences_n_area

def main():
    start_time = time.time()

    build_fences(data)

    sum = 0
    for y in range(DIMENSIONS):
        for x in range(DIMENSIONS):
            fences, area = calculate_field(x, y, data[y][x])
            sum += fences*area
    print(sum)

    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")


main()
