# take a strign. remove all character
# that are not vowels. keep spaces
# for clarity


import re

s = 'Hello, World! This is a string.'

# sub = substitute

s2 = re.sub(
    '[^aeiouAEIOU ]+', #vowels and
    # a space
    '', #replace with nothing
    s
)

print(s2)


