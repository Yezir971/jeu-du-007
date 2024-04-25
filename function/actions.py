# from keras.models import Sequential
# from keras.layers import Dense, Input
# import numpy as np
# def exemple_entrainement_ia():
#     # Création du modèle
#     model = Sequential()

#     # Première couche, couche d'entrée
#     model.add(Input(shape=(1,))) 

#     # Deuxième couche, couche cachée
#     model.add(Dense(units=64, activation='relu')) 

#     # Troisième couche, couche de sortie
#     model.add(Dense(units=1)) 

#     # Définition des données d'entrée et de sortie
#     entree = np.array([1, 2, 3, 4, 5])
#     sortie = np.array([2, 4, 6, 8, 10])
#     # Compilation du modèle
#     model.compile(loss='mean_squared_error', optimizer='adam')

#     # Entraînement du modèle
#     model.fit(x=entree, y=sortie, epochs=1000)

#     # Prédiction
#     while True:
#         x = int(input('Nombre :'))
#         print('Prédiction :', model.predict(np.array([x])))

# initialise la liste d'actions de chaque joueurs pour le tour 0
def initialisation_joueurs(liste_action_j1,liste_action_j2,nb_vie_j1,nb_vie_j2 ):
    tour_j1= {
        "tour": 0,
        "nb_bal_j1" : 0,
        "nb_vie_j1" : nb_vie_j1
        }
    tour_j2 = {
        "tour": 0,
        "nb_bal_j2" : 0,
        "nb_vie_j2" : nb_vie_j2
    }
    liste_action_j1.append(tour_j1)
    liste_action_j2.append(tour_j2)
    print(f'Liste des actions du joueurs 1{liste_action_j1}\nListe des actions du joueurs 2 {liste_action_j2}')


def fonction_jouer(choix_rejouer):
    match choix_rejouer.upper() :
        case "O":
            return True
        case  "N":
            return False
        case _:
            print("On a dit O ou N... Lia considère que vous n'etes pas sufisament futé pour jouer avec elle !\nsalut.")
            return False

"""Fonction qui va enregistrer les actions des joueurs et mettre a jour la liste des actions 
"""
def actions_joueurs(action, joueurs, tour, nb_bal, nb_vie):
    liste={}
    if nb_bal !=0 :
        match action : 
            case 'T':
                print("Bang !")
                nb_bal = nb_bal - 1
            case 'R':
                print('Recharge !')
                nb_bal = nb_bal + 1
            case 'B':
                print("Bouclier !")
            case _:
                print('Error A-J-0: Entrer action joueur mauvaise !')
    else :
        match action : 
            case 'R':
                print('Recharge !')
                nb_bal = nb_bal + 1
            case 'B':
                print("Bouclier !")
            case _:
                print('Error A-J-0: Entrer action joueur mauvaise !')
    liste = {
        "tour": tour,
        "nb_bal_j1" : nb_bal,
        "nb_vie_j1" : nb_vie,
        "action" : action
    }

    joueurs.append(liste)


"""Gestion des coups de l'ia
"""
def actions_ia(action, joueurs, tour, nb_bal, nb_vie):
    liste={}
    if nb_bal !=0 :
        match action : 
            case 'T':
                print("Bang !")
                nb_bal = nb_bal - 1
            case 'R':
                print('Recharge !')
                nb_bal = nb_bal + 1
            case 'B':
                print("Bouclier !")
            case _:
                print('Error A-IA-0: Entrer action IA mauvaise !')
    else :
        match action : 
            case 'R':
                print('Recharge !')
                nb_bal = nb_bal + 1
            case 'B':
                print("Bouclier !")
            case _:
                print('Error A-IA-0: Entrer action IA mauvaise !')
    liste = {
        "tour": tour,
        "nb_bal_j2" : nb_bal,
        "nb_vie_j2" : nb_vie,
        "action" : action
    }

    joueurs.append(liste)

'''Fonction qui va affecter les bonnes interractions aux bonnes actions
'''
def compareMouvement(joueurJ1, joueurIA, tour):
    # Si l\'ia ou le joueur se prend un balle et ne protège pas alors il perd 1 pv  
    if(joueurJ1[tour]["action"] == "T" and joueurIA[tour]["action"] != "B"):
        joueurIA[tour]["nb_vie_j2"] = joueurIA[tour]["nb_vie_j2"] - 1
    if(joueurIA[tour]["action"] == "T" and joueurJ1[tour]["action"] != "B"):
        joueurJ1[tour]["nb_vie_j1"] = joueurJ1[tour]["nb_vie_j1"] -1
    
    print(f'Joueur : {joueurJ1[tour]["nb_vie_j1"]}')
    print(f'IA :{joueurIA[tour]["nb_vie_j2"]}')
        

