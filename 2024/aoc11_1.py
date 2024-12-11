import time
from time import sleep


with open("2024/aoc11_data_1.data", "r") as f:
    data = f.read()

data = [int(i) for i in data.split(" ")]
BLINKS = 75

def get_value_digits(number: int) -> int:
    value_digits = 1
    while number // 10 > 0:
        value_digits += 1
        number = number // 10
    return value_digits

def apply_rule(number) -> list[int]:
    # Rule 1:
    if number == 0:
        return [1] 

    # Rule 2:
    value_digits = get_value_digits(number)
    if value_digits % 2 == 0:
        first_half = number // int(10**(value_digits/2))
        second_half = number % int(10**(value_digits/2))
        return [first_half, second_half]

    # Rule 3:
    return [number*2024]

class StoneVault:
    def __init__(self, data: list[int]):
        self.conversion_cache = {} # Stone value: list of stone values after blink
        self.stone_vault_dict = {} # Stone value: number of stones
        for number in data:
            self.stone_vault_dict[number] = 1

    def execute_blink(self):
        stone_vault_dict_new = {}

        for key in self.stone_vault_dict:
            value = self.stone_vault_dict[key]
            if value == 0:
                # We dont have any stones of this type.
                continue

            if key not in self.conversion_cache:
                # We have not done this calculation yet.
                self.conversion_cache[key] = apply_rule(key)

            conversion_result = self.conversion_cache[key]
            for element in conversion_result:
                stone_vault_dict_new[element] = stone_vault_dict_new.get(element, 0) + value

        self.stone_vault_dict = stone_vault_dict_new
            
def main():
    start_time = time.time()

    stone_vault = StoneVault(data)
    
    for i in range(BLINKS):
        stone_vault.execute_blink()


    # sum all values in stone_vault_dict values
    print(sum(stone_vault.stone_vault_dict.values()))

    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")


main()
