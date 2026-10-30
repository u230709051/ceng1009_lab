# #exercise1
# def sumTo(n):
#     return (n * (n + 1)) // 2
#
# print(sumTo(10))
# print(sumTo(0))
# print(sumTo(100))


# #exercise2
# import turtle
# def drawStar(t, n, size):
#
#     if n < 3 or n % 2 == 0:
#         print("n must be an odd number greater than or equal to 3!")
#         return
#     angle = 180 - 180 / n
#     for i in range(n):
#         t.forward(size)
#         t.right(angle)
#
# wn = turtle.Screen()
# wn.setup(800, 400)
# wn.bgcolor("lightgreen")
#
# tess = turtle.Turtle()
# tess.color("blue")
# tess.pensize(2)
# tess.speed(0)
#
# size = 100
# gap = 180
# x = -320
# for n in [3, 5, 7, 9]:
#     tess.penup()
#     tess.goto(x, 20)
#     tess.pendown()
#     drawStar(tess, n, size)
#     x += gap
#
# wn.exitonclick()

# #exercise3
# def sumTo(n):
#     total = 0
#     for i in range(1, n + 1):
#         total = total + i
#     return total
#
# print(sumTo(10))
# print(sumTo(0))
# print(sumTo(100))


# #exercise4
# def mySqrt(n):
#     if n == 0:
#         return 0
#     old_guess = n / 2
#     for i in range(20):
#         new_guess = (1 / 2) * (old_guess + (n / old_guess))
#         old_guess = new_guess
#     return new_guess
#
# print(mySqrt(10))
# print(mySqrt(25))
# print(mySqrt(2))


# # #exercise5
# import turtle
# def drawTriangle(t, size):
#     for i in range(3):
#         t.forward(size)
#         t.left(120)
#
# def drawSprite(t, num_legs, leg_length):
#     angle = 360 / num_legs
#     for i in range(num_legs):
#         t.forward(leg_length)
#         t.left(90)
#         t.forward(4)
#         t.right(180)
#         drawTriangle(t, 8)
#         t.right(180)
#         t.backward(4)
#         t.right(90)
#         t.backward(leg_length)
#         t.left(angle)
#
# def fancySquare(t, size, num_legs, leg_length):
#     for i in range(4):
#         t.begin_fill()
#         drawSprite(t, num_legs, leg_length)
#         t.forward(size)
#         t.left(90)
#         t.end_fill()
#
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
#
# alex = turtle.Turtle()
# alex.color("blue")
# alex.pensize(2)
# alex.speed(0)
#
# alex.penup()
# alex.goto(-100, -100)
# alex.pendown()
#
# fancySquare(alex, 200, 8, 30)
#
# wn.exitonclick()


# #exercise6
# def sign(number):
#     if number > 0:
#         return "positive"
#     elif number < 0:
#         return "negative"
#     else:
#         return "zero"
#
# print(sign(5))
# print(sign(-3.2))
# print(sign(0))


#exercise7
import turtle

def drawBar(t, height, label_dist):
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()

    t.penup()
    t.backward(40)
    t.left(90)
    t.forward(height + label_dist)
    t.write("  " + str(height))
    t.backward(height + label_dist)
    t.right(90)
    t.forward(40)
    t.pendown()


def barChart(data):
    max_height = max(data)
    numbars = len(data)
    border = 10

    wn = turtle.Screen()
    wn.setworldcoordinates(0 - border, 0 - border,
                           40 * numbars + border, max_height + border)
    wn.bgcolor("lightgreen")

    tess = turtle.Turtle()
    tess.color("blue")
    tess.fillcolor("red")
    tess.pensize(3)
    tess.speed(0)

    label_dist = (max_height + border) * 0.02

    for a in data:
        drawBar(tess, a, label_dist)

    wn.exitonclick()

xs = [48, 117, 200, 240, 160, 260, 220]
barChart(xs)