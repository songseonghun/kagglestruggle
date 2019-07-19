#case-insensitive matching
#with regular expressions


import re
str = ['Word', 'word', 'wORD', 'Hi']

for s in str:
    print('Testing ' + s + '...', end='')

    if re.match('word', s, re.IGNORECASE):
        print('OK')
    else:
        print('Not OK')        

