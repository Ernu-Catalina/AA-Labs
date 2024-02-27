import random


def generate_random_list(length):
    return [random.randint(1, 100000) for _ in range(length)]


List_1 = generate_random_list(5)
List_2 = generate_random_list(25)
List_3 = generate_random_list(100)
List_4 = generate_random_list(250)
List_5 = generate_random_list(500)
List_6 = generate_random_list(1000)
List_7 = generate_random_list(1500)
List_8 = generate_random_list(3000)
List_9 = generate_random_list(10000)
List_10 = generate_random_list(25000)