# practice function
def hello():
    """a docstring describing a function"""
    print('hello')


hello()


def hi(user_name):
    print('hello ' + user_name)


hi('John')


# using variable to pass data
def user(name):
    print('hey ' + name)


this_person = 'BigD'
user(this_person)


# Defining optional parameters with defaults
# def functioname(paremetername = defaultvalue):
def inventory(brand_name='toyota'):
    print('wow!, brand new ' + brand_name)


inventory('nissan')
inventory()


# Passing multiple values to a function
def hello(fname, lname, datestring):
    print('hello ' + fname +' ' + lname)
    print('the date is ' + datestring)


hello('kofi', 'yesu', '12/09/24')

def hello(fname, lname, datestring):
    msg = 'hello ' + fname +" " +lname
    msg += ' you mentioned the date as ' + datestring
    print(msg)


hello('nana', 'addo', '25/05/05')