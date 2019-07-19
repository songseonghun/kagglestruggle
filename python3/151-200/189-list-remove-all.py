# Removing an element from a list
# ( if there are more such elements)

data = [
    'alpha', 'beta', 'gamma',
    'beta', 'delta'
] #beta happens twice



data = [x for x in data if x != 'beta']
print(data)
