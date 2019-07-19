#Fetching a text file from the web

import requests

url = 'http://zalesia.com'
r = requests.get(url)

print(r.status_code)
print(r.content)
