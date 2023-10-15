import datetime as dt

# lists are in square brackets, numbers don't need "" in list
students = ["mark", "karl", "fahd", "khan"]
print(students[2])

# define a list of number
scores = [88, 78, 45, 66,90]
# print(scores[3])
for score in scores:
    print(score)
print("done")

# to check content of list
students = ["mark" , "karl" , "fahd" , "khan", "sanji", "zoro"]
# is sanji in the list?
has_karl = "karl" in students
print(has_karl)

has_sanji = "sanji" in students
print(has_sanji)

has_kojo = "kojo" in students
print(has_kojo)

# get length of list
students = ["mark", "karl", "fahd", "khan", "sanji", "zoro"]
print(len(students))

# add item to the end of a list. you can use append() method and the literal value in quotes or variable name
students_1 = ["yaa", "naa", "paa", "osaa", "waa", "taa"]
# add koo to the list
students_1.append("koo")
# add item using a variable
new_student = "kaa"
students_1.append(new_student)
print(students_1)


student_name = "paa"
# add student name not only if not already in the list
if student_name in students_1:
    print(f"{student_name} already in the list")
else:
    students_1.append(student_name)
    print(f"{student_name} added to the list")

# listname.insert(position, item)
food = ["fufu", "jollof", "awaakye", "banku"]
new_food = "gob3"
food.insert(3,new_food)
food.insert(2,"koko")
print(food)

# changing an item in a list
# listname[index] = new value
cars = ["toyota", "honda", "tata"]
cars[2] = "nissan"
print(cars)

# use extend function to combine lists
# original_list.extend(additional_items_list)
list1 = ["molly", "polly", "rolly"]
list2 = ["jolly", "nolly", "sully"]
# list1.extend(list2)
list2.extend(list1)
# print(list1)
print(list2)

# removing list items
letters = ["a", "b", "c", "c", "e", "d", "a", "e"]
# remove item from list
letters.remove("c")

# *remove multiple instances of an item in the list
# while "c" in letters:
#     letters.remove("c")
print(letters)

letters_1 = ["a", "b", "c", "c", "e", "d", "a", "e"]
# remove first item on list or any position
letters_1.pop(0)
# remove last item
letters_1.pop()
print(letters_1)

# letters removed can be stored in a variable
letters_1 = ["a", "b", "c", "c", "e", "d", "a", "e"]
first_removed = letters_1.pop(0)
last_removed = letters_1.pop()
print(f"{first_removed} and {last_removed} were removed from the list")

# items can also be removed using the del command
picks = [2, 3, 4, 6, 8]
# delete item sub 2
del picks[2]
print(picks)

# *del can be used to delete the whole func
# del picks
# print(picks)
# prints an error

# *clearing out list
# listItem.clear()

grades = ["a", "b", "c", "c", "e", "d", "a", "e", "f", "f"]
# count number of particular grades
f_grades = grades.count("f")
# using  a variable for value count
find = "b"
b_grades = grades.count(find)
print(f"there {f_grades} F's in the list")
print("there are" + " " + str(b_grades)+" " + find + " " + "in the list")

marks = ["a", "b", "c", "c", "e", "d", "a", "e", "f", "f"]
look_for = "c"
if look_for in marks:
    print(f"{look_for} is in the list")
else:
    print("carry on")


# Alphabetizing and sorting lists
city = ["kaduna", "ohio", "alabama", "accra", "pontiac", "maldives", "wa"]
numbers = [75, 9, 34, 54, 12, 3, 70]

city.sort()
numbers.sort()
print(city)
print(numbers)

dates = []
dates.append(dt.date(2022, 3, 23))
dates.append(dt.date(2021, 3, 24))
dates.append(dt.date(2022, 3, 2))
dates.append(dt.date(2020, 3, 3))
dates.append(dt.date(2012, 3, 23))

dates.sort()
for date in dates:
    print(f"{date:%m/%d/%y}")

# to sort items in reverse order use the (reverse = true) method
alphabets = ["a", "b", "c", "d", "f", "g", "h", "x"]
alphabets.sort(reverse=True)
print(alphabets)

# reversing a list (.reverse) this reverses items no matter the order
whip = ["c300", "c350", "e63s amg", "porsche 911 gt3s"]
whip.reverse()
print(whip)

# make a copy of a list (.copy)
boys = ["zara", "zoro", "deku", "kora"]
Cboys = boys.copy()
# reverse copied list
Cboys.reverse()
print(Cboys)
print(boys)

"""
append() Adds an item to the end of the list.
clear() Removes all items from the list, leaving it empty.
copy() Makes a copy of a list.
count() Counts how many times an element appears in a list.
extend() Appends the items from one list to the end of another list.
index() Returns the index number (position) of an element within a list.
insert() Inserts an item into the list at a specific position.
pop() Removes an element from the list, and provides a copy of that item that 
you can store in a variable.
remove() Removes one item from the list.
reverse() Reverses the order of items in the list.
sort() Sorts the list in ascending order. Put reverse=True inside the 
parentheses to sort in descending order.

"""