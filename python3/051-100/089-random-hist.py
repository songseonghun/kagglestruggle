#Let's see how uniform is
#distribution of random integers

from random import randint

histogram = [0] * 100

for _ in range(100000):
    r = randint(0, 99)
    histogram[r] += 1

for h in histogram:
    print(h)

a  = [0] *10

print(a)


r = randint(0,99)
print(r)
