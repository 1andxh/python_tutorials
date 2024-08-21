def hello(fname,lname, datestring=''):
    msg = 'hello ' + fname + ' ' + lname
    if len(datestring) > 0:
        msg += ' you mentioned ' + datestring
    print(msg)


hello('king', 'solomon', '1/02/2001')
hello('jeffery', 'schlopp')


# Using keyword arguments(kwargs)
apt_date = '12/03/2020'
last_name = 'jenner'
first_name = 'kylie'
hello(datestring=apt_date, lname=last_name, fname=first_name)


# passing multiple values in a list
def alphabetize(original_list=[]):
    """pass any list in square brackets, displays a string with items sorted"""
    # Inside the function make a working copy of the list passed in.
    sorted_list = original_list.copy()
    # sort the working copy
    sorted_list.sort()
    # make a new empty string for output
    final_list = ''

    # loop through the sorted list and append name and comma and space
    for name in sorted_list:
        final_list += name + ', '
    # knock of last comma space if final list is long enough
    final_list = final_list[:-2]
    print(final_list)


alphabetize(['schrepfer', 'mensah', 'santiago', 'yakubu'])


# passing in an arbitrary number of argument
def sorter(*args):
    newlist = list(args)
    newlist.sort()
    print(newlist)


sorter(1, 0.001, 10000, -900, 2, 57)
