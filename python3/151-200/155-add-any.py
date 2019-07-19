data = []
print(type(data))


# you can add data of any type to
# a list in pyhton

data.append(123) #number
data.append("Hi") #string
data.append(1 + 2j) #complex

class C:
    pass

o = C()
data.append(o) #object


for x in data:
    print(x)

print(data)

