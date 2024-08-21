

num1 = 20
num2 = 30
result = num1 * num2
if result <= 1000:
    print(result)
else:
    print(num1 + num2)

num3 = 40
num4 = 30
result = num3 * num4
if result <= 1000:
    print(result)
else:
    print(num3 + num4)

# a program that iterates the first 10 numbers, and in each iteration, print the sum of te current and previous numeber
previous_num = 0
for i in range(0,10):
    num_sum = previous_num + 1
    print("current number", i, "previous number", previous_num, "sum:", num_sum)
    previous_num = i

word = input("enter any word")
print("original string:", word)
# get length of string
size = len(word)
print("printing only even index chars")
for i in range(0, size-1, 2):
    print(word[i])


# a program to check if the first and last number of a list is the same
num_x = [10, 20, 30, 40, 10]
num_y = [75, 65, 35, 75, 30]
print("given list:",num_x)
if num_x[0] == num_x[4]:
    print("result is True")
if num_y[0] != num_y[4]:
    print(f"num_y = {num_y}")
    print("result is False")


print('git still not working?')

