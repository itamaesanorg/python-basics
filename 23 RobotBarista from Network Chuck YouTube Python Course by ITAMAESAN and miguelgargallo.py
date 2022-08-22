# Coffee menu
menu = "Black Coffe, Espresso, Latte, Capuccino, Frappuccino\n"
name = input("What is your name? \n")

# Ask the customer what they want to order, and store it in a variable called order.
order = input(name + ", what would you like to order? Here is what we serve: " + menu + "\n")

# Calculate the total price of the order, and store it in a variable called total.
if order == "Frappuccino":
    price = 13
else:
    price = 8
# Ask the customer how many of the order they want, and store it in a variable called quantity.
quantity = input("How many do you wish for? \n")


