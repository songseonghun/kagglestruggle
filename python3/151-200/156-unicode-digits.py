#Digits in the unicode space

import re

#10_000 = 10,000
for i in range(32, 10_000):
    ch = chr(i) #character with
    #the unicode code i
    if re.match('\d', ch):
        # if it is a digit
        print(ch, end='')
print('')


