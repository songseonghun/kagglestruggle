#Iterating over dictionary pairs
#(both keys and values)

capitals = {
    'France': 'paris',
    'Italy': 'Rome',
}

for country, city in capitals.items():
    #country = key
    #city = value

    print('the capital of ' + 
        country + ' is ' + city + '.')
