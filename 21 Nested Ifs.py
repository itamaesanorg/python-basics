# Lets play with if if if if else!!!

print("\n The Bar was dark and a voice asked from the back of the room: \n \n Ben, is that you?")

name = input("\n")
menu = "Black Coffe, Espresso, Latte, Capuccino"


if name == "Ben":
    evil_status = input("\n Are you evil? \n")
    print("\n Hello not evil" + name + ", welcome to the coffee shop. \n \n")
else:
    print("We have the following drinks: " + menu)
    order = input("")
    price = 8
    quantity = input("How many do you wish for? \n")
    total = price * int(quantity)
    print(total)
    print("Thank your total is $" + str(total))
    print("Sounds great " + name + ", we'll have your " + quantity + " " + order + " right out for you.")
else:
    print("Get out of here!")