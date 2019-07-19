#calculator that parses operations


ops = {
    '+' : lambda x, y: x + y,
    '-' : lambda x, y: x - y,
    '*' : lambda x, y: x * y,
    '/' : lambda x, y: x / y,
}

def calc(x,y, op): #operator
    return ops[op](x, y)

print(calc(3, 4, '+'))
print(calc(3, 4, '-'))
print(calc(3, 4, '*'))
print(calc(3, 4, '/'))
