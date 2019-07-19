#Calling a method of the parent class

class Animal:
    def talk(self):
        print("I am an animal")


class Cat(Animal):
    def talk(self):
        print('I am a cat')  
        #also call Animal.talk:
        super(Cat, self).talk()
        #      ^child class
        #            ^this object
        # just remeber this syntax

cat = Cat()
cat.talk()

