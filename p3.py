def get_u_number() -> str:
    return input("U-number (without U): ")


def calculate_x_list(u_number: str) -> list[int]:
    return [(int(u_number[i]) + 10 * (i + 1)) for i in range(len(u_number))]


def calculate_decrypted_list(x_list: list[int], d: int, divisor: int) -> list[int]:
    arr = []
    for i in range(len(x_list)):
        arr.append((int(x_list[i]) ** d) % divisor)

    return arr


def print_u_number_table(u_number: str, x_list: list[int], list_decrypted: list[int]) -> None:
    print(f"{'Digit(t)':<10} {'x = 10k + t':<20} {'D(x)'}")
    for i in range(len(u_number)):
        print(f"{(i + 1):<10} {(10 * (i + 1) + int(u_number[i])):<20} {list_decrypted[i]}")


def encrypt_u_number(decrypted_arr: list[int], divisor: int, e: int) -> str:
    string = ""
    for i in range(len(decrypted_arr)):
        string += str(((decrypted_arr[i] ** e) % divisor) - 10 * (i + 1))

    return string
