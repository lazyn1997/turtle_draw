# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 21:34:21 2018

@author: 魅梦
"""

from turtle import *

def drawcircle(x, y, r, angle, size):
    pensize(size)
    up()
    goto(x, y)
    down()
    begin_fill()
    circle(r, angle)
    color("black", "white")
    end_fill()
def draweye(x, y, startangle, changeangle, step, stepplus, times):
    pensize(3)
    up()
    goto(x, y)
    down()
    setheading(startangle)
    a = step
    for i in range(times):
        a = a + stepplus
        left(changeangle)
        forward(a)
#Turtle().screen.delay(0)
hideturtle()
drawcircle(0, 0, 45, 360, 2)
drawcircle(20, -1, 15, 360, 2)
drawcircle(-5, -1, 15, 360, 2)
draweye(-15, 70, -30, 3, 0.1, 0.03, 25)
draweye(-20, 58, -30, 2, 0.1, 0.03, 35)
draweye(22, 75, -75, 3, 0.1, 0.02, 30)
draweye(17, 65, -75, 2, 0.1, 0.02, 40)
setheading(90)
drawcircle(0, 55, -5, -180, 3)
setheading(90)
drawcircle(10, 55, -5, -180, 3)
begin_fill()
draweye(4, 50, -100, 0.8, 0.05, 0.01, 55)
draweye(16, 50, -80, -0.8, 0.05, 0.01, 55)
color("black", "red")
end_fill()
setheading(90)
drawcircle(0, 55, -5, -180, 3)
setheading(90)
drawcircle(10, 55, -5, -180, 3)
pensize(8)
setheading(5)
up()
goto(-25, 50)
down()
begin_fill()
color("pink", "pink")
forward(15)
end_fill()
up()
goto(30, 50)
down()
begin_fill()
color("pink", "pink")
forward(10)
end_fill()
done()
