#quick_sorty

import time
import matplotlib.pyplot as plt
from List_generation import *


# Quicksort algorithm
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


# Measure execution time and perform quicksort on each list
lists = [List_1, List_2, List_3, List_4, List_5, List_6, List_7, List_8, List_9, List_10]
execution_times = []

for i, lst in enumerate(lists):
    start_time = time.time()
    sorted_list = quicksort(lst)
    end_time = time.time()
    execution_times.append(end_time - start_time)

    print(f"Sorted List {i+1}: {sorted_list}")

# Plot execution times on a graph
plt.plot(range(1, 11), execution_times, marker='o')
plt.title('Quicksort Execution Time for Various Lists')
plt.xlabel('List Number')
plt.ylabel('Execution Time (seconds)')
plt.grid(True)
plt.show()
