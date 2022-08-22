# Instruction for this caotic amazing journey:


print("Hello, welcome to ITAMAESAN Coffee!!!!!!!!!")

name = input("What is your name?\n")

if name == "Ben" or name == "Patricia" or name == "Loki":
    evil_status = input("Are you evil?\n")
    good_deeds = int(input("How many good things you did today? " + name + "?\n"))
    if evil_status == "yes" and good_deeds < 4:
        print("You're not welcome here " + name + " Get out of here!")
        exit()
    else:
        print("Okay, come in!\n")
else:
    print("Hello " + name + ", welcome to the coffee shop. \n\n\n")