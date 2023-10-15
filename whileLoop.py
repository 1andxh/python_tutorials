import random


# counter = 65
# while counter < 91:
#     print(str(counter) + "-" + chr(counter))
#     counter += 1
# print("all done sir!")

# print("odd numbers")
# counter = 0
# while counter < 10:
#     # get a random number
#     number = random.randint(1,999)
#     if int(number / 2) == number / 2:
#         # if its an even number dont print it
#         continue
#     print(number)
#     counter += 1
# print("c'est fini")

# num = int(input("enter your index number:"))
# while num < 1 or num > 5000:
#     print(f"{num} is not valid")
#     num = int(input("enter your index number"))
# print(f"index number: {num} has been recorded")

print("numbers that aren't evenly divisible by 5")
counter = 0
while counter < 10:
    number = random.randint(1,999)
    if int(number / 5) == number / 5:
        break
    print(number)
    counter =+ 1
print("loop finished")