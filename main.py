import turtle
import math

def select_function():
    print("What function do you want to visualise? \n")

    print("1. Linear")
    print("2. Quadratic")
    print("3. Sine")
    print("4. Cosine")
    print("5. Tangent")
    print("6. Reciprocal")
    print("7. Square Root")
    print("8. Cubic")
    print("9. Expontential")
    print("10. Logarithmic")

    print("\n")

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

def sine():
    turtle_to_origin()

    wavelength = 50 # increase to spread horizontally
    v_amp = 50
    step = 1

    while (meow.xcor() < top_right_graph[0]):
        meow.forward(step)

        current_x = meow.xcor() - graph_origin[0]
        angle = 2 * math.pi * current_x / wavelength
        v_shift = math.sin(angle) * v_amp

        meow.setpos(meow.xcor(), graph_origin[1] + v_shift)

def cosine():
    turtle_to_origin()

    wavelength = 50 # increase to spread horizontally
    v_amp = 50
    step = 1

    while (meow.xcor() < top_right_graph[0]):
        meow.forward(step)

        current_x = meow.xcor() - graph_origin[0]
        angle = 2 * math.pi * current_x / wavelength
        v_shift = math.cos(angle) * v_amp

        meow.setpos(meow.xcor(), graph_origin[1] + v_shift)

def tangent():
    turtle_to_origin()

    wavelength = 100 # increase to spread horizontally
    v_amp = 20
    step = 1

    while (meow.xcor() < top_right_graph[0]):
        meow.forward(step)

        current_x = meow.xcor() - graph_origin[0]
        angle = 2 * math.pi * current_x / wavelength
        v_shift = math.tan(angle) * v_amp

        meow.setpos(meow.xcor(), graph_origin[1] + v_shift)

def reciprocal():
    turtle_to_origin()

    step = 1
    h_stretch = 20
    v_scale = graph_length

    meow.penup()
    pen_on = False
    while (meow.xcor() < top_right_graph[0]):
        meow.forward(step)

        current_x = meow.xcor() - graph_origin[0]
        current_x = current_x / h_stretch

        if abs(current_x) < 1:
            continue

        if not pen_on:
            y_pos = (v_scale / current_x)
            meow.setpos(meow.xcor(), graph_origin[1] + y_pos)
            meow.pendown()
            pen_on = True
            
        else:
            y_pos = (v_scale / current_x)
            meow.setpos(meow.xcor(), graph_origin[1] + y_pos)

def square_root():
    turtle_to_origin()

    step = 1
    v_scale = 5

    while (meow.xcor() < top_right_graph[0]):
        meow.forward(step)

        current_x = meow.xcor() - graph_origin[0]
        y_shift = math.sqrt(current_x) * v_scale

        meow.setpos(meow.xcor(), graph_origin[1] + y_shift)

def cubic():
    turtle_to_origin()
    step = 1
    h_stretch = 100

    while (meow.ycor() < top_right_graph[1]):
        

        meow.forward(step)

        current_x = meow.xcor() - graph_origin[0]
        current_x = current_x / h_stretch
        y_shift = (current_x**3) * graph_length

        meow.setpos(meow.xcor(), graph_origin[1] + y_shift)

def exponential():
    turtle_to_origin()

    step = 1
    h_stretch = 0.01
    v_scale = 100

    while (meow.ycor() < top_right_graph[1]):
        meow.forward(step)

        current_x = meow.xcor() - graph_origin[0]
        current_x = current_x * h_stretch
        y_shift = (math.e**current_x) * v_scale


        meow.setpos(meow.xcor(), graph_origin[1] + y_shift)

def logarithmic():
    turtle_to_origin()
    step = 1
    y_amp = 20
    h_scale = 20

    while (meow.xcor() < top_right_graph[0]):
        meow.forward(step)

        current_x = meow.xcor() - graph_origin[0]
        math_x = 1 + (current_x / h_scale)
        y_shift = math.log(math_x) * y_amp

        meow.setpos(meow.xcor(), graph_origin[1] + y_shift)


draw_x_y(300)
choice = select_function()
if choice == "1":
    x_equals_y()
elif choice == "2":
    quadratic()
elif choice == "3":
    sine()
elif choice == "4":
    cosine()
elif choice == "5":
    tangent()
elif choice == "6":
    reciprocal()
elif choice == "7":
    square_root()
elif choice == "8":
    cubic()
elif choice == "9":
    exponential()
elif choice == "10":
    logarithmic()

turtle.done()