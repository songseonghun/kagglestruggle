#reading command-line
#arguments


import sys

name = sys.argv[0]

print('Hello, ' + name + ' !')


print('sys.argv length' , len(sys.argv))

for arg in sys.argv:
    print('arg value=', arg)

    
