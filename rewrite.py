import matplotlib.pyplot as plt
import math

x_points = list(range(1000))
y_points = list(range(1000))

def linear():
    for i in range(len(x_points)):
        current_x_point = x_points[i]
        next_y_point = current_x_point
        y_points[i] = next_y_point

def sine():
    wavelength = 100

    for i in range(len(x_points)):
        current_x_point = x_points[i]
        next_y_point = math.sin((math.radians(current_x_point * 360 / wavelength)))
        y_points[i] = next_y_point

def cosine():
    wavelength = 100

    for i in range(len(x_points)):
        current_x_point = x_points[i]
        next_y_point = math.cos((math.radians(current_x_point * 360 / wavelength)))
        y_points[i] = next_y_point

def tangent():
    for i in range(len(x_points)):
        current_x_point = x_points[i]
        next_y_point = math.tan(current_x_point)
        y_points[i] = next_y_point

def quadratic():
    for i in range(len(x_points)):
        current_x_point = x_points[i]
        next_y_point = current_x_point**2
        y_points[i] = next_y_point


def reciprocal():
    wavelength = 50

    for i in range(len(x_points)):
        current_x_point = x_points[i]
        if current_x_point == 0:
            continue
        x_mapped = current_x_point / wavelength
        next_y_point = 1 / x_mapped
        y_points[i] = next_y_point

def square_root():
    for i in range(len(x_points)):
        current_x_point = x_points[i]
        next_y_point = math.sqrt(current_x_point)
        y_points[i] = next_y_point

def logarithmic():
    for i in range(len(x_points)):
        current_x_point = x_points[i]
        if current_x_point == 0:
            continue
        next_y_point = math.log(current_x_point)
        y_points[i] = next_y_point

def expontential():
    scale = 0.2

    for i in range(len(x_points)):
        current_x_point = x_points[i]
        next_y_point = math.e**(current_x_point * scale)
        y_points[i] = next_y_point

def cubic():
    for i in range(len(x_points)):
        current_x_point = x_points[i]
        next_y_point = current_x_point**3
        y_points[i] = next_y_point


def modulus():
    for i in range(len(x_points)):
        current_x_point = x_points[i]
        next_y_point = abs(current_x_point)
        y_points[i] = next_y_point

plt.plot(x_points, y_points)
plt.axvline(x=0, color="black", linewidth=1)
plt.axhline(y=0, color="black", linewidth=1)
plt.show()