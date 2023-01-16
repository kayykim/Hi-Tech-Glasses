#introduction
print ("Settings")
print ()
print ("Enter 1: Change display message")
print ("Enter 2: Change Language")
print ("Enter 3: Change Transparency")
print ("Enter 4: Personalization")
print ("Enter 5: Change speaker volume")
print ("Enter 6: Exit")

# input from user
choice = int(input("Option: "))

    # error checking
while choice > 6 or choice < 0:
    print ("Please enter a valid option")
    choice = int(input("Option: "))

print (choice)