import math
i = 64
print(math.sqrt(64))

# constants in maths don't use parentheses
pi = math.pi
e = math.e
tau = math.tau
print(pi)
print(e)
print(tau)
# functions from built-in math module
x = 64
y = 9
z = -342345.6565
print(math.sqrt(x))
print(math.degrees(y))
print(math.floor(z))
print(math.floor(abs(z)))

# f-string formatting
user_name = "King"
print(f"hello {user_name}")
age = "24"
print(f"i am {age} years of age")

unit_price = 53.99
quantity = 35
print(f"Subtotal: ${unit_price * quantity:,.2f}")
# 2f means two decimal places. fixed
# colon before "," or ".2f" or :".2%"

# formatting percentages
sale_tax_rate = 0.065
print(f"Sales Tax Rate {sale_tax_rate}")
print(f"Sales Tax Rate {sale_tax_rate:.2%}")

sale_tax_rate = 0.950
sample1 = f"sales tax rate {sale_tax_rate:.2%}"
sample2 = f"sales tax rate {sale_tax_rate:.2%}"
sample3 = f"sales tax rate {sale_tax_rate:.2%}"
sample4 = f"sales tax rate {sale_tax_rate:.2%}"
print(sample1)
print(sample4)

user1 = "kofi"
user2 = "ama"
user3 = "yaw"
output= f"{user3} \n{user2} \n{user1}"
print(output)

unit_price = 50
quantity = 23
sale_tax_rate = 0.321
subtotal = quantity * unit_price
sale_tax = sale_tax_rate * subtotal
total = subtotal + sale_tax
output = f"""
Subtotal: ${subtotal: ,.2f}
Sales tax: ${sale_tax: ,.2f}
Total: ${total: ,.2f}
"""
print(output)

s_subtotal = "$" + f"{subtotal: ,.2f}"
s_sales_tax = "$" + f"{sale_tax: ,.2f}"
s_total = "$" + f"{total: ,.2f}"
result = f"""
Subtotal:  {s_subtotal:>9} 
Sales tax: {s_sales_tax:>9} 
Total:     {s_total:>9}
"""
print(result)

# binary octa hexadecimal
x = 26
print(bin(x))
print(oct(x))
# print("\n") is used for line break
print("\n")
print(hex(x))