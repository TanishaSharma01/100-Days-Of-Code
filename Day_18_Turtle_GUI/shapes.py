#Draw shapes with increasing number of edges python GUI
import random
from turtle import Turtle, Screen

timmy_the_turtle = Turtle()

timmy_the_turtle.shape("turtle")

def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(angle)

def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    timmy_the_turtle.color(r, g, b)

def random_color_2():
    colors = ["VioletRed", "LightBlue2", "ForestGreen", "DarkSlateBlue", "DarkRed"]
    color = random.choice(colors)
    timmy_the_turtle.color(color)

for i in range(3, 11):
    random_color_2()
    draw_shape(i)


screen = Screen()
screen.exitonclick()
