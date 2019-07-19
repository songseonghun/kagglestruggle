#Filtering ("grepping") data
#using comprehensions


data = list(range(10))
print(data)


#now filter it
#and select only small numbers


data = [
    x for x in data if x < 4
]

print(data)


data2 = list(range(10))
data3 = []
for i in range(len(data2)):
    if data2[i] < 4:
        data3.append(i)
print(data3)

