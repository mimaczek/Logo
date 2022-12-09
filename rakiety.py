from turtle import *
import random

ht()


pershing = Turtle()
cruise   = Turtle()
patriot  = Turtle()
katiusza = Turtle()

wszystkie = [pershing, cruise, patriot, katiusza]

def start():
    clear()
    for r in wszystkie:
        r.pu()
    pershing.setposition(-100,-100)
    cruise.setposition(-100,100)
    patriot.setposition(100,100)
    katiusza.setposition(100,-100)
    for r in wszystkie:
        r.pd()
        r.speed(0)
        r.st()

def ruch(v):
    for _ in range(200):
        for i in range(-1,3):
            wszystkie[i].towards(wszystkie[i+1])
            wszystkie[i].seth(wszystkie[i].towards(wszystkie[i+1]))
            wszystkie[i].fd(v)

def bum():
    for _ in range(3):
        for r in wszystkie:
            r.color(random.choice(['pink','brown','white','red','blue','green','yellow']),
                    random.choice(['pink','brown','white','red','blue','green','yellow']))
            r.begin_fill()
            r.circle(random.choice([5,10,15,20]))
            r.end_fill()
    
start()
ruch(1)
bum()

