#!/usr/bin/env python

#Theophrastus Gamboni-Diehl
#CS3080 001 shape_shifting
#Program creates different shapes


#Added a try except block so only an int can get in
def promptForInteger(min, max, message, errorMsg):
	
  try:
    response = int(input(message))

    while (response < min or response > max):
      response = int(input(errorMsg))
    
    return response
  except ValueError:
    return promptForInteger(min, max, message, errorMsg)

#basic function for menue
def menu():

  print('''******************************
1 - Draw a Square
2 - Draw a Right Triangle
3 - Draw an Isosceles Triangle
4 - Draw a Flipped Isosceles Triangle
5 - Draw a Diamond
6 - Draw an Hourglass
7 - Draw a House
8 - Quit
******************************''')

#function to get the menu item from user
def getMenu():
  messageMenu = "Please select from the menu (1 to 8)?\n"
  errorMenu = "Your response must be number between 1 and 8, try again.\n"
  return promptForInteger(1,8,messageMenu,errorMenu)
  
#gets the size of the shape from the user
def getShape():
  messageShape = "What size should we use for your shapes (1 to 20)?\n"
  errorShape = "Your response must be number between 1 and 20, try again.\n"
  return promptForInteger(1,20,messageShape,errorShape)

#draws a square
def drawSqr(size):

  #makes size blocked units and stores size of them
  square = ["*"*size for i in range(size)]
  for unit in square:
    print(unit)

#makes a right triangle
def drawRight(size):

  #each item in list increases by 1 each iteration
  rightTriangle = ['*'*(i+1) for i in range(size)]
  for unit in rightTriangle:
    print(unit)

#makes an isosceles triangle
def isosceles(size):
  
  #puts an odd number of * sequentially in the list
  triangle = ['*' * (2*i+1) for i in range(size)]
  for unit in triangle:
    #had to center it in an area twice the size 
    print(unit.center(size*2+1))

#inverts Isosceles flag is used when needed for diamond function
def invertIsosceles(size,flag=False):

  #puts odd number into triangle list but starts at the last element
  triangle = ['*' * (2*i+1) for i in range(size-1,-1,-1)]
  #will remove the bottom point when used with diamond
  if flag:
    triangle.remove("*")

  #centers the lines
  for unit in triangle:
    print(unit.center(size*2+1))

#creates a diamond
def diamond(size):

  #takes out one level of triangles and inserts a line that both would share
  isosceles(size-1)
  print('*'*(size*2-1))
  invertIsosceles(size-1)

#creates a hourglass shape
def hourglass(size):

  #set the flag true to remove one "*" at the bottome
  invertIsosceles(size, flag=True)
  isosceles(size)

#creates a house using an isosceles and drawsqr
def house(size):
  isosceles(size-1)
  drawSqr(size*2-1)

#main part of program
__name__
menuItem = 0
shapeSize = 0

#user must press 8
while menuItem != 8:
  
  menu()

  #gets the users choice
  menuItem = getMenu()
  if menuItem != 8:
    #gets the size of the shape
    shapeSize = getShape()

    #based onn user choice will run appropriate functiong
    if menuItem == 1:
      print("Drawing Square of size " + str(shapeSize))
      drawSqr(shapeSize)
    elif menuItem == 2:
        print("Drawing Right Triangle of size "+ str(shapeSize))
        drawRight(shapeSize)
    elif menuItem == 3:
        print("Drawing Isosceles Triangle of size "+ str(shapeSize))
        isosceles(shapeSize)
    elif menuItem == 4:
        print("Drawing Inverted Isosceles Triangle of size "+ str(shapeSize))
        invertIsosceles(shapeSize)
    elif menuItem == 5:
        print("Drawing Diamond of size "+ str(shapeSize))
        diamond(shapeSize)
    elif menuItem == 6:
        print("Drawing Hourglass of size "+ str(shapeSize))
        hourglass(shapeSize)
    elif menuItem == 7:
        print("Drawing House of size "+ str(shapeSize))
        house(shapeSize)
    elif menuItem == 8:
        print("Thank you, Goodbye!")
  else:
    print("Thank you, Goodbye!")
    continue






