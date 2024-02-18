import time
import numpy as np
import matplotlib.pyplot as plt


# Using Matrix Exponentiation
def fibonacci_matrix_exponentiation(n):
    F = np.array([[1, 1], [1, 0]], dtype=object)
    if n == 0:
        return 0
    try:
        power = np.linalg.matrix_power(F, n - 1)
        return power[0][0]
    except OverflowError:
        print("Overflow error occurred for n =", n)
        return None


if __name__ == "__main__":
    testing_values = [501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000]
    execution_times = []

    for n in testing_values:
        start_time = time.time()
        fibonacci_matrix_exponentiation(n)
        end_time = time.time()
        execution_times.append(end_time - start_time)

    # Plotting the graph
    plt.plot(testing_values, execution_times, marker='o')
    plt.title('Execution Time of Fibonacci Algorithm using Matrix Exponentiation')
    plt.xlabel('Index (n)')
    plt.ylabel('Execution Time (seconds)')
    plt.grid(True)
    plt.show()
