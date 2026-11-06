# #Exercise1
# def get_grade(mark):
#     if mark >= 90:
#         return "A"
#     elif mark >= 80:
#         return "B"
#     elif mark >= 70:
#         return "C"
#     elif mark >= 60:
#         return "D"
#     else:
#         return "F"
#
# test_marks = [100, 95, 90, 89.9, 85, 80, 79.998, 75, 70, 69.5, 60, 59.99, 45, 0]
#
# for m in test_marks:
#     print("Mark:", m, "-> Grade:", get_grade(m))


# #Exercise2
# import turtle
# def choose_color(value):
#     if value >= 200:
#         return "red"
#     elif value >= 100:
#         return "yellow"
#     else:
#         return "green"
#
# def draw_bar(t, height):
#     t.fillcolor(choose_color(height))
#     t.begin_fill()
#     t.left(90)
#     t.forward(height)
#     t.write("  " + str(height))
#     t.right(90)
#     t.forward(40)
#     t.right(90)
#     t.forward(height)
#     t.left(90)
#     t.end_fill()
#
# xs = [48, 117, 200, 240, 160, 260, 220]
# maxheight = max(xs)
# numbers = len(xs)
# border = 10
#
# wn = turtle.Screen()
# wn.setworldcoordinates(0 - border, 0 - border, 40 * numbers + border, maxheight + border)
# wn.bgcolor("lightgreen")
#
# tess = turtle.Turtle()
# tess.color("blue")
# tess.pensize(3)
#
# for a in xs:
#     draw_bar(tess, a)
#
# wn.exitonclick()


# #Exercise3
# import turtle
# def choose_color(value):
#     if value >= 200:
#         return "red"
#     elif value >= 100:
#         return "yellow"
#     else:
#         return "green"
#
# def draw_bar(t, height):
#     t.fillcolor(choose_color(height))
#     t.begin_fill()
#     t.left(90)
#     t.forward(height)
#     t.write("  " + str(height))
#     t.right(90)
#     t.forward(40)
#     t.right(90)
#     t.forward(height)
#     t.left(90)
#     t.end_fill()
#
# xs = [48, -50, 117, 200, -120, 240, 160, 260, 220]
# maxheight = max(xs)
# minheight = min(0, min(xs))
# numbers = len(xs)
# border = 10
#
# wn = turtle.Screen()
# wn.setworldcoordinates(0 - border, minheight - border, 40 * numbers + border, maxheight + border)
# wn.bgcolor("lightgreen")
#
# tess = turtle.Turtle()
# tess.color("blue")
# tess.pensize(3)
#
# for a in xs:
#     draw_bar(tess, a)
#
# wn.exitonclick()


#Exercise4
def findHypot(a, b):
    return (a ** 2 + b ** 2) ** 0.5

print("findHypot(3, 4) =", findHypot(3, 4))
print("findHypot(5, 12) =", findHypot(5, 12))
print("findHypot(6, 8) =", findHypot(6, 8))





