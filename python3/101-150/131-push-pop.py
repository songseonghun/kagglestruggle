#how to push data to a list
#and how to pop it back

data = []

for i in range(5):
    data.append(i * i)
    #fill with some data
    print(data)

while(len(data)):
    #while list is not empty
    value = data.pop()
    #pop - take from back

    print(value)