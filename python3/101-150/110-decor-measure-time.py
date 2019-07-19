#Using decorator to measure time


import time

def time_measure(f):
    t0 = time.time()
    f()
    t = time.time()
    return t - t0

#decorator
@time_measure   #decorator
def slow_code():
    time.sleep(2)

print(slow_code)
