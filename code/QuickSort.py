import random
import time



def read_test(filename):
    with open(filename) as f:
        n = int(f.readline())
        line = f.readline().split()

        # tự nhận dạng int / float
        if "." in line[0]:
            arr = list(map(float, line))
        else:
            arr = list(map(int, line))

    return arr

def partition(arr, low, high):
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
        quickSort(arr, low, pivot-1)
        quickSort(arr, pivot+1, high)

name = 'data/test10_rand_float.txt'
arr = read_test(name)
start = time.time()
quickSort(arr, 0, len(arr)-1)

print(arr)
end = time.time()
elapsed = end - start
print("Time Taken:", elapsed * 1000, "ms")






# code được tham khảo tại https://www.geeksforgeeks.org/dsa/quick-sort-algorithm/