import numpy as np
import time


def generate_map(m, n):
    arr = np.random.rand(m, n)
    return np.round(arr).tolist()


ocean_map = generate_map(3000, 5000)

today = time.time()
print(sum(row.count(1) for row in ocean_map))
print(time.time()-today)