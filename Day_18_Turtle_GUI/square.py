#Draw a square python GUI

from turtle import Turtle, Screen

timmy_the_turtle = Turtle()

timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")

for _ in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)

screen = Screen()
screen.exitonclick()
