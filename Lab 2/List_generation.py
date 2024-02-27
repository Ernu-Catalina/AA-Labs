import random


def generate_random_list(length, negative=False, dispersion=100000, range_start=1, range_end=100000, float_numbers=False):
    if float_numbers:
        return [random.uniform(range_start, range_end) for _ in range(length)]
    elif negative:
        return [random.randint(-dispersion, dispersion) for _ in range(length)]
    else:
        return [random.randint(range_start, range_end) for _ in range(length)]


List_1 = generate_random_list(5, negative=True, dispersion=1000)
List_2 = generate_random_list(25, dispersion=5000)
List_3 = generate_random_list(100, negative=True, range_end=50000)
List_4 = generate_random_list(250, float_numbers=True, range_end=100)
List_5 = generate_random_list(500, dispersion=50000)
List_6 = generate_random_list(1000, negative=True, dispersion=100000)
List_7 = generate_random_list(1500, float_numbers=True, range_end=1000)
List_8 = generate_random_list(3000, negative=True, range_end=10000)
List_9 = generate_random_list(10000, dispersion=1000000)
List_10 = generate_random_list(25000, float_numbers=True, range_end=1000000)