# Caching function return values
# when you call it with the same
# arguments(s)

from functools import lru_cache

@lru_cache(maxsize=1000)
def factorial(n):
    if n <=1 :
        return 1
    print(f'Computing {n}!')
    return n * factorial(n - 1)


print(factorial(5))
print(factorial(3))
