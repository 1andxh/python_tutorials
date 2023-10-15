s = "Abracadabra Hocus Pocus you're a turtle dove"
# is there small letter t in s?
print("t" in s)

# is there a capital t in s?
print("T" in s)

# is there no uppercase t in s?
print("T" not in s)

# print 15 hyphens in a row
print("-" * 15)

# print n character or a string
print(s[2])
print(s[0])

# print range of characters eg. 33-42
print(s[33:43])

# print every third character in string starting at 0 { step value varies }
print(s[0:44:5])

# print lowest character is s ( a space is lower than a letter)
print(min(s))

print(max(s))

# find first upper case or lower of a character
print(s.index("P"))
print(s.index("o"))

# print first lower case o from the latter part of the string
# print a in the first part
print(s.index("o",22,44))
print(s.index("b",0,15))

# how many lower case a
print(s.count("a"))

print(len(s))
