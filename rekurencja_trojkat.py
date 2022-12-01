from turtle import *
from math import sqrt

X = 250
Y = 250

#Skok to coś, co musisz umieć na pamięć
def skok(x=100, y=100):
    pu()
    setposition(pos()[0]+x, pos()[1]+y)
    pd()

def kwadrat(bok):
    for i in range(4):
        fd(bok)
        rt(90)

def trojkat(bok):
    rt(30)
    color("black", "red")
    begin_fill()
    for i in range(3):
        fd(bok) ; rt(120)
    end_fill()
    lt(30)

def trojkat_sierpinskiego(bok, n):
    #Trzeba wiedzieć; kiedy przerwać rekurencję. Jak dojdziemy do jedynki, to
    #rysujemy trójkąt i koniec.
    if (n <= 1):
        begin_fill
        trojkat(bok)
        end_fill
        return
    else:
        #Wywołujemy funkcję dla samej siebie dla n mniejszego o 1
        #Tak jak w piosence o zającu, co siedział na kołku
        #i śpiewał piosenkę o samym sobie, co siedzi na kołku...
        trojkat_sierpinskiego(bok/2, n-1)
        skok(bok/2, 0)
        trojkat_sierpinskiego(bok/2, n-1)
        #Gdy nie znamy się na pierwiastkach, idziemy po boku trójkąta:
        skok(-bok/2, 0) ; rt(30) ; fd(bok/2); lt(30)
        
        trojkat_sierpinskiego(bok/2, n-1)

        #rt(30) ; fd(-bok/2) ; lt(30)
        #A jeśli umiemy w pierwiastki od razu można skoczyć w bok o ćwierć
        #i w dół o wysokość trójkąta:
        skok(-bok/4, -sqrt(3)*bok/2/2)





print("Aktualna pozycja: " + str(pos()))
#setposition(pos()[0]-100, pos()[1]-100)

#Można zmieniać wielkość ekranu:
screensize(600,600)

skok(-X, -Y)
lt(90)

#tracer(0)
speed(0)
pensize(1)
trojkat_sierpinskiego(600,3)
#update()
