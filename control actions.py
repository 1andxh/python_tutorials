import datetime as dt

'''sun = "down"
if sun == "down":
    print("goodnight")
print("i'm here")

moon = "up"
if moon == "down":
    print("goodnight")
print("this is TEST")

total = 100
sales_tax_rate = 0.065
taxable = True
if taxable:
    print(f"Subtotal : ${total:.2f}")
    sales_tax = total * sales_tax_rate
    print(F"Sales Tax: ${sales_tax:.2f}")
    total = total + sales_tax
print(f"Total    : ${total: .2f}")

total = 100
sales_tax_rate = 0.065
taxable = False
if taxable:
    print(f"Subtotal : ${total:.2f}")
    sales_tax = total * sales_tax_rate
    print(F"Sales Tax: ${sales_tax:.2f}")
    total = total + sales_tax
print(f"Total    : ${total: .2f}")'''

# if else
now = dt.datetime.now()
if now.hour < 12:
    print("Good morning!")
else:
    print("Good Afternoon!")
    print("I hope you're doing well")

# elif
light_color = "green"
if light_color == "green":
    print("Go")
elif light_color == "red":
    print("Stop")
print("this execute regardless")

# else can be added if all conditions are false
light_color = "yellow"
if light_color == "green":
    print("Go")
elif light_color == "red":
    print("Stop")
else:
    print("proceed with caution")
print("this execute regardless")


