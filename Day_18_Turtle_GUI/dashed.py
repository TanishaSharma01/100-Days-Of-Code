# Draw a dashed line
from turtle import Turtle, Screen

timmy_the_turtle = Turtle()

timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")

for _ in range(25):
    timmy_the_turtle.pendown()
    timmy_the_turtle.forward(5)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(5)

screen = Screen()
screen.exitonclick()