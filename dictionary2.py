# fromkey() and setdefault()
# newdictionaryname = dict(iterable[,value])

product = {
 'name': '',
 'unit_price': 0,
 'taxable': True,
 'in_stock': 0,
 'models': []
}

# create a dictionary name dwc001 to have same key as product
dwc001 = dict.fromkeys(product.keys())
# show what in the new dictionary
print(dwc001)



