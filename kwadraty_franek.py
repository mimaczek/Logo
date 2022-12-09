from turtle import *


def kwadraty(ilosc_kwadratow):
    x = -90
    y = 90
    for i in range(1, ilosc_kwadratow):
        penup()
        setpos(x, y)
        pendown()
        for _ in range(4):
            fd(i * 90)
            right(90)
        x -= 45
        y += 45


kwadraty(6)
