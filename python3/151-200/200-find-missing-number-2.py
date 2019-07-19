#another way of finding a missing
#number in a list

data = [3, 8, 1, 10, 4, 9, 6, 7, 2]

s = sum(data)

print(s)

max = len(data) + 1  #maximum number
print(max)
s2 = max * (max + 1 ) /2 # sum of all
#numbers from 1 to 10 including 10
print(s2)

print(f'{s2 - s} is missing')
#the missing number is actually the
#difference betwen those two sums.
