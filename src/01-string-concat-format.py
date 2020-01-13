import os

names = ["Jide", "Taiwo"]

for name in names:
    statement = 'Hello dear ' + name
    print(statement)

location_of_files = '/Users/babajide.owosakin/myspace/python-refresh/src'
file_name = 'filename.txt'

with open(os.path.join(location_of_files, file_name)) as f:
    print(f.read())

who: str = 'Jide'
how_many: int = 12

print('{} bought {} apples today'.format(who, how_many))