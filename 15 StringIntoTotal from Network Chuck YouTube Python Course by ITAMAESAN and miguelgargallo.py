#Let's build robot barista!!!

print("Hello, and welcome to the ITAMEASAN Cofe shop!!!!!!")

name = input("Waht is your name? \n")

print("Hello " + name+"," + " Thank you so much for coming to our shop. \n\n")

menu = "Black Coffe, Espresso, Latte, Capuccino"

print(name + "what would you like to order? \n" + menu)

order = input()

price = 8

quantity = input("How many do you wish for? \n")

total = price * int(quantity)

print(total)

print("Thank your total is $" + str(total))

print("Sounds great " + name + ", we'll have your " + quantity + " " + order + " right out for you.")