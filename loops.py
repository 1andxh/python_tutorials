# repeating a process with for loop
for x in range(7):
    print(x)
print("all done sir!")

for x in range(1, 4):
    print(x)

print("yaayyy")

# looping through a string
for x in "snorkle":
    print(x)
print("Done")

my_word = "bubble"
for x in my_word:
    print(x)

# looping through a list
for x in ["the", "rain", "in","spain" ]:
    print(x)

seven_dwarfs = ["happy", "sad", "grumpy", "sleepy", "dopey", "clingy"]
for dwarf in seven_dwarfs:
    print(dwarf)
print("and snow white too")


# bailing out of loop
answers = ["A", "B", "C", "D"]
for answers in answers:
    if answers == "":
        print("incomplete")
        break
    print(answers)
print("loop is done")

answers = ["a", "", "c", "d"]
for answers in answers:
    if answers == "":
        print("incomplete")
        break
    print(answers)
print("loop is done")




