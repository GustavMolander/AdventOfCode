import time

with open("2024/aoc10_data_2.txt", "r") as f:
    data = f.read()
print(data)


class Topology:
    def __init__(self, data):

        # Add properties.
        self.trailheads = {}
        self.map = []   

        # Parse input.
        lines = data.split('\n')
        self.dimensions = len(lines)
        for line in lines:
            # covert to integer, then add to map list
            self.map.append(list(map(int, line)))


    def descend_from_all_peaks(self):
        for i in range(self.dimensions):
            for j in range(self.dimensions):
                if self.map[i][j] == 9:
                    self.find_lower_ground(i, j, (i,j))


    def add_trailheads(self):
        for i in range(self.dimensions):
            for j in range(self.dimensions):
                if self.map[i][j] == 0:
                    self.trailheads[(i,j)] = []


    def check_if_outside_grid(self, x, y):
        if x < 0 or x >= self.dimensions:
            return True
        if y < 0 or y >= self.dimensions:
            return True
        return False


    def find_lower_ground(self, x, y, original_peak):
        current_value = self.map[x][y]

        # If trailhead is reached, add original peak to trailheads.
        if self.map[x][y] == 0:
            if original_peak not in self.trailheads[(x,y)]: # Disable this line for Part 1.
                self.trailheads[(x,y)].append(original_peak)
            return

        # Check all 4 directions.
        for deltas in [(0,1), (1,0), (0,-1), (-1,0)]:
            new_x, new_y = x + deltas[0], y + deltas[1]

            if self.check_if_outside_grid(new_x, new_y):
                continue
            if self.map[new_x][new_y] == current_value-1:
                # We can descend here.
                self.find_lower_ground(new_x, new_y, original_peak)


def main():
    start_time = time.time()

    map = Topology(data)
    map.add_trailheads()
    map.descend_from_all_peaks()


    end_time = time.time()
    print(sum([len(map.trailheads[key]) for key in map.trailheads]))
    print(f"Time taken: {end_time - start_time} seconds")



main()
