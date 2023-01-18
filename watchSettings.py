# Name: Kay Kim

# default settings
display = "sign language"
language = "english"
transparency = 60
colour = "black"
volume = 60

# introduction -------------------------------
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

    
# option 1 -------------------------------
def displayFunc():
    
    # user input
    print ("Would you like to view with")
    display = int (input("Sign Language (1) or Text? (2) "))

    while display != 1 and display != 2:
        print ("Please enter a valid choice")
        display = int (input("Sign Language (1) or Text? (2) "))

    if display == 1:
        return ("Sign Language")
    else:
        return ("Text")


# Main Program ===========================

choice = 1

while choice != 6:
    menu ()
    choice = int(input("Option: "))

    if choice == 1:
        display = (displayFunc())
        print ("saved")


