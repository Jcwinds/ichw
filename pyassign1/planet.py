#Assignment1, planet
#韦宗乐, 1700011705
#2017.12.19

"""Module for drawing planet orbitals

This module draw the first 6 planets, their orbitals, and the sun in solar
system. The parameters is not in real ratios """

import turtle
import math


def draw_oval(t, a, e, d):
    """Returns: None.

    This function receive 4 parameters t(turtle), a(length of long
    axis), e(eccentricity) and d(direction related to the center) and
    let a turtle t draw a certain oval.

    Parameter t: a turtle, representing a planet.
    Precondition: t is a turtle.

    Parameter a: length of long axis of the oval
    Precondition: a is a float or an int.

    Parameter e: eccentricity of the oval
    Precondition: e is a float or an int, 0 =< e < 1.

    Parameter d: direction, which decides whether the left or right
    focal spot is located in the center of the screen.
    Precondition: d = 1 or -1.
    """

    b = a * math.sqrt(1 - e ** 2)
    c = a * e
    dtheta = 2 * math.pi / 1000

    t.pu()
    t.fd(a + d * 2 * c)
    t.pd()
    
    for i in range(1000):
        theta = dtheta * (i + 1)
        x = a * math.cos(theta) + d * 2 * c
        y = b * math.sin(theta)

        t.goto(x, y)

def main():
    #set screen and asters
    turtle.screensize(1000, 1000, "white")

    Sun_t = turtle.Turtle(shape = 'circle')
    Mercury_t = turtle.Turtle(shape = 'circle')
    Venus_t = turtle.Turtle(shape = 'circle')
    Earth_t = turtle.Turtle(shape = 'circle')
    Mars_t = turtle.Turtle(shape = 'circle')
    Jupiter_t = turtle.Turtle(shape = 'circle')
    Saturn_t = turtle.Turtle(shape = 'circle')

    #create a color list
    Sun_t.fillcolor('yellow')
    colors = ['blue', 'green', 'black', 'red', 'orange', 'cyan']
    #set parameters of planets
    Mercury = (Mercury_t, 30, 0.206, 1)
    Venus = (Venus_t, 60, 0.007, -1)
    Earth = (Earth_t, 100, 0.017, 1)
    Mars = (Mars_t, 150, 0.093, 1)
    Jupiter = (Jupiter_t, 300, 0.048, -1)
    Saturn = (Saturn_t, 500, 0.054, 1)
    
    Planet_arg = [Mercury, Venus, Earth, Mars, Jupiter, Saturn]

    #set colors of planets
    for i in range(6):
        Planet_arg[i][0].pu()
        Planet_arg[i][0].fillcolor(colors[i])
        Planet_arg[i][0].pencolor(colors[i])


    #draw the orbitals, step by step
    for i in Planet_arg:
        draw_oval(i[0], i[1], i[2], i[3])


if __name__ == '__main__':
    main()
