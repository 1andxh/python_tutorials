

age = 31

if age < 21:
    # if age < 21 no alcohol
    beverage = "milk"

elif age >= 21 and age < 80:
    # if between 21 and 79 suggest beer
    beverage = "beer"
else:
    # 80 upwards fruit juice
    beverage = "fruit juice"

print(F"have a {beverage}")
print("Have a " + beverage)




