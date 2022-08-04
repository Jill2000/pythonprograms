import turtle

j = turtle.getscreen()
tur = turtle.Turtle()
turtle.bgcolor("black")
tur.pensize(5)
#tur.fd(50)

tur.penup()
tur.rt(90)
tur.fd(50)
tur.lt(90)
tur.pendown()
tur.color("red")
#head
tur.circle(150)

tur.penup()
tur.lt(90)
tur.fd(200)
tur.lt(90)
tur.fd(80)
tur.pendown()
tur.begin_fill()
#eyes
tur.circle(20)
tur.end_fill()
tur.penup()
tur.bk(160)
tur.pendown()
tur.begin_fill()
tur.circle(20)
tur.end_fill()
tur.penup()
tur.home()

tur.bk(100)
tur.lt(90)
tur.fd(70)
tur.rt(90)

#mouth
tur.down()
tur.right(90)
tur.circle(100, 180)

#nose
tur.up()
tur.goto(0,100)
tur.shape("turtle")


