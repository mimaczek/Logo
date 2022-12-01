# Tutaj pisz swój kod, młody padawanie ;-)
from turtle import *
def kwadrat(bok):
    for i in range(4):
        fd(bok)
        lt(90)
# tracer(0)


for i in range(5):
    print("Dupa nr " + str(i))

def rozetka(bok, ile):
    hideturtle
    color('red', 'blue')
    begin_fill()
    for i in range(ile):
        speed(0)
        
        kwadrat(bok)
        rt(360/ile)
    showturtle
    end_fill()
tracer(0)        
#rozetka(100,3)


update()
up()
setx(150)
sety(0)
down()
tracer(1)
color('green', 'pink')

def kwiatek():
    color('red', 'brown')
    begin_fill()
    speed(0)
    i=0
    while i<36:
        forward(200)
        left(170)
        print(abs(pos()))
        if abs(pos()) < 1:
            break
        i=i+1
    end_fill()
    done()
color('green', 'pink')
#kwiatek()

update()
##setx(-150)
##sety(-100)
down()

tracer(0)
def spirala1():
    color('blue', 'pink')
    for i in range(300):
        fd(i)
        rt(30)
update()
tracer(0)


def spirala2():
    k = 50
    for i in range(60000):
        fd(10)
        rt(k)
        k = k - 10*(1/k)
speed(0)
spirala2()
update()


def spirala3():
    for i in range(600):
        fd(1)
        rt(2 - (1/i))
color('blue', 'pink')
spirala3()
