#what happens when you return
#two values from a function


def f():
    return 10,11


a, b = f()
print(type(a))
print(a)
print(type(b))
print(b)

#what if you only take one

c = f()
print(type(c))
print(c)
#c is tuple class

