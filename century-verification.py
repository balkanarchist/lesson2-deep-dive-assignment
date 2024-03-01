'''Add functionality to your program from Task 1
to inform the user if the entered year is a century year
(e.g., 1900, 2000) regardless of whether it's a leap year or not.
'''

year = int(input("Enter a year: "))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

if year % 100 == 0:
    print(f"{year} is a century year.")
else:
    print(f"{year} is not a century year.")

#change current else to elif, then make new else the not a century year?