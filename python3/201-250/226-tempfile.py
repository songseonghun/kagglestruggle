#Using a temporary file
# ( and reading and writing)


import tempfile
def read_data(f):
    f.seek(0)
    data = f.read()
    print(data)

f = tempfile.TemporaryFile()
f.write(b'Some temp data')

read_data(f)

f.close()
