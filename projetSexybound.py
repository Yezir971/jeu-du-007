# from keras.models import Sequential
# from keras.layers import Dense, Input
# import numpy as np
from function.actions import *
import random 


# initialisation du nombre de balle de chaque joueurs 
nb_bal_j1 = 0
nb_bal_j2 = 0
# initialisation du nombre de tour 
tour = 0
# initialisation du nombre de vie de chaque joueurs 
nb_vie_j1 = 5
nb_vie_j2 = 5
# initialisation de la liste d'action de chaque jouerurs 
liste_action_j1 = []
liste_action_j2 = []

# Fonction qui sert à initialiser le dictionnaire des deux joueurs 
initialisation_joueurs(liste_action_j1, liste_action_j2,nb_vie_j1,nb_vie_j2  )
# print(liste_action_j1)
choix_rejouer = str(input('Bienvenu au jeu du 007, voulez vous jouer ? O/N\n'))
choix_rejouer = fonction_jouer(choix_rejouer)

# (liste_action_j1[tour-1]["nb_vie_j1"] >0 or liste_action_j2[tour-1]["nb_vie_j2"] ) and 
while ( choix_rejouer ) :
    # print('on joue !')
    if (liste_action_j1[tour]["nb_bal_j1"] > 0 ):
        actionJ = str(input(f"Tour: {tour}, choisi entre\nT -> tirer\nR -> Recharger\nB -> Bouclier\n")).upper()
    else :
        actionJ = str(input(f"Tour: {tour}, choisi entre\nR -> Recharger\nB -> Bouclier\n")).upper()


    # Partie IA 

    if (liste_action_j2[tour]["nb_bal_j2"] > 0 ):
        actionIA = random.randint(1,3)
    else :
        actionIA = random.randint(2,3)
    match actionIA :
        case 1 :
            actionIA = "T"
        case 2 :
            actionIA = "R"
        case 3 : 
            actionIA = "B"
        case _:
            print('Error A-IA-1: Entrer random des actions de l\'IA mauvaise !')

    tour+=1 
    actions_joueurs(actionJ, liste_action_j1, tour, liste_action_j1[tour-1]["nb_bal_j1"], liste_action_j1[tour-1]["nb_vie_j1"])
    actions_ia(actionIA, liste_action_j2, tour, liste_action_j2[tour-1]["nb_bal_j2"], liste_action_j2[tour-1]["nb_vie_j2"])
    compareMouvement(liste_action_j1,liste_action_j2,tour)
    print(f'compare Joueurs: {liste_action_j1[tour]}')
    print(f'compare IA: {liste_action_j2[tour]}')
    if(liste_action_j1[tour]["nb_vie_j1"] == 0 or liste_action_j2[tour]["nb_vie_j2"] == 0 ):
        choix_rejouer = False








