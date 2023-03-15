import time

n = 1000000
today = time.time()
result = sum(range(1, n+1))

print(result)
print(time.time()-today)


