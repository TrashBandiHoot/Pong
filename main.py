from turtle import Screen, Turtle

screen = Screen()
paddle = Turtle()


screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)






paddle.shape("square")
paddle.color("white")
paddle.penup()
paddle.goto(350, 0)
paddle.shapesize(stretch_len=1, stretch_wid=5)



def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)


def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)


screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

flag = True

while flag:
    screen.update()


screen.exitonclick()