# Lets play with if if if if else!!!
name = input("What is your name\n")
# Great the customer with their name and thank them for coming in today using concatenation.

if name == "Ben":
 evil_status = input("\n Are you evil?\n")
 if evil_status == "Y" or "y" or "Ye" or "ye" or "YES" or "Yes" or "yes" or "Of course" or "of course" or "ofcourse" or "Ofcourse":
  print("You're not welcome here Ben! Get out of here!")
  exit()
else:
 print("Hello " + name + ", welcome to the coffee shop. \n\n\n")