#bucket_sort

import time
import matplotlib.pyplot as plt
from List_generation import *


def bucket_sort(arr):
    # Find maximum and minimum values in the array
    max_val, min_val = max(arr), min(arr)
    range_val = max_val - min_val + 1

    range_val = int(range_val)
    buckets = [[] for _ in range(range_val)]

    # Fill buckets
    for num in arr:
        buckets[int(num - min_val)].append(num)

    # Concatenate buckets
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    return sorted_arr


# Measure execution time and perform cocktail sort on each list
lists = [List_1, List_2, List_3, List_4, List_5, List_6, List_7, List_8, List_9, List_10]
execution_times = []

for i, lst in enumerate(lists):
    start_time = time.time()
    bucket_sort(lst)
    end_time = time.time()
    execution_times.append(end_time - start_time)

    print(f"Sorted List {i+1}: {lst}")

# Plot execution times on a graph
plt.plot(range(1, 11), execution_times, marker='o')
plt.title('Cocktail Shaker Sort Execution Time for Various Lists')
plt.xlabel('List Number')
plt.ylabel('Execution Time (seconds)')
plt.grid(True)
plt.show()
