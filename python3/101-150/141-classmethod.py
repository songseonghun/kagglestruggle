class Class:
    @classmethod
    def class_meth(self, param):
        #method with "self"
        print('1 ' + param)

    @staticmethod
    def static_meth(param):
        #without "self"
        print('2 ' + param)


obj = Class()
#but what if vise versa?
#we need decorpators
Class.class_meth('Hi')
obj.static_meth('Yo')

