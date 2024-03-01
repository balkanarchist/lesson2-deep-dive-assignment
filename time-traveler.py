from datetime import date

'''
Enhance your program to indicate if the provided year
is in the future, past, or is the current year, 
compared to the system's current year.
'''
#You might find Python's datetime module helpful for this task.

current_year = date.today().year

year = int(input("Enter a year: "))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

if year % 100 == 0:
    print(f"{year} is a century year.")
else:
    print(f"{year} is not a century year.")


if year > current_year:
    print("This is a future year.")
elif year < current_year:
    print("This year is in the past.")
else:
    print("This is the current year.")