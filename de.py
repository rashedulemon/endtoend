import turtle

def draw_heart():
    turtle.color("red")
    turtle.begin_fill()

    turtle.left(140)
    turtle.forward(180)
    turtle.circle(-90, 200)
    turtle.left(120)
    turtle.circle(-90, 200)
    turtle.forward(180)

    turtle.end_fill()

def write_love():
    turtle.penup()
    turtle.goto(0, -180)
    turtle.pendown()
    turtle.color("black")
    turtle.write("For You ❤️", align="center", font=("Arial", 24, "bold"))

# Setup Turtle
turtle.bgcolor("white")
turtle.title("Turtle Heart of Love")
turtle.speed(2)

draw_heart()
write_love()

turtle.hideturtle()
turtle.done()
