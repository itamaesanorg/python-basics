# Lets play with if if if if else!!!
name = input("What is your name\n")
# Great the customer with their name and thank them for coming in today using concatenation.

if name == "Ben":
    evil_status = input("\n Are you evil?\n")
    if evil_status == "yes":
        print("You're not welcome here Ben! Get out of here!")
        exit()
    else:
        print("Oh! You are one of those good Bens! Come in! \n\n\n")
else:
    print("Hello " + name + ", welcome to the coffee shop. \n\n\n")