#generating a series
# of *different* random numbers

from random import randint

data = set()
n = 0

while n < 6:
    r = randint(1,46)
    if r not in data:
        n += 1
        data.add(r) #new number

print(len(data))
print(data)

