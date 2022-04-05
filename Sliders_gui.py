import turtle

wn = turtle.Screen()
wn.title("david Sliders")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer(0)

#score trace
score_a = 0
score_b = 0

#paddel a
paddel_a = turtle.Turtle()
paddel_a.speed(0)
paddel_a.shape("square")
paddel_a.color("white")
paddel_a.shapesize(stretch_wid = 5, stretch_len = 1)
paddel_a.penup()
paddel_a.goto(-390, 0)

#paddel b
paddel_b = turtle.Turtle()
paddel_b.speed(0)
paddel_b.shape("square")
paddel_b.color("white")
paddel_b.shapesize(stretch_wid = 5, stretch_len = 1)
paddel_b.penup()
paddel_b.goto(390, 0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.shapesize(stretch_wid = 0.7, stretch_len = 0.7)
ball.penup()
ball.goto(0,0)
ball.dx = 0.2
ball.dy = 0.2

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("yellow")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A:{} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 20, "normal"))

#functions
def paddel_a_up():
    if paddel_a.ycor() == 240:
        y = paddel_a.ycor()
    else:
        y = paddel_a.ycor()
        y += 20
    paddel_a.sety(y)
    
def paddel_a_down():
    if paddel_a.ycor() == -240:
        y = paddel_a.ycor()
    else:
        y = paddel_a.ycor()
        y -= 20
    paddel_a.sety(y)
    
def paddel_b_up():
    if paddel_b.ycor() == 240:
        y = paddel_b.ycor()
    else:
        y = paddel_b.ycor()
        y += 20
    paddel_b.sety(y)
    
def paddel_b_down():
    if paddel_b.ycor() == -240:
        y = paddel_b.ycor()
    else:
        y = paddel_b.ycor()
        y -= 20
    paddel_b.sety(y)

wn.listen()
wn.onkeypress(paddel_a_up, "w")
wn.onkeypress(paddel_a_down, "s")
wn.onkeypress(paddel_b_up, "Up")
wn.onkeypress(paddel_b_down, "Down")

while True:
    wn.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    #borders conditions
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A:{} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 20, "normal"))
    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A:{} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 20, "normal"))

    if (ball.xcor() > 370 and ball.xcor() < 380) and (ball.ycor() < paddel_b.ycor() + 50 and ball.ycor() > paddel_b.ycor() - 50):
        ball.dx *= -1

    if (ball.xcor() < -370 and ball.xcor() > -380) and (ball.ycor() < paddel_a.ycor() + 50 and ball.ycor() > paddel_a.ycor() - 50):
        ball.dx *= -1
















    
