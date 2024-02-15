import random
import turtle
from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("chocolate")
tim.speed(6)

# colors = ["navy", "orange red", "Red", "blue", "green", "black", "orange", "cyan", "chocolate", "pink", "aquamarine4",
#           "dark red", "indigo", "gold", "chartreuse", "hot pink", "brown", "sienna", "pale goldenrod", "teal",
#           "steel blue"]


turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)  # making tuple of the r g b variables
    return color_tuple


tim.forward(100)
tim.right(90)
tim.forward(100)
tim.right(90)
tim.forward(100)
tim.right(90)
tim.forward(100)
tim.right(135)
tim.forward(141.4)
tim.left(135)
tim.forward(100)
tim.left(135)
tim.forward(141.4)
tim.left(135)
tim.forward(50)
tim.left(90)
tim.forward(100)
tim.right(90)
tim.forward(50)
tim.right(90)
tim.forward(50)
tim.right(90)
tim.forward(100)
tim.left(90)  # change it to right make 2nd square on top of this one
tim.forward(50)


def turtle_square():
    for _ in range(4):  # Range 0 to 4
        tim.forward(100)
        tim.right(90)


def turtle_diagonal():
    tim.right(45)
    tim.forward(141.4)


def turtle_center():
    tim.right(135)
    tim.forward(50)
    tim.right(90)
    tim.forward(100)


turtle_square()
turtle_diagonal()
tim.right(135)
tim.forward(100)
tim.right(90)
turtle_diagonal()
turtle_center()
tim.right(90)
tim.forward(50)
tim.left(45)
turtle_center()
tim.left(90)
tim.forward(50)

tim.clear()
tim.left(180)


def turtle_dashed_line():
    for _ in range(15):
        tim.pendown()
        tim.forward(10)
        tim.penup()
        tim.forward(10)


turtle_dashed_line()

tim.pendown()
tim.forward(210)
tim.right(90)
tim.clear()


def draw_shape(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        tim.forward(130)
        tim.right(angle)


for shape_side in range(3, 16):
    tim.color(random_color())
    draw_shape(shape_side)

tim.reset()


# RANDOM WALK

directions = [0, 90, 180, 270]  # 0 deg for EAST, 90 NORTH, 180 WEST, 270 SOUTH
tim.pensize(15)

for _ in range(100):
    tim.speed(0)
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))

tim.reset()
tim.pensize(1)
tim.hideturtle()


# SPIROGRAPH

s = Screen()
s.bgcolor("black")  # To make bg color black
def spirograph(size_of_gap):

    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.left(size_of_gap)
        tim.speed(0)
spirograph(5)


tim.hideturtle()






screen = Screen()
screen.exitonclick()














# from turtle import *
# import turtle as tur
# import random
# import math
#
#
# tur.setup(900,500, startx= 300, starty= 300)
# tur.title("Python Guides")
# a1 = tur.Turtle()
# b1 = tur.Turtle()
# c1 = tur.Turtle()
# d1 = tur.Turtle()
# e1 = tur.Turtle()
#
# a1.color('medium violet red')
# b1.color('cornflower blue')
# c1.color('maroon')
# d1.color('dark green')
# e1.color('light salmon')
#
# turtlist = []
# turtlist.append(a1)
# turtlist.append(b1)
# turtlist.append(c1)
# turtlist.append(d1)
# turtlist.append(e1)
#
# tur.speed(0)
# tur.tracer(0)
# tur.hideturtle()
# tur.pensize(600)
# sum = 0
# count = 0
# for j in range(100):
#     for i in range(10000):
#         for turt in turtlist:
#             turt.seth(random.randrange(0,360,90))
#             turt.fd(10)
#         tur.update()
#     for turt in turtlist:
#         sum += math.sqrt(turt.xcor()*turt.xcor() + turt.ycor()*turt.ycor())/10*2*math.sqrt(turt.xcor()*turt.xcor() + turt.ycor()*turt.ycor())/10*2/100
#         count += 1
#     for turt in turtlist:
#         turt.clear()
#         turt.up()
#         turt.goto(0,0)
#         turt.down()
#     print(sum/count)
