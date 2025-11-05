import time
from datetime import datetime

# a) Current date and time
current_datetime = datetime.now()
print("a) Current date and time:", current_datetime)

# b) Current year
print("b) Current Year:", current_datetime.year)

# c) Month of the year
print("c) Month of the year:", current_datetime.month)

# d) Week number of the year
print("d) Week number of the year:", current_datetime.isocalendar()[1])

# e) Weekday of the week (0 = Monday, 6 = Sunday)
print("e) Weekday of the week:", current_datetime.weekday())

# f) Day of the year
print("f) Day of year:", current_datetime.timetuple().tm_yday)

# g) Day of the month
print("g) Day of the month:", current_datetime.day)

# h) Day of week (Monday, Tuesday, etc.)
print("h) Day of week:", current_datetime.strftime("%A"))
