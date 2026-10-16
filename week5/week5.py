#import random
#for i in range(10):
#    print(random.random())


#import random
#for i in range(10):
#    print(random.randint(25, 35))


#import math
#a = 3
#b = 4
#hypotenuse = math.hypot(a, b)
#print(f"a={a}, b={b} => hypotenuse={hypotenuse}")


#import math
#def areaOfCircle(r):
#    return math.pi * r ** 2

#print(areaOfCircle(5))
#print(areaOfCircle(10))


#import turtle
#def draw_star():
#    t = turtle.Turtle()
#    t.speed(5)
#    for i in range(5):
#        t.forward(100)
#        t.right(144)
#    turtle.done()

#draw_star()


#import turtle
#def drawSquare(t, size):
#    for i in range(4):
#        t.forward(size)
#        t.left(90)

#t = turtle.Turtle()
#t.speed(5)

#for i in range(5):
#    drawSquare(t, 20)
#    t.penup()
#    t.forward(30)
#    t.pendown()

#turtle.done()


import turtle
def drawSquare(t, size):
    for i in range(4):
        t.forward(size)
        t.left(90)

t = turtle.Turtle()
t.speed(5)

num_squares = 6
innermost = 20

for i in range(num_squares):
size = innermost + i * 20
    t.penup()
    offset = (size - innermost) / 2
    t.goto(-offset, -offset)
    t.pendown()
    drawSquare(t, size)

turtle.done()
