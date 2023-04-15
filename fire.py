#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Date: 2021/6/19 16:21:15
@Software: PyCharm
@Author: lazyn
"""

import time
import random
import turtle
from turtle import *


def draw_firework(count, dis, ang):
    for c in range(count):
        forward(dis)
        left(ang)


def draw(lis):
    pensize(1)
    for t in range(10):
        for li in lis:
            x, y, col, dis, ang, add, count = li
            penup(), goto(x - t * add / 2, y), pendown()
            color('black', col)
            begin_fill()
            setheading(0)
            draw_firework(count, t * add + 30, ang)
            end_fill()
        update()
        time.sleep(0.015)
        clear()

    pensize(2)
    for t in range(10):
        for li in lis:
            x, y, col, dis, ang, add, count = li
            count = int(count / 4)
            penup(), goto(x - add * 5 + 10, y), pendown()
            setheading(-90)
            stara = dis / 2 - 10
            penup(), left(90), backward(2 * t), right(90)
            for i in range(count):
                penup()
                pencolor(col)
                circle(stara + t * 2, 360 / count - 1)
                pendown()
                circle(stara + t * 2, 1)
        update()
        time.sleep(0.03)
        clear()


def main(cols):
    while True:
        fires = random.randint(10, 15)
        need_list = []
        for f in range(fires):
            startx, starty = random.randint(-350, 350), random.randint(-100, 250)
            ccol = random.choice(cols)
            dist = random.randint(50, 80)
            if dist <= 60:
                angle = 171
            else:
                angle = random.choice([174, 175, 176])
            add = (dist - 30) / 10
            count = int(360 / (180 - angle))
            need_list.append([startx, starty, ccol, dist, angle, add, count])
        draw(need_list)
        clear()
    done()


if __name__ == '__main__':
    setup(810, 605)
    screensize(800, 600, 'black')
    hideturtle()
    colors = ['red', 'blue', 'yellow', 'white',
              'green', 'orange', 'purple', 'seagreen',
              'indigo', 'cornflowerblue']
    tracer(False)
    main(colors)

