#Demostrating the "finally" keyword

def f():
    try:
        print(1/0)
    except:
        print('Exception')
        return 0
    finally:
        print('Finally')
        # the finally block will work
    print('Return') #will not be printed
    return 1

print('Start')
f()
print('Finish')
