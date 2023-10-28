# name = {key:value, key:value, key:value, key:value,...}
people = {
    'htanaka': 'Haru Tanaka',
    'ppatel': 'Priya Pate',
    'bagarcia': 'Benjamin Albert Garcia',
    'zmin': 'Zhang Min',
    'afarooqi': 'Ayesha farooq',
}
# print(people)
print(people['bagarcia'])

# get length of dictionary
# len(dictionary name)
how_many = len(people)
print(how_many)
print(len(people))


# use the in keyword to search for a key in dictionary
if 'jajackson' in people:
    print('jajackson can be found')
else:
    print('sorry buddy!:( ')
# or
print('jajackson' in people)
print('zmin' in people)

# get dictionary data
# dictionary name.get(key)
