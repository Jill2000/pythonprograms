
def number():
  for i in range(3):
    
    digit = int(input("Enter 6-digit number: "))#ma error pag string ang i input
    deletedDigit = digit % 15 #kuhaon ra nya ang last number
    newDigit = digit// 10 #5 digit only
    remainder = newDigit - (newDigit // 7 * 7 )

    if (remainder == deletedDigit):
      print("True")
    else:
      print("False")
  
                                        #julianjillmercado <3
number()






