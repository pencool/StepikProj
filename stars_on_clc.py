from turtle import *
from random import randint as r
from random import choice as c

Screen().setup(600, 600)
Screen().bgcolor('black')
ht()
speed(0)


def star(size):
    colors = ['red', 'green', 'aqua', 'blue', 'purple', 'orange', 'violet']
    color(c(colors))
    begin_fill()
    lt(r(0, 360))
    for i in range(5):
        fd(size)
        lt(144)
    end_fill()


Screen().onclick(star(r(10, 60)))
Screen().onclick()
