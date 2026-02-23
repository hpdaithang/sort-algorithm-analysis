import numpy as np
import time

def read_test(filename):
    with open(filename) as f:
        n = int(f.readline())
        line = f.readline().split()

        # tự nhận dạng int / float
        if "." in line[0]:
            arr = np.array(line, dtype=float)
        else:
            arr = np.array(line, dtype=np.int64)

    return arr


import numpy as np

def partition(arr, low, high):
    pivot_index = np.random.randint(low, high + 1)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

    pivot = arr[high]
    left = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            left += 1
            arr[left], arr[j] = arr[j], arr[left]

    left += 1
    arr[left], arr[high] = arr[high], arr[left]
    return left

def quickSort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quickSort(arr, low, pivot - 1)
        quickSort(arr, pivot + 1, high)

name1 = 'data/test01_inc.txt'
name2 = 'data/test02_dec.txt'
name3 = 'data/test03_rand_int.txt'
name4 = 'data/test04_rand_int.txt'
name5 = 'data/test05_rand_int.txt'
name6 = 'data/test06_rand_float.txt'
name7 = 'data/test07_rand_float.txt'
name8 = 'data/test08_rand_float.txt'
name9 = 'data/test09_rand_float.txt'
name10 = 'data/test10_rand_float.txt'
arr = read_test(name10)

start = time.perf_counter()
quickSort(arr, 0, arr.size - 1)
end = time.perf_counter()
# print(arr)
print("Time Taken:", (end - start) * 1000, "ms")