import time
def first_attempt():
    start_time = time.time()
    with open("aoc/aoc9_data_2.txt", "r") as f:
        data = f.read()
    int_list = expand_string(data)

    compacted_list = compact_memory(int_list)
    print(calculate_checksum(compacted_list))

    end_time = time.time()
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



def expand_string(input: str):
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
    return output

def compact_memory(int_list):
    forward_index = 0
    backward_index = len(int_list) - 1
    while True:
        if int_list[forward_index] != -1:
            forward_index += 1
            continue
        if int_list[backward_index] == -1:
            backward_index -= 1
            continue
        if forward_index < backward_index:
            tmp = int_list[forward_index]
            int_list[forward_index] = int_list[backward_index]
            int_list[backward_index] = tmp
            forward_index += 1
            backward_index -= 1
        else:
            break
    return int_list







first_attempt()
