#Identify and fix the bugs in the code below.

choice = input("Do you choose the path to the left or right? ")

if choice == "left":    #changed to the equality comparison operator ==
    print("You find a treasure chest!")
elif choice == "right": #changed to the equality comparison operator ==
    print("You encounter a dragon!")
else:
    print("Invalid choice!")
#To make it even more explicit, maybe add an extra sentence for the else print statement
#telling the user that (s)he should enter only left or right in the prompt.