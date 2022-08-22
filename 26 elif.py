# Here we will use a while loop to keep asking the customer for the quantity of the order until they enter a valid number.

# Coffee menu
menu = "Black Coffe, Espresso, Latte, Capuccino, Frappuccino\n"

name = input("What is your name? \n")

# Ask the customer what they want to order, and store it in a variable called order.
order = input(name + ", what would you like to order? Here is what we serve: " + menu + "\n")

# Calculate the total price of the order, and store it in a variable called total.
    
    
if order == "Frappuccino":
    price = 13
elif order == "Black Coffe":
    price = 3
elif order == "Espresso":
    price = 5
elif order == "Latte":
    print("Do you want extra cream? \n")
    price = 9
    if input() == "yes":
        pricewithcream = price + 1
        quantity = input("How many do you wish for? \n")
        print("Your total is $" + str(pricewithcream * int(quantity)))
        exit()
    else:
        quantity = input("How many do you wish for? \n")
        print("Your total is $" + str(price * int(quantity)))
        exit()

elif order == "Capuccino":
    price = 10
else:
    print("Sorry, we don't serve that here.")
    price = 0






print("count that every " + order + "costs" + price + ", thanks for comming today, and see you soon" + name + "!")
