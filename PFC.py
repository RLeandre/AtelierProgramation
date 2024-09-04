import random

partieAI = input("Voulez-vous jouer contre l'ordinateur (Max 5 parties) O/N ? " )

while partieAI != 'O' and partieAI != 'N':
     print("Je n'ai pas compris votre réponse")
     partieAI = input("Voulez-vous jouer contre l'ordinateur (Max 5 parties) O/N ? " )

if partieAI == 'O':
    nomJ1 = input("Quel est votre nom ? ")
    print("Bienvenu ",nomJ1, " nous allons jouer ensemble \n")
    nomJ2 = 'Machine'

else :
    nomJ1 = input("Quel est votre nom ? ")
    print("Bienvenu ",nomJ1, " nous allons jouer ensemble")
    nomJ2 = input("Quel est le nom du deuxième joueur ?")
    print("Bienvenu ",nomJ2, " nous allons jouer ensemble \n")

scoreJ1 = 0
nbr_tours = 0
continuer = True
scoreJ2 = 0

while continuer :
    nbr_tours += 1 
    choixJ1 = input("{nom} faîtes votre choix parmi (pierre, papier, ciseaux): ".format(nom=nomJ1))

    while choixJ1 != 'pierre' and choixJ1 != 'papier' and choixJ1 != 'ciseaux': 
                print("Je n'ai pas compris votre réponse") 
                choixJ1 = input("Joueur ", nomJ1 ," faîtes votre choix parmi (pierre, papier, ciseaux): ")

    if partieAI == 'O': 
        choixJ2 = ['papier','pierre','ciseaux'][random.randint(0, 2)]

    else :
        choixJ2 = input("Joueur ", nomJ2 ," faîtes votre choix parmi (pierre, papier, ciseaux): ")
        while choixJ2 != 'pierre' and choixJ2 != 'papier' and choixJ2 != 'ciseaux': 
                print("Je n'ai pas compris votre réponse") 
                choixJ2 = input("Joueur ", nomJ2 ," faîtes votre choix parmi (pierre, papier, ciseaux): ")   

    #On affiche les choix de chacun
    print("Si on récapitule :",nomJ1, choixJ1, "et", nomJ2, choixJ2,"\n")

    #On regarde qui a gagné cette manche on calcule les points et on affiche le résultat
    #On simplifie les cas les transformants en int les choix pour les opérations 
    l_verif = ['papier','pierre','ciseaux']

    val_choixJ1 = l_verif.index(choixJ1)
    
    val_choixJ2 = l_verif.index(choixJ2)
    
 
    #Les cas d'égalité 
    if val_choixJ1 == val_choixJ2 :
        gagnant = "aucun de vous, vous être ex æquo"
        scoreJ1 = scoreJ1 + 0
        scoreJ2 = scoreJ2 + 0
    #Les cas où le joueur 1 perd
    elif val_choixJ1 - val_choixJ2 == -2 or  val_choixJ1 - val_choixJ2 == 1 :
        gagnant = nomJ2
        scoreJ1 = scoreJ1 + 0
        scoreJ2 = scoreJ2 + 1
    #Les cas où le joueur 1 gagne 
    else :
        gagnant = nomJ1
        scoreJ1 = scoreJ1 + 1
        scoreJ2 = scoreJ2 + 0     


    print("le gagnant est",gagnant)
    print("Les scores à l'issue de cette manche sont donc",nomJ1, scoreJ1, "et", nomJ2, scoreJ2, "\n")

    if nbr_tours == 5:
        continuer = False       

    else :
        #On propose de continuez ou de s'arrêter 
        go = input("Souhaitez vous refaire une partie {} contre {} ? (O/N) ".format(nomJ1,nomJ2))
        #Tant que l'on a pas de réponse on redemande 
        while go != 'O' and go != 'N':
            print("Vous ne répondez pas à la question, on continue ")
            go = input("Souhaitez vous refaire une partie {} contre {} ? (O/N) ".format(nomJ1,nomJ2))
        #On continue si l'input est 'O'
        continuer = (go == 'O')
           
if continuer == False :
    print("Merci d'avoir joué ! A bientôt")