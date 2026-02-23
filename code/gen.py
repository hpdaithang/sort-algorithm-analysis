import numpy as np
import os

n = 1_000_000
os.makedirs("data", exist_ok=True)

# =========================
# Hàm ghi file
# =========================
def write_test(filename, arr):
    with open(filename, "w") as f:
        f.write(str(arr.size) + "\n")
        # chuyển sang list để join nhanh và ổn định
        f.write(" ".join(map(str, arr.tolist())))

# =========================
# TEST 1: TĂNG DẦN (INT)
# =========================
start = np.random.randint(-n, n)
steps = np.random.randint(1, n, size=n)
arr_inc = start + np.cumsum(steps)

write_test("data/test01_inc.txt", arr_inc)

# =========================
# TEST 2: GIẢM DẦN (INT)
# =========================
start = np.random.randint(n // 2, n)
steps = np.random.randint(1, n // 2, size=n)
arr_dec = start - np.cumsum(steps)

write_test("data/test02_dec.txt", arr_dec)

# =========================
# TEST 3 → 5: RANDOM INT
# =========================
for i in range(3, 6):
    arr_int = np.random.randint(
        -1_000_000_000,
        1_000_000_000,
        size=n,
        dtype=np.int64
    )
    write_test(f"data/test{str(i).zfill(2)}_rand_int.txt", arr_int)

# =========================
# TEST 6 → 10: RANDOM FLOAT
# =========================
for i in range(6, 11):
    arr_float = np.random.rand(n) * 100000
    write_test(f"data/test{str(i).zfill(2)}_rand_float.txt", arr_float)