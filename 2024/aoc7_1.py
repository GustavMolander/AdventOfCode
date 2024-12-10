import time

start_time = time.time()

with open("aoc/aoc7_data_2.txt", "r") as f:
    data = f.read()

lines = data.split('\n')

def ternary(n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))

def apply_operator(operator_id: int, arguments: tuple[int, int]):
    if operator_id == 0:
        return arguments[0] + arguments[1]
    elif operator_id == 1:
        return arguments[0] * arguments[1]
    elif operator_id == 2:
        return int(str(arguments[0]) + str(arguments[1]))
    
total_sum = 0

for line in lines:
    split = line.split(':')
    target_sum = split[0]
    arguments = split[1].split(' ')[1:]
    arguments = [int(arg) for arg in arguments]

    combinations = 2**(len(arguments)-1)

    for combo in range(combinations):
        binary_combo = bin(combo)[2:].zfill(len(arguments)-1)
        sum = arguments[0]

        for i, char in enumerate(binary_combo):
            sum = apply_operator(int(char), (sum, arguments[i+1]))

        if sum == int(target_sum):
            total_sum += sum
            break

    


print(total_sum)

end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")
