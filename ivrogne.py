#-*- coding:utf-8 -*-
from random import randrange
from turtle import *
from colors import COLORS





class Ivrogne(object):
    #Usine à ivrognes
    
    def __init__(self,x,y,color):
        #Constructeur
        self.pos = [x,y] #NB: il est possible que les ivrognes sortent de l'écran 
        self.color = color
    
    def Mouvement(self):
        #Methode qui modifie et renvoie la position de l'ivrogne
        tmp = getDeplacement()
        for i in range(0,2):
            self.pos[i] += tmp[i]
        return self.pos

def getDeplacement():
    #Génère un déplacement aléatoire
    depl = [0,0]
    tmp = randrange(8)
    if(tmp in (0,1,2)):
        depl[0] += 1
    elif(tmp in (3,4,5)):
        depl[0] -= 1
    if(tmp in (1,3,7)):
        depl[1] += 1
    elif(tmp in (2,4,6)):
        depl[1] -= 1
    return depl
    
def turtleMovementIvrogne(args):
    #Gère les ivrognes et la simulation
    def movIvrogne(ivrogne):
        #Fait bouger l'ivrogne passé en argument
        up()
        hideturtle()
        color(ivrogne.color)
        goto(ivrogne.pos[0]*10,ivrogne.pos[1]*10)
        down()
        showturtle()
        ivrogne.Mouvement()
        goto(ivrogne.pos[0]*10,ivrogne.pos[1]*10)

    for iv in args:
        movIvrogne(iv)
  

nbIvrogne = int(input("Combien d'ivrognes?")) #self-explanatory
reset() #initialise la simulation
speed(0) #règle la vitesse au maximum


listeIvrognes = [Ivrogne(randrange(-50,50),randrange(-50,50),COLORS[randrange(0,478)]) for i in range(nbIvrogne)]
#Paramètres à regler en fonction de la taille de l'écran et de la version de Python

while(True):
    turtleMovementIvrogne(listeIvrognes)
    
