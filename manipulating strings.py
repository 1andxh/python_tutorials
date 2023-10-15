# Manipulating strings
s1 = "There is no such word as schmeedledorp"
s2 = " a b c "
s3 = "ABC"

# capitalize first letter,leave the rest
print(s3.capitalize())

# count number of spaces
print(s1.count(" "))

# find a character in str{returns -1 if none is found}
print(s3.find("."))

# is s2 all lower {s.islower} is returns true/false
print(s2.islower())
print(s2.isupper())

# convert str to lower
print(s3.lower())

# str leading characters {idr understand this}
print(s1.lstrip())
print(s1.strip())

# swap letter case
print(s1.swapcase())

# show string in initial caps
print(s1.title())

# print all caps
print(s1.upper())