#splitting data into
#odd and even numbers
#짝홀

data = [
    45, 56, 67, 23, 57, 78, 67 ,454
]

odd = []
even = []

print(type(odd))
print(type(even))

for d in data:
    if d % 2:
        odd.append(d)   #홀수 1이 나머지로 나옴으로
    else:
        even.append(d)  #짝수

print(f'Odd numbers : {odd}')

print(f'Even numbers : {even}')

