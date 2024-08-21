# to nest a dictionary, assign a name for the dictionary as a whole,
# assign a unique name as a key for the sub dictionaries
# enclose all the key-value pairs for every dictionary in curly braces

products = {
    'RB00111': {'name': 'rayban glasses', 'price': 112.98, 'models': ['black', 'tortoise']},
    'DWC0317': {'name': 'dji drone', 'price': 72.98, 'models': ['black', 'white']},
    'MTS0540': {'name': 'nike shorts', 'price': 2.98, 'models': ['small', 'medium', 'large']},
    'ECG202': {'name': 'apple homepod', 'price': 52.98, 'models': []}
}

print(f"{'ID':<6} {'Name':<17} {'Price':>8} {'Models'}")
print('-' * 60)

# loop through dict. in each product dict
for oneproduct in products.keys():

    id = oneproduct
    # get name of one product
    name = products[oneproduct]['name']
    unit_price = '$' + f"{products[oneproduct]['price']}"
    models = ''

    for m in products[oneproduct]['models']:
        models += m + ','

    if len(models) >2:
        models = models[:-2]
    else:
        models = '<none>'
print(f"{id:<6} {name:<17} {unit_price:>8} {models}")
