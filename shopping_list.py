#!/usr/bin/env python

#Theophrastus Gamboni-Diehl
#CS3080 001 
#What does the program do

#Added a try except block so only an int can get in
def promptForInteger(min, max, message, errorMsg):
	
  try:
    response = int(input(message))

    while (response < min or response > max):
      response = int(input(errorMsg))
    
    return response
  except ValueError:
    return promptForInteger(min, max, message, errorMsg)
#menu
def menu():
  print('''Welcome to your Shopping List!
***********************************
1 - Add an item to the list
2 - Remove an item from the list
3 - Print the list
4 - Quit
***********************************''')

  MIN_MENU = 1
  MAX_MENU = 4

  menuChoice = "Please make a selection from the menu.\n"
  menuError ="That is an invalid number, please select from the menu.\n"




  menuChoice = promptForInteger(MIN_MENU,MAX_MENU,menuChoice,menuError)
  return menuChoice


def promptForString(message, errorMsg):
  response = input(message)

  while(response == '' ):
    print(errorMsg)
    response = input(message)

  return response

def handleAddItem(groceryList):

  addItemChoice = "Please enter the name of your item.\n"
  addItemError = "You didn't enter anything, please enter a valid name"


  print("You have chosen to add an item.")
  groceryChoice = promptForString(addItemChoice,addItemError)


  if groceryChoice in groceryList:
    print("You already have " + {1} + "on your grocery list.", groceryChoice)
  else:
    groceryList.append(groceryChoice)
    print("You've added " + {1} + " to your grocery list.", groceryChoice)

  return groceryList

def handleRemoveItem(groceryList):
  print("lol")


def handlePrintList(groceryList):
  for item in groceryList:
    print(item)



#######################################################################


addItemChoice = "Please enter the name of your item.\n"
addItemError = "You didn't enter anything, please enter a valid name"

removeItemChoice = "Please enter the name of your item.\n"
removeItemError = "You didn't enter anything, please enter a valid name for your item.\n"


flagChoice = 1
while flagChoice:

  
  menuChoice = menu()

  shoppinglist = []

  if menuChoice == 1:
    handleAddItem(shoppinglist)
    continue
  elif menuChoice ==2:
    print("You have chosen to remove an item.")
  elif menuChoice == 3:
    handlePrintList(shoppinglist)
  elif menuChoice ==4:
    flagChoice = 0
    print("Thank you, goodbye!")
    break

# Menu selection



  
  




# Messages for adding an item
'''



"Would you like to add it to your list again (y/Y/n/N)?\n"
"You didn't indicate a response, please try again.\n"
"You've added <name> to your grocery list."
"Ok, I won't add <name> to your grocery list."
'''

# Messages for removing an item
'''


"You've removed <name> to your grocery list."
"Sorry, <name> was not on your list."
'''

# Print the list to the user in alphabetical order
'''
"You have chosen to print your list"
"Your list is empty."
'''

# Welcome message
#"Welcome to your Shopping List!"



# Goodbye message
#"Thank you, goodbye!"