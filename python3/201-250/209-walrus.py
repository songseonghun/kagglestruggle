#using the new := operator

# in python 3.8

#read and print lines before you meet stop


with open('input.txt') as f:
    while (
        str := f.readline().strip()
    ) != 'STOP':
        print(str)
