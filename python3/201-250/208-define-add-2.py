##defining a "+" operator for
#your own class

class C:
    def __init__(self, value):
        self.value = value

    # redefine "+"
    def __add__(self, x):
        return self.value + x

    def __radd__(self, x):
        return self.value + x

obj = C(5)
print(obj + 10) #OK     use __add__

#what if you want to do it this way:
print(10 + obj) #ok use __radd__





