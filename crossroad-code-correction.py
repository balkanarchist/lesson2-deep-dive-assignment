#Fix the errors in the following code.

number = int(input("Enter a whole number (i.e., no decimals): ")) #converted input into an integer

if number > 0:
    print("The number is positive.")
elif number == 0:    #added extra = to make it an equality comparison
    print("The number is zero.")
else:    #removed the condition for else
    print("The number is negative.")