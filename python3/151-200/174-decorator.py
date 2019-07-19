# A Minimalistic example of using decorators

def my_decorator(my_func):
    print('USING DECORATOR')
    return my_func #no()


# now add the decorator
@my_decorator
def some_function():
    print('Hello from some_function')

some_function()
#you are still calling som_function,
#but the decorator function was also activated

