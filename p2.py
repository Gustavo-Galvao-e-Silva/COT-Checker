def print_powers_of_two(exponent_in_binary: str) -> None:
    print("Powers of two: ", end="")
    for i in range(len(exponent_in_binary)):
        if exponent_in_binary[i] == '0':
            continue
        else:
            print(2 ** (len(exponent_in_binary) - i - 1), end=" + ")

    print("")


def convert_to_binary(num: int) -> str:
    binary = bin(num)[2::]
    return binary


def calculate_mod_e_powers_of_two(e: int, max_power_of_two: int, divisor: int) -> list[int]:
    arr = []
    previous_remainder = e % divisor
    arr.append(previous_remainder)
    for i in range(1, max_power_of_two + 1):
        current_remainder = (previous_remainder ** 2) % divisor
        arr.append(current_remainder)
        previous_remainder = current_remainder
    return arr


def calculate_mod_from_powers_of_two(arr: list[int], divisor: int, binary_exponent: str) -> int:
    product = 1
    rev = binary_exponent[::-1]
    for i in range(len(binary_exponent)):
        if rev[i] == '1':
            product *= arr[i]

    result = product % divisor
    return result


def print_powers_mod(arr: list[int], binary_exponent: str) -> None:
    rev = binary_exponent[::-1]
    print(f"{'Result':<10} {'Check':<5}")
    length = len(binary_exponent)
    for i in range(length):
        if rev[i] == '1':
            print(f"{arr[i]:<10} {'\u2713':<5}")
        else:
            print(f"{arr[i]:<10}")
