def classmate():
  name1 = input("Enter your first classmate: ")
  name2 = input("Enter your second classmate: ")
  name3 = input("Enter your third classmate: ")

  list_name = []
  list_name.append(name1)
  list_name.append(name2)
  list_name.append(name3)
  print(list_name)

  print("Try again? y/n")
  again = input()
  if(again=='y'):
    classmate()
  elif(again=='n'):
    exit()
classmate()
  
