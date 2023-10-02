import random
import timeit
import math

from main import (
    add_lists,
    subtract_lists,
    number_to_list,
    multiply_lists,
    compare_lists,
    list_to_number,
    divide_lists,
    modulo_lists,
    isqrt_list,
)


def generate_random_number(size):
    return random.randint(2**size, 2 ** (size + 1) - 1)


def run_tests():
    for _ in range(1):  # Adjust the number of tests as needed
        num1 = generate_random_number(2000)

        list1 = number_to_list(num1)

        # isqrt_list
        # result = isqrt_list(list1)
        math.isqrt(num1)

        print("isqrt_list: OK")


if __name__ == "__main__":
    runtime = timeit.timeit(run_tests, number=1)
    print("Time: ", runtime)
