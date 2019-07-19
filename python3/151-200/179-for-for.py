#Using more than one "for" in
# a list comprehension

nums = range(1, 3)
table = [
    f'{x} + {y} = {x + y}'
        for x in nums
        for y in nums
]

print(table)
