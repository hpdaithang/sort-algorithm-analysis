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


def MaxHeap(arr, i, n):
    left_tree = i * 2 + 1
    right_tree = i * 2 + 2
    largest = i

    if left_tree < n and arr[left_tree] > arr[largest]:
        largest = left_tree
    if right_tree < n and arr[right_tree] > arr[largest]:
        largest = right_tree

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        MaxHeap(arr, largest, n)


def HeapSort(arr, n):
    for i in range(n // 2 - 1, -1, -1):
        MaxHeap(arr, i, n)


    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        MaxHeap(arr, 0, i)


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
HeapSort(arr, arr.size)
end = time.perf_counter()

print("Time Taken:", (end - start) * 1000, "ms")