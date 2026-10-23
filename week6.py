import turtle

# ── SETUP ────────────────────────────────────────
wn = turtle.Screen()
wn.bgcolor("lightgreen")

t = turtle.Turtle()
t.color("blue")
t.speed(0)

# ── FUNCTIONS ────────────────────────────────────

def drawPoly(someturtle, somesides, somesize):
    angle = 360 / somesides
    for i in range(somesides):
        someturtle.forward(somesize)
        someturtle.right(angle)

def drawEquitriangle(someturtle, somesize):
    drawPoly(someturtle, 3, somesize)

def drawStar(someturtle, size):
    for i in range(5):
        someturtle.forward(size)
        someturtle.right(144)

def drawSprite(someturtle, numLegs, legLength):
    angle = 360 / numLegs
    for i in range(numLegs):
        someturtle.forward(legLength)
        someturtle.backward(legLength)
        someturtle.right(angle)


# ── EXERCISE 1 ───────────────────────────────────
# t.color("hotpink")
# drawPoly(t, 8, 50)
# wn.exitonclick()

# # ── EXERCISE 2 ───────────────────────────────────
# t.color("blue")
# t.penup()
# t.goto(0,0)
# t.pendown()
# for i in range(36):
#     drawPoly(t, 4, 100)
#     t.right(20)
# wn.exitonclick()
#
# ── EXERCISE 3 ───────────────────────────────────
# t.penup()
# t.goto(-300, 150)
# t.pendown()
# length = 5
# for i in range(80):
#     t.forward(length)
#     t.right(90)
#     length += 3
#
# t2 = turtle.Turtle()
# t2.color("blue")
# t2.speed(0)
# t2.penup()
# t2.goto(100, 150)
# t2.pendown()
# length = 5
# for i in range(80):
#     t2.forward(length)
#     t2.right(91)
#     length += 3
# wn.exitonclick()
#
# # ── EXERCISE 4 ───────────────────────────────────
# drawEquitriangle(t, 100)
# wn.exitonclick()

# ── EXERCISE 5 ───────────────────────────────────
# t.color("hotpink")
# t.penup()
# t.goto(-300, 100)
# t.pendown()
# for i in range(5):
#     drawStar(t, 80)
#     t.penup()
#     t.forward(350)
#     t.right(144)
#     t.pendown()
# wn.exitonclick()
#
# # ── EXERCISE 6 ───────────────────────────────────
t.color("blue")
t.penup()
t.goto(0, 0)
t.pendown()
drawSprite(t, 15, 120)

wn.mainloop()




