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
    if 2 < 3:
        print("2 is less than 3")
        if 1 < 4:
            print("1 is less than 4")
else:
    print("Hello " + name + ", welcome to the coffee shop. \n\n\n")