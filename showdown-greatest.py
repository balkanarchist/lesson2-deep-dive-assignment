#Write a Python program that prompts the user to enter three numbers.
#The program should then identify and
#print out the largest number among the three.

n1 = int(input("Please enter a whole number (e.g., 1): "))
n2 = int(input("Please enter another whole number: "))
n3 = int(input("Please enter a third whole number: "))

if n1 > n2 and n1 > n3:
    print(f"{n1} is the largest number.")

elif n2 > n1 and n2 > n3:
    print(f"{n2} is the largest number.")

else:
    print(f"{n3} is the largest number.")