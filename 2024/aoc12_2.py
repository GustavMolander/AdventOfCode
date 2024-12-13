import time
from time import sleep


with open("2024/aoc12_data_2.data", "r") as f:
    data = f.read()
data = data.split("\n")
DIMENSIONS = len(data)


node_info = {} # (x,y) : (Node)
counted_nodes = {} # (x,y) : 1

class Node:
    def __init__(self, x, y, node_type):
        self.node_type = node_type
        self.x = x
        self.y = y
        self.north_fence = False
        self.east_fence = False
        self.south_fence = False
        self.west_fence = False
        self.borders = 0 # Not counted yet.

    def __str__(self):
        return f"Node at ({self.x}, {self.y}) with type {self.node_type} and borders {self.borders}, and fences n e s w {self.north_fence}, {self.east_fence}, {self.south_fence}, {self.west_fence}"


def check_outide_bounds(x, y):
    if x < 0 or x >= DIMENSIONS or y < 0 or y >= DIMENSIONS:
        return True
    return False

def find_if_fence(data, x,y, node_type):
    if check_outide_bounds(x, y):
        return True
    elif data[y][x] != node_type:
        return True
    return False

# Should be done first.
def build_fences(data):
    for y in range(DIMENSIONS):
        for x in range(DIMENSIONS):
            node = Node(x, y, data[y][x])

            # Build fences in all directions. North, East, South, West
            node.north_fence = find_if_fence(data, x, y-1, node.node_type)
            node.east_fence = find_if_fence(data, x+1, y, node.node_type)
            node.south_fence = find_if_fence(data, x, y+1, node.node_type)
            node.west_fence = find_if_fence(data, x-1, y, node.node_type)

            node_info[(x, y)] = node

# Can be done after build_fences.
def calculate_borders():
    for x in range(DIMENSIONS):
        for y in range(DIMENSIONS):
            current_node = node_info[(x, y)]
            prelimilary_borders = current_node.north_fence + current_node.east_fence + current_node.south_fence + current_node.west_fence

            # Check west node.
            if not find_if_fence(data, x-1, y, current_node.node_type):
                # The west node is in the same group, and could potentially already have claimed north or south border.
                west_node = node_info[(x-1, y)]
                if west_node.north_fence and current_node.north_fence:
                    prelimilary_borders -= 1
                if west_node.south_fence and current_node.south_fence:
                    prelimilary_borders -= 1

            # Check north node.
            if not find_if_fence(data, x, y-1, current_node.node_type):
                # The north node is in the same group, and could potentially already have claimed east or west border.
                north_node = node_info[(x, y-1)]
                if north_node.east_fence and current_node.east_fence:
                    prelimilary_borders -= 1
                if north_node.west_fence and current_node.west_fence:
                    prelimilary_borders -= 1

            current_node.borders = prelimilary_borders
            node_info[(x, y)] = current_node



def calculate_field(x, y, node_type):
    if (x, y) in counted_nodes:
        # already counted
        return (0, 0)

    counted_nodes[(x, y)] = 1
    current_node = node_info[(x, y)]
    borders = current_node.borders
    area = 1

    for direction in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
        new_x, new_y = x+direction[0], y+direction[1]
        if not find_if_fence(data, new_x, new_y, current_node.node_type):
            additional_borders, additional_area = calculate_field(new_x, new_y, node_type)
            borders += additional_borders
            area += additional_area

    return (borders, area)

def main():
    start_time = time.time()

    build_fences(data)
    calculate_borders()

    sum = 0

    for y in range(DIMENSIONS):
        for x in range(DIMENSIONS):
            borders, area = calculate_field(x, y, data[y][x])
            sum += borders*area
    print(sum)

    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")


main()
