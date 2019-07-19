#removing accents from characters

import unidecode

str = 'Cafe Munchen'

str = unidecode.unidecode(str)
print(str)

