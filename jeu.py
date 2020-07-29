# coding: utf8
import pygame
import labyrinthe
import couleur
import grille
import pacman
import fantomes

def init():
    '''La fonction est responsable de l'initialisation du jeu et donc de pygame.
    Arguments :
    entree : /
    sortie :  dictionnaire des attributs  '''
    
    pygame.init()
    
    musique()

    horloge = pygame.time.Clock()
    fenetre = pygame.display.set_mode((1080,720))
    pygame.display.set_caption("Bouffe Qui Peut")

    att = {}
    att["Largeur"] = 1080
    att["Hauteut"] = 720
    att["surface"] = fenetre
    att["horloge"] = horloge
    att["continuer"] = True
    att["pacman"] = pacman.init(1,1,1)
    att["labyrinthe"] = labyrinthe.init(grille.GRILLE)
    att["fantome"] = [(fantomes.init("Pouchy",grille.FANTOMES[0][0],grille.FANTOMES[0][1],couleur.BLEU)),(fantomes.init("Baggy",grille.FANTOMES[1][0],grille.FANTOMES[1][1],couleur.JAUNE)),(fantomes.init("Jacky",grille.FANTOMES[2][0],grille.FANTOMES[2][1],couleur.ROSE)),(fantomes.init("Jean",grille.FANTOMES[3][0],grille.FANTOMES[3][1],couleur.ROUGE))]
    
    return att

def quitte():
    '''La fonction definie l'evenement 'quitter le jeu'.
    Arguments :
    entree: /
    sortie : / '''
    pygame.quit()

def boucle(att):
    '''La fonction est responsable de l'execution du jeu.
    Arguments :
    entree : le dictionnaire des attributs du jeu
    sortie : / '''
    
    while att["continuer"]:
        
        traite_evenements(att)   
        dessine(att)
        update(att)
        labyrinthe.gagne(att)
        att["horloge"].tick(40)
        
def traite_evenements(att):
    ''' La fonction estresponsable du traitement des evenements.
    Arguments :
    entree : le dictionnaire des attributs
    sortie : / '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            att["continuer"] = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                att["continuer"] = False
            if event.key == pygame.K_UP:
                pacman.depl_haut(att["pacman"])
            if event.key == pygame.K_DOWN:
                pacman.depl_bas(att["pacman"])
            if event.key == pygame.K_RIGHT:
                pacman.depl_droite(att["pacman"])
            if event.key == pygame.K_LEFT:
                pacman.depl_gauche(att["pacman"])
                
def dessine(surface):
    '''La fonction dessine le labyrinthe.
    Arguments :
    entree : surface
    sortie : / '''
    surface["surface"].fill(couleur.NOIR)
    labyrinthe.dessine_labyrinthe(surface["surface"],surface["labyrinthe"])
    fantomes.dessine(surface["fantome"],surface["surface"])
    pacman.dessine(surface["surface"],surface["pacman"])
    

def update(att):
    '''La fonction met a jour le labyrinthe :
    Arguments :
    entree : dict -- att
    sortie : / '''
    pacman.update(att)
    fantomes.update(att["fantome"][0],att["labyrinthe"])
    fantomes.update(att["fantome"][1],att["labyrinthe"])
    fantomes.update(att["fantome"][2],att["labyrinthe"])
    fantomes.update(att["fantome"][3],att["labyrinthe"])
    pygame.display.update()
    if att["pacman"]["vivant"] == False :
        att["continuer"] = False
        
def musique():
    '''La fonction lance la musique du jeu
    Arguments :
    entrre : /
    sortie : / '''
    pygame.mixer.music.load("sonpac2.wav")
    musique = pygame.mixer.music.play()
    musique
    
def fin(stat):
    '''La fonction afficher une image game_over ou gagner ! en fonction de ce qu\'a fait le joueur.
    Arguments :
    entree : stats(str)
    sortie : / '''
    fenetre = pygame.display.set_mode((1080,720)) 
    continuer = True
    while continuer : 
        if stat == 'game_over' :
            image = pygame.image.load('perdu.jpg').convert_alpha()
            fenetre.blit(image, (0, 100))
            pygame.display.flip()
            pygame.time.wait(3000)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        continuer = False
                    
        if stat == 'gagner' :
            image = pygame.image.load('gagner.jpg').convert_alpha()
            fenetre.blit(image, (0, 150))
            pygame.display.flip()
            pygame.time.wait(5000)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        continuer = False
        