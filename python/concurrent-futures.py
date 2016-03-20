from time import time
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor

def gcd(pair):
    a, b = pair
    low = min(a, b)
    for i in range(low, 0, -1):
        if a % i == 0 and b % i == 0:
            return i


numbers = [(1963309, 2265973), (2030677, 3814172),
           (1551645, 2229620), (2039045, 2020802)]

start = time()

# No threading
#results = list(map(gcd, numbers))

# Threads -- actually slower!
#pool = ThreadPoolExecutor(max_workers=2)

# Threads running on different processes
pool = ProcessPoolExecutor(max_workers=2)

results = list(pool.map(gcd, numbers))

end = time()
print('Took %.3f seconds' % (end - start))