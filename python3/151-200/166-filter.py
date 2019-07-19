#using "filter" to select items
#bases on some condition

#Here's the condition:
def is_odd(x):
    return x % 2

data = [1, 2, 3, 4, 5, 6, 7 ,8 ,9]

data  = filter(is_odd, data)
#object of the filter type

print(type(data))
data = list(data) # a list again
print(type(data))

print(data)
