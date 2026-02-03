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

def Merge(arr1, arr2):
    arr_f = []
    ij = 0
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
        ij += 1
    while j < len(arr2):
        arr_f.append(arr2[j])
        j += 1
        ij += 1

    return arr_f

def MergeSort(arr, l, r):
    if l < r:
        mid = (l + r) // 2
        #print( l , r , mid )
        arr1 = MergeSort(arr, l, mid)
        arr2 = MergeSort(arr, mid + 1, r)
        #print(arr1)
        #print(arr2)
        arr_3 = Merge(arr1, arr2)
        return arr_3
    else:
        return arr[l:l + 1]

name = 'data/test01_inc.txt'
arr = read_test(name)
start = time.time()
MergeSort(arr, 0, len(arr) - 1)
end = time.time()
print(arr)

elapsed = end - start
print("Time Taken:", elapsed * 1000, "ms")