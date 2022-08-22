
print("Hello, welcome to ITAMAESAN Coffee!!!!!!!!!")

name = input("What is your name?\n")

if name == "Ben" or name == "Patricia":
    evil_status = input("Are you evil?\n")
    if evil_status == "Yes":
        print("You're not welcome here " + name + " Get out of here!")
        exit()
    else:
        print("Oh! You are one of those good " + name + "\n Come in! \n\n\n")
else:
    print("Hello " + name + ", welcome to the coffee shop. \n\n\n")
    
beard_length = int(input("How long is your beard?\n"))

if beard_length >= 1:
    print("*oh, hello good, nice beard. You may go to the front of the line.")
else:
    print("*oh, hello good, nice beard. You may go to the back of the line.")

