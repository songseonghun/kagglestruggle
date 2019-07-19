#default values are calculated
#only once

import random

def f(x = random.randint(1, 10)):
    print(x)


f()
f()
f()
f()
