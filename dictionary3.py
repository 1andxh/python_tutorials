product = {
 'name': '',
 'unit_price': 0,
 'taxable': True,
 'in_stock': 0,
 'models': []
}

# create a dictionary for product
dwc001 = dict.fromkeys(product.keys())
dwc001.setdefault('taxable',True)
dwc001.setdefault('models',[])
dwc001.setdefault('reorder_point',100)

# show what in the new dict.
print('dictionary after fromkeys() and setdefault()')
print(dwc001)

# change the taxable field from none to true
print('\nDictionary after fromkeys() and setdefault()')
dwc001['taxable'] = True

print(dwc001)
