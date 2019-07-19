#creating a class in python
#using attributes to keep data

class Animal:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print('I am a ' + self.name)

#Creating an object or an instance

animal1 = Animal('cat')
animal1.talk()


#another object of the same class

animal2 = Animal('dog')
animal2.talk()