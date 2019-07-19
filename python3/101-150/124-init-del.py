#Creating custom constructor
#and desctructor for a class

class C:
    def __init__(self):
        print('Constructor')    # 생성자
    def __del__(self):
        print('Destructor')     #소멸자

o = C() #생성자 호출
print('Hello world')       
#소멸자 호출
#프로그램 종료
