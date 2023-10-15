import datetime
# put today's date in a variable
today = datetime.date.today()
# put another data in last_of_teen
last_of_teen = datetime.date(2019, 12, 31)
# last_of_teen2 = datetime.time(23,44,23,2)
print(today)
print(last_of_teen)
# print(last_of_teen2)
print(last_of_teen.day)
print(last_of_teen.year)
print(last_of_teen.month)
print(f"{last_of_teen:%a,%b %d,%y}")
print(f"{last_of_teen: %A,%B %d,%y}")
print(f"{today:%m/%d/%y}")
print(f"{today:%x}")

# working with times
midnight = datetime.time()
print(midnight)
print(type(midnight))

almost_midnight = datetime.time(23, 59, 59, 999999)
print(almost_midnight)

right_now = datetime.datetime.now()
print(right_now)

# date and time can be used with parameters
new_years_eve = datetime.datetime(2019, 12, 31, 23, 59)
print(new_years_eve)

# calculating time span
# time delta is created when you subtract two dates and times
new_years_day = datetime.datetime(2019, 1, 1)
memorial_day = datetime.datetime(2019, 5, 27)
days_between = memorial_day - new_years_day
print(days_between)
print(type(days_between))

# you can define timedelta using this syntax
# datetime.timedelta(days=,seconds=,microseconds=,milliseconds=,minutes=,hours=,weeks=)
new_years_day = datetime.date(2019, 1, 1)
duration = datetime.timedelta(days=146)
print(new_years_day + duration)

memorial_day = datetime.date(2019, 5, 27)
duration = datetime.timedelta(days=146)
print(memorial_day-duration)

# calculate duration less than a dat
start_time = datetime.datetime(2019, 3 ,31, 8, 0, 0)
finish_time = datetime.datetime(2019, 3, 31, 14, 34, 45)
time_between = finish_time - start_time
print(time_between)
print(type(time_between))

now = datetime.datetime.now()
birth_date = datetime.datetime(1995, 3, 31, 8, 26)
age = now - birth_date
print(age)

days_old = 10376
years_old = days_old // 365
print(years_old)

# e.g. find my age
# date according to the computer
to_day = datetime.date.today()

# any birthdate expressed as dd/mm/yy
birthdate = datetime.date(2001, 5, 25)

# duration between dates as time delta
delta_age = (to_day - birthdate)

# duration between dates as a number of days
days_Old = delta_age.days

# floor divide days by 365 to get years
years = days_Old // 365

# floor the days by 30 to calculate the month
month = (days_Old % 365) // 30
print(f"you are {years} years and {month} months old")


