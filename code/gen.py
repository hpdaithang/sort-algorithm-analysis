import random
import os

n = 1_000_000
os.makedirs("data", exist_ok=True)

def write_test(filename, arr):
    with open(filename, "w") as f:
        f.write(str(len(arr)) + "\n")
        f.write(" ".join(map(str, arr)))

# ===== TEST 1: TĂNG DẦN (INT) =====
arr_inc = [random.randint(-n, n)]
for _ in range(1, n):
    arr_inc.append(arr_inc[-1] + random.randint(1, n))
write_test("data/test01_inc.txt", arr_inc)

# ===== TEST 2: GIẢM DẦN (INT) =====
arr_dec = [random.randint(n // 2, n)]
for _ in range(1, n):
    arr_dec.append(arr_dec[-1] - random.randint(1, n // 2))
write_test("data/test02_dec.txt", arr_dec)

# ===== TEST 3 → 5: RANDOM INT =====
for i in range(3, 6):
    arr_int = [random.randint(-1_000_000_000, 1_000_000_000) for _ in range(n)]
    write_test(f"data/test{str(i).zfill(2)}_rand_int.txt", arr_int)

# ===== TEST 6 → 10: RANDOM FLOAT =====
for i in range(6, 11):
    arr_float = [(random.random() * 100000) for _ in range(n)]
    write_test(f"data/test{str(i).zfill(2)}_rand_float.txt", arr_float)
