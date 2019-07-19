import re
text = '''This program will
replace double or   tripple  or
more spaces with a     single space'''


text = re.sub(
    r'\s{2,}', ' ', text
)
# sub = substitute
# \s{2,} = two or more spaces
# '  replace single space

print(text)