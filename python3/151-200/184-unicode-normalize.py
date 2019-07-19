#handling the German letter &
#(which is equivalent to 'ss)

str1 = 'strasse'
str2 = 'straße' #street in englsh

print(str1 == str2) #false


print(
    str1.casefold() ==
    str2.casefold()
)