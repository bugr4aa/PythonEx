import turtle

turtle.speed(3)
turtle.bgcolor('white')
turtle.pensize(3)

def func():
	for i in range(400):
		turtle.right(1)
		turtle.forward(1)

turtle.color('red','red')
turtle.begin_fill()

turtle.left(140)
turtle.forward(111.65)

func()
turtle.left(120)

func()

turtle.forward(111.65)
turtle.end_fill()

turtle.hideturtle()
turtle.done()
