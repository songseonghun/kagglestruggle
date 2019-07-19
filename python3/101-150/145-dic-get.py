#a safer way of reading values from
#a dictionary

data = {
    'France': 'Paris',
    'Italy': 'Rome'
}

#capital  = data['Gemany'] #error
capital = data.get('Germany') #OK
print(capital)
#but it returns 'None'

capital = data.get('Germany', '??')
print(capital)
#prints '??'
