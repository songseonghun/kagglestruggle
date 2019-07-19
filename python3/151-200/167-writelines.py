#be careful when using
#"writelines"


data = [
    'alpha',
    'beta',
    'gamma'
]

with open('data2.txt', 'w') as f:
    f.writelines(data)

# no new lines will be added
#alphabetagamma

