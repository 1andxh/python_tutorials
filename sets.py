sample_set = {1.98, 98.9, 74.95, 2.5, 1, 16.3}
# to add single item .add()
sample_set.add(11.23)

# to add multiple items .update() and should be in square brackets
sample_set.update([88, 66, 4.54])
print(sample_set)

# copied set will not have the same order as original
ss2 = sample_set.copy()
print(ss2)

