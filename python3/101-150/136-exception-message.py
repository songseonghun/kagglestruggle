#Passing a message to
#your custom exception

class MyException(Exception):
    #we need a constructor
    def __init__(self, message):
        print(message)

# Now use it
try:
    raise MyException('SOS!')
except:
    print('Caught')   
