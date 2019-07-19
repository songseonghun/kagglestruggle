# reversed() vs reverse()

a = ['alpha', 'beta', ' gamma']

b = reversed(a)
print(b)
print(a) # original a


# a에 값이 변경됨.
c = a.reverse()
print(c)
print(a) #a is broken


