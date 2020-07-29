# coding: utf8
import pygame
import grille
import couleur
import jeu

def init(grille):
    ''' La fonction charge le labyrinthe dans un tableau à deux dimensions.
    Arguments :
    entree : grille(str)
    sortie : liste '''
    tableau = []
    liste = []
    for i in grille:
        if i != "\n":
            liste += i
        else:
            tableau.append(liste)
            liste = []
    return tableau  
    
def est_mur(tableau,lin,col):
    ''' La fonction verifie si le caractere à la position (lin,col) est un mur.
    Arguments :
    entree : tableau(liste) , lin(int), col(int)
    sortie : True ou false (boolleen) '''
    return tableau[lin][col] == "#"
        

def est_gomme(tableau,lin,col):
    ''' La fonction verifie si le caractere à la position (lin,col) est un mur.
    Arguments :
    entree : tableau(liste) , lin(int), col(int)
    sortie : True ou false (boolleen) '''
    return tableau[lin][col] == "."
        

def dessine_mur(surface,lin,col):
    '''La fonction dessine le mur (une partie du mur) aux coordonnees (lin,col)
    Arguments :
    entree : surface , lin(int), col(int)
    sortie : / '''
    x = grille.T_CASE * col
    y = grille.T_CASE * lin
    pygame.draw.rect(surface,couleur.MARRON,(x,y,grille.T_CASE,grille.T_CASE))

def dessine_gomme(surface,lin,col):
    '''La fonction dessine les gommes aux coordonnees (lin,col)
    Arguments :
    entree : surface , lin(int), col(int)
    sortie : / '''
    x = grille.T_CASE * col
    y = grille.T_CASE * lin
    pygame.draw.circle(surface,couleur.JAUNE,(x+grille.T_CASE//2,y+grille.T_CASE//2),grille.T_CASE//6)

def dessine_labyrinthe(surface,tableau):
    '''La fonction dessine le labyrinthe
    Arguments :
    entree : surface , tableau(liste)
    sortie : / '''
    for i in range(len(tableau)):
        for j in range(len(tableau[i])):
            if est_mur(tableau,i,j) == True :
                dessine_mur(surface,i,j)
            elif est_gomme(tableau,i,j) == True:
                dessine_gomme(surface,i,j)
  
        
def mange_gomme(tableau,att):
    '''La fonction verifie si le caractere a la position de pacman si il y a une gomme.
    Arguments :
    entree : tableau(liste), att(dict)
    sortie : / '''
    if est_gomme(tableau,att["pacman"]["pos_c"],att["pacman"]["pos_l"]):
        tableau[att["pacman"]["pos_c"]][att["pacman"]["pos_l"]] = " "
        
        


def gagne(att):
    '''La fonction ferme le jeu si la partie est terminee (ici gagnee).
    Arguments :
    entree : att(dict)
    sortie : / '''
    g = 0
    for i in range(len(att["labyrinthe"])):
        for j in range(len(att["labyrinthe"][i])):
            if est_gomme(att["labyrinthe"],i,j):
                g += 1
    if g == 0 :
        jeu.fin("gagner")
        att["continuer"] = False





    
