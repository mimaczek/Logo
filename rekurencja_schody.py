from turtle import *

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

def schody(bok, n):
    #Jak jest colormode(1), to podajemy kolory od 0..1
    # A jak jest colormode(255), to kolory są 1..255
    colormode(255)

    #kolorki zależne od położenia:
    R = int((X + pos()[0] + 1)/2)
    G = 255 - int((X + pos()[0] + 1)/2)
    B = int((X + pos()[1] + 1)/2)
    #Poniższą linijkę wyłączyłem, bo za wolno działała
    #print("R: " + str(R) + " G: " + str(G) + " B: " + str(B))
    pencolor((R,G,B))
    if (n==1):
        kwadrat(bok)
        return
    else:
        schody(bok/2, n-1)
        #Można podawać komendy po średnikach:
        pu(); fd(bok/2); rt(90); fd(bok/4); lt(90); pd()
        schody(bok/2, n-1)
        pu(); bk(bok/2); rt(90); fd(bok/4); lt(90); pd()
        schody(bok/2, n-1)
        pu(); lt(90); fd(bok/2);rt (90); pd()


print("Aktualna pozycja: " + str(pos()))
#setposition(pos()[0]-100, pos()[1]-100)

#Można zmieniać wielkość ekranu:
screensize(600,600)

skok(-X, -Y)
lt(90)
tracer(0)
#Można eksperymentowac z ilością poziomów(wg mnie do 10, potem już za długo się czeka,
#ale nie przekraczać wysokości 500, bo się wywali błędem (chyba, że sam poprawisz)
schody(500,7)
update()

print("Aktualna pozycja żółwia: " + str(pos()))
print("Wielkość ekranu: " + str(screensize()))
