import time
with open("aoc/aoc9_data_2.txt", "r") as f:
    data = f.read()


class FreeSpace:
    def __init__(self, input: str):
        # Create a memory list from the input string
        current_id = 0
        output = []
        free_space = False
        for char in input:
            n = int(char)
            if free_space:
                output.extend([-1] * n)
                free_space = False
            else: 
                output.extend([current_id] * n)
                free_space = True
                current_id += 1
        self.memory_list = output
        # Create a free space dictionary
        self.free_space_dict = {}

    def add_free_space_to_dict(self, start, size):
        if size in self.free_space_dict:
            free_space_queue = self.free_space_dict[size]

            # Use binary search to find insertion point in queue
            left, right = 0, len(free_space_queue)
            while left < right:
                # Integer division
                mid = (left + right) // 2
                if free_space_queue[mid] < start:
                    left = mid + 1
                else:
                    right = mid
            # Right and left are now the same.
            free_space_queue.insert(left, start)
        else:
            # if dict is empty, add the start to the list
            self.free_space_dict[size] = [start]
    
    def initial_dict_fill(self):
        continuous_free_space = 0
        for i in range(len(self.memory_list)):
            if self.memory_list[i] == -1:
                continuous_free_space += 1
            else:
                if continuous_free_space > 0:
                    # Adding free space to the dictionary
                    self.add_free_space_to_dict(i - continuous_free_space, continuous_free_space)
                continuous_free_space = 0

    def use_earliest_free_space(self, size, index):
        current_earliest_free_space = None
        current_earliest_free_space_key = None

        for key in sorted(self.free_space_dict.keys()):
            if key < size:
                continue

            if len(self.free_space_dict[key]) > 0 and self.free_space_dict[key][0] < index:
                if current_earliest_free_space is None:
                    # Handle first case.
                    current_earliest_free_space = self.free_space_dict[key][0]
                    current_earliest_free_space_key = key
                else:
                    # Handle other cases.
                    if self.free_space_dict[key][0] < current_earliest_free_space:
                        current_earliest_free_space = self.free_space_dict[key][0]
                        current_earliest_free_space_key = key

        if current_earliest_free_space is None:
            return -1
        else:
            index = self.free_space_dict[current_earliest_free_space_key].pop(0)
            self.add_free_space_to_dict(index + size, current_earliest_free_space_key - size)
            return index


    def move_bits(self, origin, destination, size):
        for i in range(size):
            tmp = self.memory_list[origin + i]
            self.memory_list[origin + i] = self.memory_list[destination + i]
            self.memory_list[destination + i] = tmp
        
            


def first_attempt():
    start_time = time.time()

    free_space = FreeSpace(data)
    free_space.initial_dict_fill()

    # Move all blocks in the end to memory space in the beginning.
    block_size = 0
    for i in range(len(free_space.memory_list)):
        index = len(free_space.memory_list) - i - 1
        next_bit_index = index - 1
        if next_bit_index < 0:
            break
        current_bit = free_space.memory_list[index]
        next_bit = free_space.memory_list[next_bit_index]
        if current_bit != -1:
            # Block found.
            block_size += 1
            if current_bit != next_bit:
                # End of block found.
                new_index = free_space.use_earliest_free_space(block_size, index)
                if new_index == -1:
                    # No free space found.
                    pass
                else: 
                    free_space.move_bits(index, new_index, block_size)
                block_size = 0


    # print()
    # print_str(free_space.memory_list)
    # print(free_space.memory_list)
    # print(free_space.free_space_dict)


    end_time = time.time()
    print(calculate_checksum(free_space.memory_list))
    print(f"Time taken: {end_time - start_time} seconds")

def print_str(int_list):
    copy_int_list = int_list.copy()
    for i in range(len(copy_int_list)):
        if copy_int_list[i] == -1:
            copy_int_list[i] = "."
    print("".join(map(str, copy_int_list)))

def calculate_checksum(int_list):
    checksum = 0
    for i in range(len(int_list)):
        if int_list[i] != -1:
            checksum += i*int_list[i]
    return checksum


first_attempt()
