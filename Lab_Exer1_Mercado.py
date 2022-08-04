import turtle

j = turtle.getscreen()
t = turtle.Turtle()
t.shape("turtle")
t.pensize(5)

def move_left():
  t.penup()
  t.setheading(180)
  t.fd(100)
def move_right():
  t.penup()
  t.setheading(0)
  t.fd(100)
def move_up():
  t.penup()
  t.setheading(90)
  t.fd(100)
def move_down():
  t.penup()
  t.setheading(270)
  t.fd(100)
###########################################
def draw_octagon():
  t.pendown()
  t.color("cyan")
  for i in range(8):
    
    t.fd(50)
    t.rt(90)
    t.lt(45)
  t.penup()

def draw_circle():
  t.color("black")
  t.pendown()
  t.fillcolor("blue")
  t.begin_fill()
  t.circle(80)
  t.end_fill()
    
  t.penup()

def draw_triangle():
  t.pendown()
  t.color("red")
  for i in range(3):
    t.fd(100)
    t.lt(120)
  t.penup()


screen =turtle.Screen()
screen.listen()

screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")

screen.onkey(draw_octagon, "o")
screen.onkey(draw_circle, "c")
screen.onkey(draw_triangle, "t")

