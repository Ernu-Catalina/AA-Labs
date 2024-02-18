import time
import matplotlib.pyplot as plt


# Using Dynamic Programming (Memoization)
def fibonacci_memoization(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]


if __name__ == "__main__":
    testing_values = [501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000]
    execution_times = []

    for n in testing_values:
        start_time = time.time()
        fibonacci_memoization(n)
        end_time = time.time()
        execution_times.append(end_time - start_time)

    plt.plot(testing_values, execution_times, marker='o')
    plt.title('Execution Time of Fibonacci Algorithm using Dynamic Programming (Memoization)')
    plt.xlabel('Index (n)')
    plt.ylabel('Execution Time (seconds)')
    plt.grid(True)
    plt.show()
