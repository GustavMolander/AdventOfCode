import time

start_time = time.time()

ANTENNA_HASHMAP = {}
ANTINODES_HASHMAP = {}

with open("aoc/aoc8_data_2.txt", "r") as f:
    data = f.read()

lines = data.split('\n')
DIMENSIONS = len(lines)

def draw_antinodes():
    for key in ANTINODES_HASHMAP:
        x, y = key
        if lines[y][x] == '.':
            lines[y] = lines[y][:x] + '#' + lines[y][x+1:]
    for line in lines:
        print(line)

def check_outside_grid(tuple: tuple[int, int]):
    x, y = tuple
    return x < 0 or x >= DIMENSIONS or y < 0 or y >= DIMENSIONS


def add_antinodes(antenna_1: tuple[int, int], antenna_2: tuple[int, int]):
    diff = (antenna_1[0] - antenna_2[0], antenna_1[1] - antenna_2[1])

    antinode = (antenna_1[0], antenna_1[1])
    while not check_outside_grid(antinode):
        ANTINODES_HASHMAP[tuple(antinode)] = 0
        antinode = (antinode[0] + diff[0], antinode[1] + diff[1])


for j, line in enumerate(lines):
    for i, char in enumerate(line):
        if char.isalnum() or char.isdigit():
            if char in ANTENNA_HASHMAP:
                ANTENNA_HASHMAP[char].append((i,j))
            else:
                ANTENNA_HASHMAP[char] = [(i, j)]

for key in ANTENNA_HASHMAP:
    antenna_list = ANTENNA_HASHMAP[key]
    while len(antenna_list) > 1:
        antenna_1 = antenna_list.pop(0)
        for antenna_2 in antenna_list:
            add_antinodes(antenna_1, antenna_2)
            add_antinodes(antenna_2, antenna_1)


draw_antinodes()
end_time = time.time()
print(len(ANTINODES_HASHMAP))
print(f"Time taken: {end_time - start_time} seconds")
