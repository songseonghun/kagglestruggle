# A possible implementation
# of a non-recursivce factorial
# calculation for positive ints

def factorial(n):
    f = 1
    for m in range(1, n + 1):
        f *= m
    return f

print(factorial(5))

# f * m
# 1*1 =1
# 1*2 =2
# 2*3 = 6
# 6 * 4 = 24
# 24 * 5= 120




