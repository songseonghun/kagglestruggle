# how many digits are ther in a number


import math

n = 123456

# method 1
print(len(str(n)))


# method 2
print( 1 + math.floor(math.log10(n)))
# pure mathematical
# log - base 10


