# returning values from functions
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
    # return the alphabetized list
    # return final_list
    print(final_list)
# random_list = ['McMullen','kaesar','Maier','Wilsom','Yudt','Gallagher','Jacobs']
# alpha_list = alphabetize(random_list)
# print(alpha_list)
names = ['McMullen','kaesar','Maier','Wilsom','Yudt','Gallagher','Jacobs']
alphabetize(names)