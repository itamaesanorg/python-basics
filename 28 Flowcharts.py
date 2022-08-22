# Instruction for this caotic amazing journey:


print("Hello, welcome to ITAMAESAN Coffee!!!!!!!!!")

name = input("What is your name?\n")

if name == "Ben" or name == "Patricia" or name == "Loki":
    evil_status = input("Are you evil?\n")
    if evil_status == "yes":
        print("You're not welcome here " + name + " Get out of here!")
        exit()
    else:
        print("How many good things you did today?" + name + "?")
        ans = input("")
        if ans > "4" or ans == "4":
            print("Okay, come in!")
        else:
            print("You are not welcome here " + name + "! Get out of here!")
else:
    print("Hello " + name + ", welcome to the coffee shop. \n\n\n")