#the "id" function

class C:
    pass

# Let's create two object:

o1 = C()
o2 = C()

#and a variable pointing to one of them:
o3 = o2

print(id(o1)) # an object
print(id(o2)) # a diffrent object
print(id(o3)) #same object as o2
