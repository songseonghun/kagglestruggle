#Find a missing number in a list
data = [3, 8, 1, 10, 4, 9, 6, 7, 2]

# 5 is missing : list is not sorted

# you can also tranform a list to 
# a set to make the solution faster
# for bigger data arrys:

data = set(data)
print(data)
print(len(data))

for i in range(1, len(data) + 1):
    #1....10

    if i not in data:
        print(f'{i} is missing')
        # done: it's found
        break

