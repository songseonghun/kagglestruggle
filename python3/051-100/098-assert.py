#Using assert to break
#the program if you data are wrong

def divide(x, y):
    assert y != 0  
    #assert 가정이 맞는 경우 프로그램 실행 취소
    return x / y

a = divide(100,10)
print(a)

a = divide(100,0) # not ok
print(a)    #will not be printed


