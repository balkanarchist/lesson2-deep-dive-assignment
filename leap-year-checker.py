#Write a Python program that prompts the user to input a year.
#The program should determine if the given year is a leap year
#or not and then display an appropriate message. 

year = int(input("Enter a year: "))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")