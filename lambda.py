# unmasking anonymous functions
"lambda arguments : expression"

names = ['Adams', 'Ma', 'diMeola', 'Zadunsky']
names.sort()
print(names)

".sort(key = transform)"
def lowercaseof(anystring):
    """converts string to all lowercase"""
    return anystring.lower()
print(lowercaseof('ZAmunDa'))
names.sort(key=lowercaseof)



