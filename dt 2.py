import datetime as dt
from dateutil.tz import gettz

# get time from computer
here_now = dt.datetime.now()

# get utc datetime now
utc_now = dt.datetime.utcnow()

time_difference = (utc_now - here_now)
print(f"my time : {here_now:%I:%M %p}")
print(f"utc time : {utc_now:%I:%M %p}")
print(f"difference : {time_difference}")


event = dt.datetime(2020, 7, 4, 19, 0, 0)
utc = dt.datetime.now(gettz('Etc/UTC'))
print(utc)
