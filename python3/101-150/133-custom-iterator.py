class C:
    def __iter__(self):
        self.n = 0
        return self
    def __next__(self):
        self.n += 1
        return self.n

c = C()
i = iter(c) # get an iterator

for _ in range(5):
    #use the iterator   #반복자
    #반복자는 객체지향프로그래밍에서
    #배열이나 그와 유사한 자료 구조의 내부
    #의 요소를 순회하는 객체
    print(next(i))
