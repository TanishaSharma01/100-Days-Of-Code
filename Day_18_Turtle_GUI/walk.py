#Creating a random walk using turtle GUI
import random
from turtle import Turtle, Screen
import turtle

turtle.colormode(255)
timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.pensize(10)
timmy_the_turtle.speed("fastest")

def random_angle():
    angles = [0, 90, 180, 270, 360]
    angle = random.choice(angles)
    timmy_the_turtle.setheading(angle)
    # timmy_the_turtle.right(angle)
    timmy_the_turtle.forward(30)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color

def random_color_2():
    colors = ["VioletRed", "LightBlue2", "ForestGreen", "DarkSlateBlue", "DarkRed", "CornflowerBlue"
              , "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
    color = random.choice(colors)
    timmy_the_turtle.color(color)

for _ in range(0, 100):
    timmy_the_turtle.color(random_color())
    random_angle()

screen = Screen()
screen.exitonclick()
