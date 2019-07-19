#Testing "empty" values
# in boolean context

x = 1

if x:
    print("True")
else:
    print("False")

x = 0

if x:
    print("True")
else:
    print("False")

#empty일 경우 거짓으로 구분 0 값
x = ''

if x:
    print("True")
else:
    print("False")
