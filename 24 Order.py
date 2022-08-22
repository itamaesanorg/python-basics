# Here we will use a while loop to keep asking the customer for the quantity of the order until they enter a valid number.

# Coffee menu
menu = "Black Coffe, Espresso, Latte, Capuccino, Frappuccino\n"

name = input("What is your name? \n")

# Ask the customer what they want to order, and store it in a variable called order.
order = input(name + ", what would you like to order? Here is what we serve: " + menu + "\n")

# Calculate the total price of the order, and store it in a variable called total.
if order == "Frappuccino":
    price_Frappucino = 13
    quantity = input("How many do you wish for? \n")
    print("Okay, I will prepeare your " + quantity + " " + order + " for you.")
    print("Your total is $" + str(price_Frappucino * int(quantity)))
else:
    quantity = input("How many do you wish for? \n")
    price = 8
    print("Okay, I will prepeare your " + quantity + " " + order + " for you.")
    print("Your total is $" + str(price * int(quantity)))

    
    
# Ask the customer how many of the order they want, and store it in a variable called quantity.



