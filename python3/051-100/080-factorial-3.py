# It is always possible
# to gain one line of code

# computing a factorial
# using recursion


def factorial(n):
    if n <=1 :
        return 1
    return n * factorial(n-1)

#else문을 사용하지 않아도 됨.

print(factorial(5))
