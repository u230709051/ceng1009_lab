# for i in range(100):
#     print("We like Python's turtles!")

# months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
# for month in months:
#     print("One of the months of the year is", month)

# numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]
# for number in numbers:
#     print(number)
#
# for number in numbers:
#     print(number, "squared is", number ** 2)

# import turtle
# wn = turtle.Screen()
# t = turtle.Turtle()
# t.speed(5)
#
# t.penup()
# t.goto(-250, 0)
# t.pendown()
# for i in range(3):
#     t.forward(70)
#     t.left(120)
#
# t.penup()
# t.goto(-120, 0)
# t.pendown()
# for i in range(4):
#     t.forward(70)
#     t.left(90)
#
# t.penup()
# t.goto(10, 0)
# t.pendown()
# for i in range(6):
#     t.forward(70)
#     t.left(60)
#
# t.penup()
# t.goto(200, 0)
# t.pendown()
# for i in range(8):
#     t.forward(70)
#     t.left(45)
#
# wn.exitonclick()

# import turtle
# sides = int(input("Enter the number of sides: "))
# length = int(input("Enter the length of the sides: "))
# color = input("Enter the color of the sides: ")
# fill = input("Enter the fill of the sides: ")
#
# wn = turtle.Screen()
# t = turtle.Turtle()
# t.color(color, fill)
#
# t.begin_fill()
# for i in range(sides):
#     t.forward(length)
#     t.left(360 / sides)
# t.end_fill()
# wn.exitonclick()

# import turtle
# wn = turtle.Screen()
# pirate = turtle.Turtle()
#
# angles = [160, -43, 270, -97, -43, 200, -940, 17, -86]
# for angle in angles:
#     pirate.left(angle)
#     pirate.forward(100)
#
# print("pirate's heading:", pirate.heading())
# wn.exitonclick()

# import turtle
# wn = turtle.Screen()
# t = turtle.Turtle()
#
# for i in range(5):
#     t.forward(150)
#     t.left(144)
#
# wn.exitonclick()

# import turtle
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
#
# t = turtle.Turtle()
# t.color("blue")
# t.shape("turtle")
# t.speed(0)
#
# t.penup()
# t.stamp()
# t.left(90)
#
# for i in range(12):
#     t.penup()
#     t.forward(80)
#     t.pendown()
#     t.forward(15)
#     t.penup()
#     t.forward(15)
#     t.stamp()
#     t.backward(110)
#     t.right(30)
#
# t.hideturtle()
# wn.exitonclick()

# import turtle
# n = int(input("Enter the number of legs: "))
#
# wn = turtle.Screen()
# t = turtle.Turtle()
#
# for i in range(n):
#     t.forward(100)
#     t.backward(100)
#     t.left(360/n)
#
# wn.exitonclick()