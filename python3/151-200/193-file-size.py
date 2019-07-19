#how to get file size in bytes


import os

statinfo = os.stat('data2.txt')
print(statinfo.st_size)
