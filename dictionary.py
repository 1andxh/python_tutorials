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
person = 'bagarcia'
print(people.get(person))

# You don’t get an error, and the program doesn’t just crash and burn.
# Instead, get() just gracefully returns the word None
person = 'agyekum'
print(people.get(person))

person = 'kaywa'
print(people.get('kaywa','not in dictionary'))


# changing value of key
# dictionaryname[key]=newvalue

# print current value
print(people['htanaka'])
# change value
people['htanaka'] = 'Haru Tanak Abdul'
print(people['htanaka'])


# updating dictionary data
# dictionaryname.update(key,value)
people = {
    'htanaka': 'Haru Tanaka',
    'ppatel': 'Priya Pate',
}
people.update({'ppatel': 'Priyatea Pate'})
print(people)
# update dictionary with new value pair
people.update({'wiggins':'Wanda Wiggins'})


# show items in a dictionary
for person in people.keys():
    print(person + "=" + people[person])


# looping through a dictionary
for person in people:
    print(person)

# copying a dictionary
cars = {
    'BMW': 'Balvarian Motors',
    'Benz': 'Mercedes Benz'
}
showroom = cars.copy()
print(cars)
print(showroom)

# delete item from dictionary
del cars['Benz']
print(cars)

# to remove all key - values
cars.clear()
print(cars)

# .pop() removes a key from the dictionary into a new variable
people = {
    'htanaka': 'Haru Tanaka',
    'ppatel': 'Priya Pate',
    'bagarcia': 'Benjamin Albert Garcia',
    'zmin': 'Zhang Min',
    'afarooqi': 'Ayesha farooq',
}
adios = people.pop('zmin')
print(adios)
print(people)

# adios = people.popitem()

# multi-key dictionary
product = {
 'name': 'Ray-Ban Wayfarer Sunglasses',
 'unit_price': 112.99,
 'taxable': True,
 'in_stock': 10,
 'models': ['Black', 'Tortoise']
}
# dictionaryname[key] to print value of each key
print(product['name'])
print('Price:   ', f"${product['unit_price']:.2f}")
print('Taxable: ', product['taxable'])
print('In Stock:', f"{product['in_stock']} more")
print('models:')
for model in product['models']:
    print(" " * 10 + model)









