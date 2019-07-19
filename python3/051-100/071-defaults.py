#supplying default values
#for function arguments
#초기값 정의

def greet(name = 'Dear'):
    print('Hello, ' + name + '!')



greet('John')

greet()

greet('Karla')


def greet2(name):
    print('Hello, ' + name + '!')

#greet2()
#변수가 없는 경우 에러가 남.


