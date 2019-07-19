# what is the day(week day) today?

import datetime

t = datetime.datetime.today()

print(t)
d = t.strftime('%A')
a = t.strftime
print(a)

print(f'Today is {d}')
