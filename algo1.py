
def test():
        attempt = 1
        num1 = input("Enter your first number: ")
        [num2 = input("Enter your second number: ")
        if num1 == num2:
                print("The first number is equal to the second numnber")
        elif num1 > num2:
                print("The first number is greater than the second number")
        elif num1 < num2:
                print(" The first number is less than the second number ")

        print("Do you want to 'do it' again or 'nah'? ")
        do1 = "do it"
        nah1 = "nah"
        do2= input()
        if do1 == do2:
                #while attempt < 5:
                        test()
        elif do2 == nah1:
                exit()
test()
