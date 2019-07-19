#remove newline characters from
#the strings in a list

data = [
    'alpha\n',
    'beta\n',
    'gamma\n'
]

print(data)
print(type(data))

# Let's replace a separate function 
# with a lambda
data = list(map(
    lambda s: s.strip(), data))

print(data)
