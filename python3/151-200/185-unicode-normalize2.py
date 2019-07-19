# canonical normalization
# in unicode

import unicodedata

# 'a' can be represented in two ways:

s1 = 'á'
s2 = 'a\u0301' #combining acute

print(s1 == s2) #False


s3 = unicodedata.normalize('NFC', s2)
print(s1 == s3) #True
print(s1)
print(s2)
print(s3)


