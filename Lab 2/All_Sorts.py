import time
import matplotlib.pyplot as plt
from List_generation import *


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


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


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


lists = [List_1, List_2, List_3, List_4, List_5, List_6, List_7, List_8, List_9, List_10]
execution_times_merge_sort = []
execution_times_quicksort = []
execution_times_heap_sort = []
execution_times_bucket_sort = []

for i, lst in enumerate(lists):
    # Merge sort
    start_time = time.time()
    merge_sort(lst.copy())
    end_time = time.time()
    execution_times_merge_sort.append(end_time - start_time)

    # Quicksort
    start_time = time.time()
    quicksort(lst.copy())
    end_time = time.time()
    execution_times_quicksort.append(end_time - start_time)

    # Heapsort
    start_time = time.time()
    heap_sort(lst.copy())
    end_time = time.time()
    execution_times_heap_sort.append(end_time - start_time)

    # Bucket sort
    start_time = time.time()
    bucket_sort(lst.copy())
    end_time = time.time()
    execution_times_bucket_sort.append(end_time - start_time)

# Plot execution times for each sort
plt.figure(figsize=(10, 6))

plt.plot(range(1, len(lists) + 1), execution_times_merge_sort, label='Merge Sort', marker='o')
plt.plot(range(1, len(lists) + 1), execution_times_quicksort, label='Quicksort', marker='o')
plt.plot(range(1, len(lists) + 1), execution_times_heap_sort, label='Heapsort', marker='o')
plt.plot(range(1, len(lists) + 1), execution_times_bucket_sort, label='Bucket Sort', marker='o')

plt.title('Sorting Algorithm Execution Time for Various List Lengths')
plt.xlabel('List Number')
plt.ylabel('Execution Time (seconds)')
plt.legend()
plt.grid(True)
plt.xticks(range(1, len(lists) + 1))
plt.show()

