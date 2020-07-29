# coding: utf8
import couleur
import pygame
import labyrinthe
import grille
import jeu

HAUT = 0 
DROITE = 1
BAS = 2
GAUCHE = 3

def init(x,y,direc):
    '''La fonction initialise le pacman a sa position selon la direction choisie precedemment.
    Arguments :
    entree : x(int),y(int),direc(int)
    sortie : dict -- '''
    att = {}
    att["vivant"] = True
    att["pos_l"] = x
    att["pos_c"] = y
    att["direc"] = direc
    att["depl_l"] = 0
    att["depl_c"] = 0

    return att

def dessine(surface,att):
    '''La fonction dessine pacman dans le jeu.
    Arguments :
    entree : surface(dict), att(dict)
    sortie : / '''
    pygame.draw.circle(surface,couleur.JAUNE,(att["pos_l"]*30+15,att["pos_c"]*30+15),10)
    
    if att["direc"] == 0:
        pygame.draw.polygon(surface,couleur.NOIR,((att["pos_l"]*30+15,att["pos_c"]*30+15),(att["pos_l"]*30+5,att["pos_c"]*30),(att["pos_l"]*30+25,att["pos_c"]*30)))
        pygame.draw.circle(surface,couleur.NOIR,(att["pos_l"]*30+10,att["pos_c"]*30+15),2)
        
    if att["direc"] == 1:
        pygame.draw.polygon(surface,couleur.NOIR,((att["pos_l"]*30+15,att["pos_c"]*30+15),(att["pos_l"]*30+25,att["pos_c"]*30+20),(att["pos_l"]*30+25,att["pos_c"]*30+10)))
        pygame.draw.circle(surface,couleur.NOIR,(att["pos_l"]*30+15,att["pos_c"]*30+10),2)
        
    if att["direc"] == 2:
        pygame.draw.polygon(surface,couleur.NOIR,((att["pos_l"]*30+15,att["pos_c"]*30+15),(att["pos_l"]*30+5,att["pos_c"]*30+27),(att["pos_l"]*30+25,att["pos_c"]*30+27)))
        pygame.draw.circle(surface,couleur.NOIR,(att["pos_l"]*30+20,att["pos_c"]*30+15),2)
        
    if att["direc"] == 3:
        pygame.draw.polygon(surface,couleur.NOIR,((att["pos_l"]*30+15,att["pos_c"]*30+15),(att["pos_l"]*30,att["pos_c"]*30+20),(att["pos_l"]*30,att["pos_c"]*30+10)))
        pygame.draw.circle(surface,couleur.NOIR,(att["pos_l"]*30+15,att["pos_c"]*30+10),2)
        
def depl_haut(att):
    '''La fonction defini le deplacement vers le haut.
    Arguments :
    entree : att(dict)
    sortie : / '''
    
    att["depl_l"] = -1
    att["depl_c"] = 0
    att["direc"] = 0
    
def depl_bas(att):  
    '''La fonction defini le deplacement vers le bas.
    Arguments :
    entree : att(dict)
    sortie : / '''
    
    att["depl_l"] = 1
    att["depl_c"] = 0
    att["direc"] = 2

def depl_droite(att):
    '''La fonction defini le deplacement vers la droite.
    Arguments :
    entree : att(dict)
    sortie : / '''
    
    att["depl_l"] = 0
    att["depl_c"] = 1
    att["direc"] = 1

def depl_gauche(att):
    '''La fonction defini le deplacement vers la gauche.
    Arguments :
    entree : att(dict)
    sortie : / '''

    att["depl_l"] = 0
    att["depl_c"] = -1
    att["direc"] = 3

def update(att):
    '''La fonction met a jour les deplacements de pacman.
    Arguments :
    entree : att(dict), tableau(liste)
    sortie : / '''
    
    x = att["pacman"]["pos_c"]
    y = att["pacman"]["pos_l"]

    for i in range(len(att["fantome"])):
        
        if att["pacman"]["pos_l"] == att["fantome"][i]["pos_c"] and att["pacman"]["pos_c"] == att["fantome"][i]["pos_l"] :
            jeu.fin('game_over')
            att["pacman"]["vivant"] = False
    
    if att["pacman"]["depl_l"] == -1 and att["pacman"]["vivant"] == True :
        if att["labyrinthe"][x-1][y] != "#":
            pygame.draw.rect(att["surface"],couleur.NOIR,(att["pacman"]["pos_l"]*30,att["pacman"]["pos_c"]*30,30,30))
            att["pacman"]["pos_c"] -= 1
            
    elif att["pacman"]["depl_l"] == 1 and att["pacman"]["vivant"] == True :
        if att["labyrinthe"][x+1][y] != "#":
            pygame.draw.rect(att["surface"],couleur.NOIR,(att["pacman"]["pos_l"]*30,att["pacman"]["pos_c"]*30,30,30))
            att["pacman"]["pos_c"] += 1
      
        
    elif att["pacman"]["depl_c"] == -1 and att["pacman"]["vivant"] == True :
        if att["labyrinthe"][x][y-1] != "#":
            pygame.draw.rect(att["surface"],couleur.NOIR,(att["pacman"]["pos_l"]*30,att["pacman"]["pos_c"]*30,30,30))
            att["pacman"]["pos_l"] -= 1
        
        
    elif att["pacman"]["depl_c"] == 1 and att["pacman"]["vivant"] == True :
        if att["labyrinthe"][x][y+1] != "#":
            pygame.draw.rect(att["surface"],couleur.NOIR,(att["pacman"]["pos_l"]*30,att["pacman"]["pos_c"]*30,30,30))
            att["pacman"]["pos_l"] += 1
            
    att["pacman"]["depl_l"] = 0
    att["pacman"]["depl_c"] = 0
    
    labyrinthe.mange_gomme(att["labyrinthe"],att)
