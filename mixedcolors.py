tupleColors = ("red","yellow","blue")
def space():
	print("\n")
def choosing():
  
  print("Enter the color you want to mix")
  space()
  first_color = input("Enter the first color: ")
  second_color = input("Enter the second color: ")

  if ( first_color == tupleColors[0] and second_color == tupleColors[2]) or ( first_color == tupleColors[2] and second_color == tupleColors[0]):
          print(first_color + " + " + second_color + " = VIOLET " )

  elif ( first_color == tupleColors[0] and second_color == tupleColors[1]) or ( first_color == tupleColors[1] and second_color == tupleColors[0]):
          print(first_color + " + " + second_color + " = ORANGE " )

  elif ( first_color == tupleColors[1] and second_color == tupleColors[2]) or ( first_color == tupleColors[2] and second_color == tupleColors[1]):
          print(first_color + " + " + second_color + " = GREEN " )
  else:
    print("Error: Only primary colors are allowed")
  space()
  y = input("Press y if you want to mix another color ")
  if(y == "y"):
    choosing()
  else:
    quit()
choosing()
space()

