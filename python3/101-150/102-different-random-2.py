#generating a series
# of *different* random numbers

from random import randint

data = set()

while len(data) < 20:
    r = randint(0,100)
    data.add(r)

print(len(data))
print(data)
