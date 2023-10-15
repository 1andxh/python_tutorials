'''
tuples is just an immutable list, can't be changed after its defined
the syntax for creating a tuple is the same as list. except you don't use square brackets
'''

prices = (29.95, 9.98, 4.95, 79.98, 2.95)
print(len(prices))
# to count number of time an item appears
print(prices.count(4.95))
# to check if a value exists
print(23.95 in prices)

look_for = 12345
if look_for in prices:
    position = prices.index(look_for)
else:
    position = -1
print(position)

# loop through items in tuple
for price in prices:
    print(f"${price:.2f}")

# you can't assign index in tuple
