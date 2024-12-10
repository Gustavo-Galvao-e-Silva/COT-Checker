from math import gcd


def phi(n: int) -> int:
    num_of_coprimes = 0
    for i in range(1, n + 1):
        if gcd(n, i) == 1:
            num_of_coprimes += 1

    return num_of_coprimes


def find_inverse_e(e: int, divisor: int) -> int:
    inverse = 0
    for i in range(divisor):
        if ((e * i) % divisor) == 1:
            inverse = i
            break

    return inverse
