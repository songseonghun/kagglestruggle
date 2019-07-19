#filtering data using a
#built-in function "filter"

data = list(range(10))
print(data) # 10 numbers

def my_filter(x):
    #your custom filtering function 
    return x < 4
    #only select small numbers

data = list (
    filter(my_filter, data)
)

print(data)

