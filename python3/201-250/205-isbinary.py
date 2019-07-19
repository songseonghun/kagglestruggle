# Check if the given text string
# can represent a binary number
# ( in its string format, i.e. with
# regular 1 an 0 as characters)

s1 = '11010101' # ok
s2 = '10111400' # not ok

import re

if re.search('[^01]', s1):
    print('s1 is not binary')


if re.search('[^01]', s2):
    print('s2 is not binary')

    