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

def MaxHeap(arr,i, n):
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
    for i in range(n // 2, -1, -1):
        MaxHeap(arr, i, n)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        MaxHeap(arr, 0, i)

name = 'data/test01_inc.txt'
arr = read_test(name)
start = time.time()
HeapSort(arr, len(arr))
end = time.time()
print(arr)

elapsed = end - start
print("Time Taken:", elapsed * 1000, "ms")


