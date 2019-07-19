#positional-only parameters
#Available in Python 3.8+

def  s(a,b, /)
    print(a+b)

s(10,20) #ok

def s2(a, b, /, c):
    print(a + b + c)

s2(10,20, c= 30)


