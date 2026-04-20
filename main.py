import turtle
import math

def select_function():
    print("What function do you want to visualise? \n")

    print("1. Linear \n")
    print("2. Quadratic")

    choice = input("> ")

    return choice

meow = turtle.Turtle()
meow.hideturtle()

def draw_x_y(length):
    global graph_origin
    global graph_length
    global top_right_graph

    graph_length = length

    top_pos = meow.ycor()
    meow.right(90)
    meow.forward(length)

    graph_origin = meow.position()

    meow.left(90)
    meow.forward(length)

    right_pos = meow.xcor()

    top_right_graph = [right_pos, top_pos]




def turtle_to_origin():
    meow.setpos(graph_origin)
    meow.setheading(0)

def x_equals_y():
    turtle_to_origin()

    meow.left(45)

    fwd_amt = math.sqrt((graph_length**2)*2)
    meow.forward(fwd_amt)

def quadratic():
    turtle_to_origin()

    scale = 0.005  # vertical scale for x^2 (smaller => flatter)
    step = 1        # pixels to move horizontally per loop

    while (meow.xcor() < top_right_graph[0]) and (meow.ycor() < top_right_graph[1]):
        meow.forward(step)
        current_x = meow.xcor() - graph_origin[0]
        up_amount = (current_x ** 2) * scale

        meow.setpos(meow.xcor(), graph_origin[1] + up_amount)



draw_x_y(300)
choice = select_function()
if choice == "1":
    x_equals_y()
if choice == "2":
    quadratic()

turtle.done()