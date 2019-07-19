#Using the zip built-in
#function

colours = ['red', 'green', 'yellow']
fruits = ['apple', 'peer', 'banana']


z = zip(colours, fruits)

print(z)
print(type(z))

for x in z:
    # x is a tuple
    print(x[0] + ' ' + x[1])
