import datetime as dt

# base class for all members
class Member:
    """the member class attribute and methods are for everyone"""
    # by default a new account expires in one year
    expiry_days = 365

    # initialize member object
    def __int__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

        # calc expiry from today
        self.expiry_date = dt.date.today() + dt.timedelta(days=self.expiry_days)

new_member = Member()
new_member.firstname = 'Joe'
new_member.lastname = 'Akan'

print(new_member.lastname)
print(new_member.expiry_date)