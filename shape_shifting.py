#!/usr/bin/env python

#Theophrastus Gamboni-Diehl
#CS3080 001 shape_shifting
#Program creates different shapes

def promptForInteger(min, max, message, errorMsg):
	
  try:
    response = int(input(message))

    while (response < min or response > max):
      response = int(input(errorMsg))
    
    return response
  except ValueError:
    return promptForInteger(min, max, message, errorMsg)

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
def getMenu():
  messageMenu = "Please select from the menu (1 to 8)?\n"
  errorMenu = "Your response must be number between 1 and 8, try again.\n"
  return promptForInteger(1,8,messageMenu,errorMenu)
  

def getShape():
  messageShape = "What size should we use for your shapes (1 to 20)?\n"
  errorShape = "Your response must be number between 1 and 20, try again.\n"
  return promptForInteger(1,20,messageShape,errorShape)

def drawSqr(size):

  square = ["*"*size for i in range(size)]
  for unit in square:
    print(unit)


def drawRight(size):
  rightTriangle = ['*'*(i+1) for i in range(size)]
  for unit in rightTriangle:
    print(unit)

def isosceles(size):
  
  triangle = ['*' * (2*i+1) for i in range(size)]
  for unit in triangle:
    print(unit.center(size*2+1))

def invertIsosceles(size,flag=False):
  triangle = ['*' * (2*i+1) for i in range(size-1,-1,-1)]
  if flag:
    triangle.remove("*")
  for unit in triangle:
    print(unit.center(size*2+1))

def diamond(size):
  isosceles(size-1)
  print('*'*(size*2-1))
  invertIsosceles(size-1)

def hourglass(size):
  invertIsosceles(size, flag=True)
  isosceles(size)

def house(size):
  print("house")

  

menuItem = 0
shapeSize = 0

while menuItem != 8:
  
  menu()
  menuItem = getMenu()
  if menuItem != 8:
    shapeSize = getShape()


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







