import time
import matplotlib.pyplot as plt
from mpmath import mp

# Set the precision
mp.dps = 1000  # Adjust this value as needed


# Using Binet's Formula with mpmath
def fibonacci_binet_formula(n):
    sqrt5 = mp.sqrt(5)
    phi = (1 + sqrt5) / 2
    return int((phi ** n - (-phi) ** -n) / sqrt5)


if __name__ == "__main__":
    testing_values = [501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000]
    execution_times = []

    for n in testing_values:
        start_time = time.time()
        fibonacci_binet_formula(n)
        end_time = time.time()
        execution_times.append(end_time - start_time)

    plt.plot(testing_values, execution_times, marker='o')
    plt.title("Execution Time of Fibonacci Algorithm using Binet's Formula (with mpmath)")
    plt.xlabel('Index (n)')
    plt.ylabel('Execution Time (seconds)')
    plt.grid(True)
    plt.show()
