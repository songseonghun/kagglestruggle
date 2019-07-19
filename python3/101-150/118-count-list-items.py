#count how many times each item
#appears in the list


my_list = [
    'a', 'b', 'a', 'b', 'c', 'b',
    'd', 'b', 'e', 'f'
]

print(type(my_list))

b = sorted(set(my_list))
print(b)

for item in sorted(set(my_list)):
    #set(my_list) each item appears 
    #only one time

    count = my_list.count(item)
    print(
        f'{item} = {count} times'
    )
   