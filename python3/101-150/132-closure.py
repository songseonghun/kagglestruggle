#using lambdas to create closures

def power(x, y):
    return x ** y

square  = lambda x : power(x, 2)
cube = lambda x: power(x, 3)

print(square(5))
print(cube(5))


