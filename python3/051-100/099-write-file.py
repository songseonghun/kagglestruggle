#write to a text file

f = open('d:/t.txt', 'w')
#or:
#f = open('t.txt', mode='w')
# w = crate and write
# r = read(default)
# a = append
# x = create if not existed

f.write('Hello world!!')
f.close()

