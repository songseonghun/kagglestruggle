#Uisng yield

def f():
    for i in range(100):
        yield i

g1 = f()
g2 = f()


print(next(g1))
print(next(g2))
print(next(g1))
print(next(g2))
print(next(g1))
print(next(g2))
