#Creating a random walk using turtle GUI
import random
from turtle import Turtle, Screen
import turtle

turtle.colormode(255)
timmy_the_turtle = Turtle()
timmy_the_turtle.pensize(0)
timmy_the_turtle.speed("fastest")
timmy_the_turtle.penup()
timmy_the_turtle.goto(-200, -300)
timmy_the_turtle.pendown()

# colors we extracted from image.jpg
new_colors_list = [(219, 173, 124), (159, 180, 190), (134, 73, 53), (49, 102, 153), (245, 232, 236), (118, 82, 93), (179, 140, 150),
                   (41, 46, 65), (162, 104, 151), (126, 173, 114)]

def random_color():
    random_color = random.choice(new_colors_list)
    return random_color

x_coord = timmy_the_turtle.xcor()
y_coord = timmy_the_turtle.ycor()

for i in range(1, 11):
    for j in range(0,10):
        timmy_the_turtle.color(random_color())
        timmy_the_turtle.dot(20)
        timmy_the_turtle.penup()
        timmy_the_turtle.forward(50)
        timmy_the_turtle.pendown()
    timmy_the_turtle.penup()
    timmy_the_turtle.left(90)
    timmy_the_turtle.goto(x_coord, y_coord + (i * 50))
    timmy_the_turtle.right(90)

timmy_the_turtle.hideturtle()
screen = Screen()
screen.exitonclick()
