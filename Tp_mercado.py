#                           TITLE : TURTLE RUSH                                   #
#                                                                                 #
############################# INSTRUCTION! ########################################
#       Your character is the turtle, try to chase the and eat the red apple      #
#     to gain score.                                                              #
#     Moves:                                                                      #
#     arrow left : to turn left                                                   #
#     arrow right : to turn right                                                 #
#     arrow up : to increase your speed                                           #
#     arrow down: to decrease your speed                                          #
#     R key : to reset your turtle if ever get stuck                              #
#                                                                                 #
####### SUBMITTED BY JULIAN JILL MERCADO###########################################


import turtle
import math
import random

j = turtle.getscreen()
j.bgcolor("cyan")


#draw border
border = turtle.Turtle()
border.penup()
border.setposition(-300,-300)
border.pendown()
border.pensize(3)
for side in range(4): # para ni sa square border
  border.forward(600)
  border.lt(90)
border.hideturtle()

#t is the turtle
t = turtle.Turtle()
t.shape("turtle")
t.pensize(5)
t.penup()
t.speed(0)

#score
score = 0

#goal or the apple
goal = turtle.Turtle()
goal.color("red")
goal.shape("circle")
goal.penup()
goal.speed(0)
goal.setposition(random.randint(-300,300),random.randint(-300,300))

#speed of the turtle
speed = 1

#function
def move_left():
  t.left(30)
def move_right():
  t.right(30)
def inc_spd():
  global speed
  speed +=1
def dec_spd():
  global speed
  speed -=1
def reset():
  t.home()

def isCollision(t1,t2):
  r = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+ math.pow(t1.ycor()-t2.ycor(),2))
  if r < 20:
    return True
  else:
    return False
  
#key bindings
j =turtle.Screen()
j.listen()
j.onkey(move_left, "Left")
j.onkey(move_right, "Right")
j.onkey(inc_spd, "Up")
j.onkey(dec_spd, "Down")
j.onkey(reset, "r")



while True:
  t.forward(speed)

  #xboundary
  if t.xcor() > 290 or t.xcor() < -290:
    t.right(180)

  #yboundary
  if t.ycor() > 290 or t.ycor() < -290:
    t.right(180)

  #collision check
  if isCollision(t,goal):
    goal.setposition(random.randint(-290,290),random.randint(-290,290))
    goal.right(random.randint(0,360))
    score +=1

    #putting the score into the screen
    #print(score)
    border.undo()
    border.penup()
    border.hideturtle()
    border.setposition(-290,310)
    scorestring = "Score: %s" %score
    border.write(scorestring, False, align="left",font=("Arial",14,"normal"))

  #moving the prutas
  goal.forward(3)

  #xboundary
  if goal.xcor() > 290 or goal.xcor() < -290:
    goal.right(180)

  #yboundary
  if goal.ycor() > 290 or goal.ycor() < -290:
    goal.right(180)




