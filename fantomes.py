import pygame
import couleur
import labyrinthe
import random

def init(nom,x,y,couleur):
    '''La fonction initialise les fantomes a leurs positions et reçoit les attributs de deplacement d'arret et de vitesse.
    Arguments :
    entree : nom(str), x(int),y(int),couleur(str)
    sortie : dict -- '''
    att = {}

    att["nom"] = nom
    att["couleur"] = couleur
    att["pos_l"] = y
    att["pos_c"] = x
    att["depl_c"] = 0
    att["depl_l"] = 0
    att["arret"] = 0
    att["vit"] = 5
    
    return att

def dessine(att,surface):
    '''La fonction dessine les fantomes.
    Arguments:
    entree : att(dict) , surface(dict)
    sortie : '''
    for i in range(len(att)):  
        pygame.draw.circle(surface,att[i]["couleur"],(att[i]["pos_c"]*30+15,+att[i]["pos_l"]*30+15),10)
        pygame.draw.circle(surface,couleur.BLANC,(att[i]["pos_c"]*30+10,+att[i]["pos_l"]*30+15),3)
        pygame.draw.circle(surface,couleur.BLANC,(att[i]["pos_c"]*30+20,+att[i]["pos_l"]*30+15),3)
        pygame.draw.circle(surface,couleur.NOIR,(att[i]["pos_c"]*30+10,+att[i]["pos_l"]*30+15),2)
        pygame.draw.circle(surface,couleur.NOIR,(att[i]["pos_c"]*30+20,+att[i]["pos_l"]*30+15),2)
        
    
def depl_possible(att,tableau,lc):
    '''La fonction verifie si un deplacement est possible. (Si il y a un mur ou non).
    Arguments :
    entree : att(dict) , tableau(dict) , lc(int)
    sortie : booleen'''
    #print(att["pos_l"],att["pos_c"])
    #print(l,c)
    l,c = lc
    return not(labyrinthe.est_mur(tableau,att["pos_l"] + l,att["pos_c"] + c))

def choix_deplacement(att,labyrinthe):
    '''La fonction choisi quel deplacements les fantomes vont effectues.
    Arguments:
    entree : att(dict) , labyrinthe(dict)
    sortie : '''
    c = random.randint(-1,1)
    l = random.randint(-1,1)
    while not(depl_possible(att,labyrinthe,(l,c))):
        c = random.randint(-1,1)
        l = random.randint(-1,1)     
    att["depl_c"] = 0
    att["depl_l"] = 0

    att["depl_c"] += c
    att["depl_l"] += l

def update(att,labyrinthe):
    '''La fonction met a jour les fantomes.
    Arguments:
    entree : att(dict) , labyrinthe(dict)
    sortie : '''
    if att["vit"] == att["arret"]:
        choix_deplacement(att,labyrinthe)
        att["pos_l"] += att["depl_l"]
        att["pos_c"] += att["depl_c"]
        att["arret"] = 0
    else :
        att["arret"] += 1
