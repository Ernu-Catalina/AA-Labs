#merge_sort

import time
import matplotlib.pyplot as plt
from List_generation import *


# Merge sort algorithm
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    result.extend(left[left_idx:])
    result.extend(right[right_idx:])

    return result


lists = [List_1, List_2, List_3, List_4, List_5, List_6, List_7, List_8, List_9, List_10]
execution_times = []

for i, lst in enumerate(lists):
    start_time = time.time()
    sorted_list = merge_sort(lst)
    end_time = time.time()
    execution_times.append(end_time - start_time)

    print(f"Sorted List {i+1}: {sorted_list}")

# Plot execution times on a graph
plt.plot([len(lst) for lst in lists], execution_times, marker='o')
plt.title('Merge Sort Execution Time for Various List Lengths')
plt.xlabel('List Length')
plt.ylabel('Execution Time (seconds)')
plt.grid(True)
plt.show()
