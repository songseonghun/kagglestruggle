# how to check if the file
# or direcotry exists

import os

print(os.path.exists('data2.txt'))
print(os.path.exists('none.txt'))


#also with directories
print(os.path.exists('__pycache__'))
