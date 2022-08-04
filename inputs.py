import time
name = input("Enter your name: ")
score = 0
def scorePlus():
    global score
    score += 1
    print("Your new score: ",score)
def scoreMinus():
    global score
    score -= 1
    print("Your new score: ",score)
def q1():
    global score
    time.sleep(0.5)
    print("\n1. What is 9x9? ")
    print("a) 82")
    print("b) 81")
    print("c) 85\n")

    answer = str(input("Answer: "))

    if answer == "b":
        print("Correct! ")
        scorePlus()
    else:
        print("Wrong Answer")
        scoreMinus()
    q2()

def q2():
    global score
    time.sleep(0.5)
    print("\n2. What is 5x5? ")
    print("a) 24")
    print("b) 25")
    print("c) 35\n")

    answer = str(input("Answer: "))

    if answer == "b":
        print("Correct! ")
        scorePlus()
    else:
        print("Wrong Answer")
        scoreMinus()
    q3()

def q3():
    global score
    time.sleep(0.5)
    print("\n3. What is 2x20? ")
    print("a) 40")
    print("b) 20")
    print("c) 50\n")

    answer = str(input("Answer: "))

    if answer == "a":
        print("Correct! ")
        scorePlus()
    else:
        print("Wrong Answer")
        scoreMinus()
    q4()
def q4():
    global score
    time.sleep(0.5)
    print("\n4. What is the fullname of Omar ")
    print("a) Sultan")
    print("b) Arafat")
    print("c) Mercado\n")

    answer = str(input("Answer: "))

    if answer == "b":
        print("Correct! ")
        scorePlus()
    else:
        print("Wrong Answer")
        scoreMinus()
    q5()
def q5():
    global score
    time.sleep(0.5)
    print("\n5. Who is the friend of Omar ")
    print("a) Moe Sargi")
    print("b) Jannine Ann")
    print("c) Noynoy\n")

    answer = str(input("Answer: "))

    if answer == "a":
        print("Correct! ")
        scorePlus()
    else:
        print("Wrong Answer")
        scoreMinus()

q1()
print("Congrats "+name)
