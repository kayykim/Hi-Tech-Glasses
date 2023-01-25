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
    
    
# option 2 -------------------------------
def languageFunc():

    # show options 
    options = ("english", "spanish", "french", "mandarin", "urdu", "korean")
    print ("Select a language: ")

    # user input
    language = input (options)
    language = language.lower()

    while language not in options:
        print ("That is not an option")
        print()
        print ("Select a language: ")
        language = input (options)
        language = language.lower()

    return language


# option 3 -------------------------------
def transparencyFunc():
    level = int(input ("Enter from 0 to 100 to select transparency (0-transparent): "))
    while level > 100 or level < 0:
        print ("Not a valid option")
        level = int(input ("Enter from 0 to 100 to select transparency: "))

    return level
    
    
# option 4 -------------------------------
def colourFunc():

    # show colour
    choices = ("red", "orange", "yellow", "green", "blue", "purple", "black")
    print (choices)

    # user input
    option = input ("Select a colour: ")
    option = option.lower()

    while option not in choices:
        print ("That is not an option")
        print()
        print ("Select a colour: ")
        option = input (choices)
        option = choices.lower()

    return option


# option 5 -------------------------------
def volumeFunc():

    # user input
    level = int(input ("Enter from 0 to 100 to select volume (0-mute): "))
    while level > 100 or level < 0:
        print ("Not a valid option")
        level = int(input ("Enter from 0 to 100 to select volume: "))
        print ("saved")

    return level


# Main Program ===========================

choice = 1

while choice != 6:
    menu ()
    choice = int(input("Option: "))

    if choice == 1:
        display = (displayFunc())
        print ("saved")
    
    elif choice == 2:
        language = (languageFunc())
        print ("saved")
        
    elif choice == 3:
        transparency = transparencyFunc()
        print ("saved")
       
    elif choice == 4:
        colour = colourFunc()
        print ("saved")
        
    elif choice == 5:
        volume = volumeFunc()
        print ("saved")
        
    else: 
        break

print ("Your settings have been adjusted to: ")
print ("Display: ", display)
print ("Language: ", language)
print ("Transparency: ", transparency)
print ("Personalization: ", colour)

