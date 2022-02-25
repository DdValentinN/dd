import turtle



def escalier(taille, nombre):
    for i in range (0, nombre):
        t.forward(taille)
        t.left(90)
        t.forward(taille)
        t.right(90)
        taille -= 10
    t.forward(taille)

def carre(taille):
    for i in range (0,4):
        t.forward(taille)
        t.left(90)

def carres(taille_depart, nombre):
    for i in range (0,nombre):
        taille = (i+1)* taille_depart
        carre(taille)


t = turtle.Turtle()
carres(10,10)
#  escalier(60, 5)

turtle.done()
