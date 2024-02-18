import time
import matplotlib.pyplot as plt


# Recursive Approach
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


if __name__ == "__main__":
    testing_values = [5, 7, 10, 12, 15, 17, 20, 22, 25, 27, 30, 32, 35, 37, 40, 42, 45]
    execution_times = []

    for n in testing_values:
        start_time = time.time()
        fibonacci_recursive(n)
        end_time = time.time()
        execution_times.append(end_time - start_time)

    plt.plot(testing_values, execution_times, marker='o')
    plt.title('Execution Time of Recursive Fibonacci Algorithm')
    plt.xlabel('Index (n)')
    plt.ylabel('Execution Time (seconds)')
    plt.grid(True)
    plt.show()


