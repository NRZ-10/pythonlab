import calendar

year = int(input("Enter a year: "))

if calendar.isleap(year):
    print(year, "is a Leap Year")
else:
    print(year, "is Not a Leap Year")
