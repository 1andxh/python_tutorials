class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@edu.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * 1.04)


emp_1 = Employee('Daniel', 'fletcher', 50000)
emp_2 = Employee('Sarah', 'Duke', 75000)

print(emp_1.email)
# print(emp_2.email)
print(emp_1.fullname())
# print(Employee.fullname(emp_2))
# emp_1.fullname()
print
emp_1.apply_raise()
print(Employee.apply_raise(emp_1))



