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

name = 'data/test10_rand_float.txt'
arr = read_test(name)
start = time.time()
arr.sort()
end = time.time()
print(arr)

elapsed = end - start
print("Time Taken:", elapsed * 1000, "ms")