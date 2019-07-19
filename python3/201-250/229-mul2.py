#Multpying by 2 using shift
# << bit 연사자를 쉬프트로 이동 
# 0011 1100 << 1111 0000

val = 10

val <<= 2 # mul by 4

print(val)

val = 1
for _ in range(5):
    val <<= 1 # *= 2
    print(val)

