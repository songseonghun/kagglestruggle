# Count bits "1" in a binary
# representation of a positive 
# integer number

num = 12345

bit_num = bin(num)
# this is a string let'see it
print(bit_num)


#now count the "1" s
c = bit_num.count('1')
print(c) # the number of 1 bits


