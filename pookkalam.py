from turtle import *

def drawFirstType(f, r):
    home()
    forward(f)
    right(r)
    forward(f)
    drawFlower(30, 45, 'purple')


def drawSecondType(forward1, forward2, ang):
    home()
    right(ang)
    forward(forward1)
    drawFlower(15, 45, 'red')
    home()
    right(ang)
    forward(forward2)
    drawFlower(15, 45, 'blue')


def drawFlower(rad, ang, col):
    fillcolor(col)
    pendown()
    begin_fill()
    for i in range(360 / ang):
        circle(rad)
        left(ang)
    end_fill()
    penup()


def main():
    penup()
    home()
    goto(0, -180)
    pendown()
    fillcolor('green')
    begin_fill()
    circle(180)
    end_fill()
    penup()

    home()
    drawFlower(90, 20, 'orange')
    home()
    drawFlower(30, 45, 'yellow')

    drawFirstType(85, -90)
    drawFirstType(85, 90)
    drawFirstType(-85, -90)
    drawFirstType(-85, 90)

    drawSecondType(85, 148, 0)
    drawSecondType(85, 148, 90)
    drawSecondType(-85, -148, 0)
    drawSecondType(-85, -148, 90)

    mainloop()


if __name__ == '__main__':
    main()
