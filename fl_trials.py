# to iterate through letter in a word
for i in "bethesda":
    print(i)


# loop through a range
for j in range(7):
    print(j)

# iterate through a list
Animal_list = ['cat', 'dog', 'sheep', 'goat']
for x in Animal_list:
    print(x)

programmingLanguages = {'J': 'Java', 'P': 'Python'}
for key, value in programmingLanguages.items():
    print(key, value)


# for loop using the zip() function for parallel iteration
a1 = ['Python', 'Java', 'CSharp']
b2 = [1, 2, 3]

for i, j in zip(a1, b2):
    print(i, j)


# Using else statement inside a for loop in Python
    flowers = ['Jasmine', 'Lotus', 'Rose', 'Sunflower']
for f in flowers:
    print(f)
else:
    print('Done')


# Nested for loops in Python(one loop inside another loop)
list1 = [5, 10, 15, 20]
list2 = ['Tomatoes', 'Potatoes', 'Carrots', 'Cucumbers']

for x in list1:
    for y in list2:
        print(x, y)


# Using break statement inside a for loop in Python
    vehicles = ['Car', 'Cycle', 'Bus', 'Tempo']

for v in vehicles:
    if v == "Bus":
        break
    print(v)


# Using continue statement inside a for loop in Python
vehicles = ['Car', 'Cycle', 'Bus', 'Tempo']

for v in vehicles:
    if v == "Bus":
        continue
    print(v)


# for loop to count the number of elements in a list
numbers = [12, 3, 56, 67, 89, 90]
count = 0

for n in numbers:
    count += 1

print(count)

# you can use len(numbers) also to get the count


# for loop to find the sum of all numbers in a list
numbers = [12, 3, 56, 67, 89, 90]
sum = 0

for n in numbers:
    sum += n

print(sum)


# for loop to find the multiples of 5 in a list
numbers = [2, 5, 6, 10, 15, 20, 25]

for n in numbers:
    if n % 5 == 0:
        print(n)


# for loop to print a triangle of stars
for i in range(1, 5):
    for j in range(i):
        print('*', end='')
    print()


# for loop to copy elements from one list to another
list1 = ['Mango', 'Banana', 'Orange']
list2 = []
for i in list1:
    list2.append(i)

print(list2)


# for loop to find the maximum element in a list
numbers = [1, 4, 50, 80, 12]
max = 0

for n in numbers:
    if (n > max):
        max = n

print(max)


# for loop to find the minimum element in a list
numbers = [1, 4, 50, 80, 12]
min = 1000

for n in numbers:
    if (n < min):
        min = n

print(min)


# for loop to sort the numbers in a list in ascending order
numbers = [1, 4, 50, 80, 12]

for i in range(0, len(numbers)):
    for j in range(i + 1, len(numbers)):
        if (numbers[i] > numbers[j]):
            temp = numbers[i]
            numbers[i] = numbers[j];
            numbers[j] = temp

print(numbers)


# for loop to sort the numbers in a list in descending order
numbers = [1, 4, 50, 80, 12]

for i in range(0, len(numbers)):
    for j in range(i + 1, len(numbers)):
        if (numbers[i] < numbers[j]):
            temp = numbers[i]
            numbers[i] = numbers[j];
            numbers[j] = temp

print(numbers)


# for loop to print the multiples of 3 using range() function
# printing multiples of 3 till 20

for i in range(3, 20, 3):
    print(i)


# for loop to print the multiples of 5 using range() function
# printing multiples of 5 till 20

for i in range(5, 20, 5):
    print(i)


# for loop to print the numbers in reverse order using range() function
for i in range(10, 0, -1):
    print(i)

