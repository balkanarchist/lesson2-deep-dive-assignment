'''Enhance your program to handle cases where
two or all of the numbers are equal. The program
should display appropriate messages like "Two
numbers are equal and the largest"
or "All numbers are equal".
'''
n1 = int(input("Please enter a whole number (e.g., 1): "))
n2 = int(input("Please enter another whole number: "))
n3 = int(input("Please enter a third whole number: "))

if n1 > n2 and n1 > n3:
    print(f"{n1} is the largest number.")

elif n2 > n1 and n2 > n3:
    print(f"{n2} is the largest number.")

elif n3 > n1 and n3 > n2:
    print(f"{n3} is the largest number.")

elif (n1 == n2 and n1 != n3) or (n1 == n3 and n1 != n2) or (n2 == n3 and n2 != n1) or (n3 == n1 and n3 != n2 ):
    print("Two numbers are equal and the largest.")

else:
    print("All numbers are equal.")
