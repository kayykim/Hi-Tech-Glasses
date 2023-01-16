import time

#introduction
def menu ():
    print ()
    print ("Settings")
    print ()
    print ("Enter 1: Change display message")
    print ("Enter 2: Change Language")
    print ("Enter 3: Change Transparency")
    print ("Enter 4: Personalization")
    print ("Enter 5: Change speaker volume")
    print ("Enter 6: Exit")

def display():
    print ("Would you like to view with")
    display = int (input("Sign Language (1) or Text? (2) "))

    while display != 1 and display != 2:
        print ("Please enter a valid choice")
        display = int (input("Sign Language (1) or Text? (2) "))

    if display == 1:
        return ("Sign Language")
    else:
        return ("Text")


# Main Program 
menu ()

# input from user
choice = int(input("Option: "))

    # error checking
while choice > 6 or choice < 0:
    print ("Please enter a valid option")
    choice = int(input("Option: "))
    print ("Your settings have been adjusted")

while choice != 6:
    if choice == 1:
        print (display())

    time.sleep(1)
    menu()
    choice = int(input("Option: "))


print ("You've exited settings")
    
    elif choice == 1:
        print ("Would you like to view with")
        display = int (input("Sign Language (1) or Text? (2) "))

    elif choice == 2:
        print ("Select a language: ")
        language = input ("English, Spanish, French, Mandarin, Urdu, Korean ")
        language = language.lower()
        print ("Your settings have been adjusted.")
    
    time.sleep(1)
    menu()
    choice = int (input(""))


print ("You have exited Settings.")
