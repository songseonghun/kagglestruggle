# Let us simplify the code
# by using the "with" keyword.
# Write to a text file

with open('d:/tt.txt', 'w') as f:
    f.write('Hello World!')

# with automatically call the __enter__
#and __exit__ methods.

###
'''
f = open('d:/t.txt', 'w')
#or:
#f = open('t.txt', mode='w')
# w = crate and write
# r = read(default)
# a = append
# x = create if not existed

f.write('Hello world!!')
f.close()
'''
####