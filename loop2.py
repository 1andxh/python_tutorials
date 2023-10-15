# continue statement in loop
answers = ["a", "", "c", "d"]
for answers in answers:
    if answers == "":
        print("incomplete")
        continue
    print(answers)
print("loop is done")

# another example
names = ["kofi", "yaw", "ama", "kwasi", "joey"]
for names in names:
    if names == "":
        print("N/A")
        continue
    print(names)
print("all names present")

names = ["kofi", "yaw", "ama", "", "joey", "sey", "bro"]
for names in names:
    if names == "":
        print("N/A")
        continue
    print(names)
print("all names present")

names = ["kofi", "yaw", "ama", "", "joey"]
for names in names:
    if names == "":
        print("N/A")
        break
    print(names)
print("all names present")



