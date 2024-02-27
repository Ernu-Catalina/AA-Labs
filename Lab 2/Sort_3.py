#heap_sort

import time
import matplotlib.pyplot as plt
from List_generation import *


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


# Measure execution time and perform heapsort on each list
lists = [List_1, List_2, List_3, List_4, List_5, List_6, List_7, List_8, List_9, List_10]
execution_times = []

for i, lst in enumerate(lists):
    start_time = time.time()
    heap_sort(lst)
    end_time = time.time()
    execution_times.append(end_time - start_time)

    print(f"Sorted List {i+1}: {lst}")

# Plot execution times on a graph
plt.plot(range(1, 11), execution_times, marker='o')
plt.title('Heapsort Execution Time for Various Lists')
plt.xlabel('List Number')
plt.ylabel('Execution Time (seconds)')
plt.grid(True)
plt.show()