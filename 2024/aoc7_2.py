import time

with open("aoc/aoc7_data_2.txt", "r") as f:
    data = f.read()

def op1(a,b): return a+b
def op2(a,b): return a*b
def op3_st(a,b): return int(str(a)+str(b))
def op3_math(a: int,b: int):
    count = 1
    b_copy = b
    while b_copy/10 > 0:
        b_copy = b_copy/10
        count+=1
    return a*10**count + b

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


def is_valid_combination(target_sum: int, arguments: list[int]):
    if len(arguments) == 1:
        return 
    first_arg = arguments[0]
    rest_args = arguments[1:]
    target_sum_1 = op1(first_arg, is_valid_combination(rest_args[0], rest_args[1:]))
    target_sum_2 = op2(first_arg, is_valid_combination(rest_args[0], rest_args[1:]))
    target_sum_3 = op3_st(first_arg, is_valid_combination(rest_args[0], rest_args[1:]))
    if target_sum == target_sum_1:
        return True
    elif target_sum == target_sum_2:
        return True
    elif target_sum == target_sum_3:
        return True
    return False


# second attempt.
def second_attempt():
    start_time = time.time()
    lines = data.split('\n')

    # Parse input.
    for line in lines:
        split = line.split(' ')
        target_sum = split[0].replace(':', '')
        arguments = [int(arg) for arg in split[1:]]

        if is_valid_combination(int(target_sum), arguments):
            print(target_sum)
            exit()




    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")
    
# first attempt.
def initial_solution():
    start_time = time.time()
    total_sum = 0
    lines = data.split('\n')

    for line in lines:
        split = line.split(' ')
        target_sum = split[0].replace(':', '')
        arguments = [int(arg) for arg in split[1:]]

        combinations = 3**(len(arguments)-1)

        for combo in range(combinations):
            ternary_combo = ternary(combo).zfill(len(arguments)-1)
            sum = arguments[0]

            for i, char in enumerate(ternary_combo):
                sum = apply_operator(int(char), (sum, arguments[i+1]))

            if sum == int(target_sum):
                print("sum found with combo", ternary_combo)
                total_sum += sum
                break

    
    print(total_sum)

    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")

second_attempt()