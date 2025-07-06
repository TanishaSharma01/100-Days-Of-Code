#CLASSES AND OBJECTS

# import another_module
# print(another_module.another_variable)

# from turtle import Turtle, Screen
#
# # turtle object
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100)
#
# my_screen = Screen()
# #attributes
# print(my_screen.canvheight)
#
# #object methods
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokemon Name",
["Pikachu","Charizard","Squirtle"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "r"
print(table)