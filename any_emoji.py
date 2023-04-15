# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 21:34:21 2018

@author: 魅梦
"""
import turtle
import numpy as np
import cv2
im = cv2.imread('20201127155845.png')
height, width, deep = im.shape

if height > 150 or width > 150:
    while height > 150 and width > 150:
        height *= 0.9
        width *= 0.9
    height, width = int(height), int(width)
    im = cv2.resize(im, (width, height))
print(height, width)
# 归一化
im = im/255
turtle.speed(0)
# 设置画笔大小
ps = 3
stepsize = 5
maincolor = np.mean(im.reshape(height*width, deep), axis=0)
print(np.mean(maincolor))


turtle.screensize(width*ps, height*ps)
turtle.setup(width*(ps + 1), height*(ps + 1))
turtle.hideturtle()
turtle.tracer(False)
for he in range(height):
    for we in range(0, width, stepsize):
        if we + stepsize < width:
            end = we + stepsize
        else:
            end = width
        if np.mean(im[he][we: end]) <= 0.9:
            turtle.up()
            turtle.goto(ps*(we - width/2), ps*(height/2 - he))
            turtle.down()
            w = we
            while w < end:
                b, g, r = im[he][w]
                turtle.pencolor(r, g, b)
                turtle.pensize(ps)
                turtle.forward(ps)
                w += 1
turtle.up()
turtle.done()
