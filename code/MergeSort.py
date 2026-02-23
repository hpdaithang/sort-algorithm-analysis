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


def Merge(arr1, arr2):
    arr_f = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr_f.append(arr1[i])
            i += 1
        else:
            arr_f.append(arr2[j])
            j += 1

    while i < len(arr1):
        arr_f.append(arr1[i])
        i += 1

    while j < len(arr2):
        arr_f.append(arr2[j])
        j += 1

    return arr_f


def MergeSort(arr, l, r):
    if l < r:
        mid = (l + r) // 2

        arr1 = MergeSort(arr, l, mid)
        arr2 = MergeSort(arr, mid + 1, r)

        return Merge(arr1, arr2)
    else:
        return arr[l:l + 1]

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
sorted_arr = MergeSort(arr, 0, arr.size - 1)
end = time.perf_counter()

print("Time Taken:", (end - start) * 1000, "ms")