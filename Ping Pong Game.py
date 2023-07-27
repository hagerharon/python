import turtle
#great screen  its' proparties
wind = turtle.Screen()
wind.title("Ping Pong game")
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0)

#player1
mardrab1 = turtle.Turtle()  #intializes turtle object
mardrab1.speed(0)  # set speed of animation
mardrab1.shape("square")
mardrab1.color("blue")
mardrab1.shapesize(stretch_wid=5, stretch_len=1)
mardrab1.penup()
mardrab1.goto(-350, 0)

#player2
mardrab2 = turtle.Turtle()
mardrab2.speed(0)
mardrab2.shape("square")
mardrab2.color("red")
mardrab2.shapesize(stretch_wid=5, stretch_len=1)
mardrab2.penup()
mardrab2.goto(350, 0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2.5
ball.dy = 2.5

#sore
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("player 1: 0 player 2: 0",
            align="center",
            font=("Courier", 24, "normal"))
#test code
print("right")


#functions to control in madrab1
def mardrab1_up():
  y = mardrab1.ycor()  #get y coordinate of madrab1
  y += 20  # change position 20px
  mardrab1.sety(y)  #save the new position of madrab1


def mardrab1_down():
  y = mardrab1.ycor()
  y -= 20
  mardrab1.sety(y)


#functions to control in madrab2
def mardrab2_up():
  y = mardrab2.ycor()
  y += 20
  mardrab2.sety(y)


def mardrab2_down():
  y = mardrab2.ycor()
  y -= 20
  mardrab2.sety(y)


#keyboard bindings
wind.listen()  #tell the window to except keyyboard input
wind.onkeypress(mardrab1_up, "w")  # when pressing w call function madrab1_up
wind.onkeypress(mardrab1_down, "s")
wind.onkeypress(mardrab2_up, "d")
wind.onkeypress(mardrab2_down, "a")

while True:
  wind.update()  # update screen when the loop run

  #move the ball
  ball.setx(ball.xcor() + ball.dx)
  ball.sety(ball.ycor() + ball.dy)

  #check border
  if ball.ycor() > 290:
    ball.sety(290)
    ball.dy *= -1

  if ball.ycor() < -290:
    ball.sety(-290)
    ball.dy *= -1

  if ball.xcor() > 390:
    ball.goto(0, 0)
    ball.dx *= -1
    score1 += 1
    score.clear()
    score.write("player 1: {} player 2: {}".format(score1, score2),
                align="center",
                font=("Courier", 24, "normal"))
  if ball.xcor() < -390:
    ball.goto(0, 0)
    ball.dx *= -1
    score2 += 1
    score.clear()
    score.write("player 1: {} player 2: {}".format(score1, score2),
                align="center",
                font=("Courier", 24, "normal"))
  #collision ball
  if (ball.xcor() > 340
      and ball.xcor() < 350) and (ball.ycor() < mardrab2.ycor() + 40
                                  and ball.ycor() > mardrab2.ycor() - 40):
    ball.setx(340)
    ball.dx *= -1
  if (ball.xcor() < -340
      and ball.xcor() > -350) and (ball.ycor() < mardrab1.ycor() + 40
                                   and ball.ycor() > mardrab1.ycor() - 40):
    ball.setx(-340)
    ball.dx *= -1

#test code
print("good")
