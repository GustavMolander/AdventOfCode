import time

def check_outside_grid(x, y):
    return x < 0 or x >= DIMENSIONS or y < 0 or y >= DIMENSIONS

class Antenna:
    def __init__(self, char, x, y):
        self.frequency = char
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"{self.frequency} at ({self.x}, {self.y})"


with open("aoc/aoc8_data_2.txt", "r") as f:
    data = f.read()


start_time = time.time()

antenna_hashmap = {}
antinodes_hashmap = {}
lines = data.split('\n')
DIMENSIONS = len(lines)

for j, line in enumerate(lines):
    for i, char in enumerate(line):
        if char.isalnum() or char.isdigit():
            if char in antenna_hashmap:
                antenna_hashmap[char].append(Antenna(char, i, j))
            else:
                antenna_hashmap[char] = [Antenna(char, i, j)]

for key in antenna_hashmap:
    antenna_list = antenna_hashmap[key]
    while len(antenna_list) > 1:
        antenna_1 = antenna_list.pop(0)
        for antenna_2 in antenna_list:
            diff_x = antenna_1.x - antenna_2.x
            diff_y = antenna_1.y - antenna_2.y
            antinode_1 = (antenna_1.x + diff_x, antenna_1.y + diff_y)
            antinode_2 = (antenna_2.x - diff_x, antenna_2.y - diff_y)
            if not check_outside_grid(*antinode_1):
                antinodes_hashmap[str(antinode_1)] = 0
            if not check_outside_grid(*antinode_2):
                antinodes_hashmap[str(antinode_2)] = 0


print(len(antinodes_hashmap))

end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")
