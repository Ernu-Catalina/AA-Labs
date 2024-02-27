#cocktail_sort

import time
import matplotlib.pyplot as plt
from List_generation import *


def cocktail_sort(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1

    while swapped:
        swapped = False

        # Forward pass
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        if not swapped:
            break

        swapped = False
        end -= 1

        # Backward pass
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        start += 1


# Measure execution time and perform cocktail sort on each list
lists = [List_1, List_2, List_3, List_4, List_5, List_6, List_7, List_8, List_9, List_10]
execution_times = []

for i, lst in enumerate(lists):
    start_time = time.time()
    cocktail_sort(lst)
    end_time = time.time()
    execution_times.append(end_time - start_time)

    print(f"Sorted List {i+1}: {lst}")

# Plot execution times on a graph
plt.plot([len(lst) for lst in lists], execution_times, marker='o')
plt.title('Cocktail Shaker Sort Execution Time for Various List Lengths')
plt.xlabel('List Length')
plt.ylabel('Execution Time (seconds)')
plt.grid(True)
plt.show()
