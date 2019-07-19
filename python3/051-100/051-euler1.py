sum = 0

for n in range(0,1000):
    if not(n % 3) or not(n % 5):
        sum += n
print(sum)
