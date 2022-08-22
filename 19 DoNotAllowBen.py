# We are going to discover If and Else statements in this program too.

print("Welcome to the coffee shop!")

name = input("What is your name? \n")

menu = "Black Coffe, Espresso, Latte, Capuccino"

if name == "Ben":
    print("Hello " + name + ", welcome to the coffee shop. \n")
    print("We have the following drinks: " + menu)
    print(name + "what would you like to order? \n" + menu)

    order = input()

    price = 8

    quantity = input("How many do you wish for? \n")

    total = price * int(quantity)

    print(total)

    print("Thank your total is $" + str(total))

    print("Sounds great " + name + ", we'll have your " + quantity + " " + order + " right out for you.")

else:
    print("I don't like you, " + name + " quits the coffee shop.")
    