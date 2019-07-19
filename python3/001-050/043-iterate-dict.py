#When iterating over
#a dictionary, you get
#the keys of it

data = {
    'France' : 'Paris',
'Gemany' : 'Berin',
'Italy' : 'Rome'
}

print(type(data))


for country in data:
    print('The captical of' + 
    country + 'is' + data[country])
