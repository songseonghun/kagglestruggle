#Parsing JSON from a file

import json

#q.open the file
with open('test.json') as f:
    #2. parse JSON
    data = json.loads(f.read())


print(data["leeters"][3])

