# is the number an Armstrong number?
# example: 153 is.
# 153 = 1^3 + 5^3 + 3^3
# 3 is the length of the number


def is_armstrong(n):
    pwr = len(str(n))
    s = sum(
        [int(x) ** pwr for x in str(n)]
    )
    return s == n

print(is_armstrong(153)) #yes
print(is_armstrong(154)) #no
print(is_armstrong(1634)) #yes

print(1 ** 3)
print(5 ** 3)
print(3 ** 3)
print(4 ** 3)
#260 8
#267 15
