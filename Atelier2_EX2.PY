def position1(lst,elt):
    for i in range(len(lst)) : 
        if lst[i] == elt :
            return i
    return -1
def position2(lst,elt):
    k = 0
    while lst[k] != elt :
        k += 1 
        if k >= len(lst) : 
            return -1
    return k
lstTEST = [1,2,4,3,5,7,6] 
print("TEST POS")
print(position1(lstTEST,2))    
print(position1(lstTEST,10))  
print(position2(lstTEST,2))  
print(position2(lstTEST,10)) 

def nb_occurence(lst,e):
    c = 0 
    for elt in lst :
        if elt == e :
            c +=1 
    return c 

print("TEST NBCOCURENCE")
lstTEST2 = [1,2,4,3,5,7,6,7,3] 
print(nb_occurence(lstTEST2,7))

def est_triee1(lst):
    prev = 0 
    c = 0
    for i in range(len(lst)):
        if i == 0 :
            c += 1
            prev = lst[i]
        elif lst[i] > prev :
            c += 1 
            prev = lst[i]
    return c == len(lst)    

def est_triee2(lst: list[int]) -> bool:
    """
    Vérifie si la liste est triée par ordre croissant en utilisant une boucle while.

    Paramètres:
    lst (list[int]): Liste des entiers.

    Retourne:
    bool: True si la liste est triée par ordre croissant, False sinon.
    """
    i = 0
    while i < len(lst) - 1:
        if lst[i] > lst[i + 1]:
            return False
        i += 1
    return True
#la meilleure version semble être la 2 

lstTEST3 = [1,2,3,5,7,8]     
lstTEST4 = [1,2,9,5,7,8]      
print("TEST TRIE")
print(est_triee1(lstTEST3))
print(est_triee1(lstTEST4))
print(est_triee2(lstTEST3))
print(est_triee2(lstTEST4))

def position_tri(lst: list[int], e: int) -> int:
    """
    Recherche l'indice de l'élément e dans une liste triée lst en utilisant la recherche dichotomique.

    Paramètres:
    lst (list[int]): Liste triée des entiers.
    e (int): Élément à rechercher dans la liste.

    Retourne:
    int: L'indice de l'élément e dans lst s'il est présent, sinon -1.
    """
    if est_triee2(lst) :
        debut = 0
        fin = len(lst) - 1

        while debut <= fin:
            milieu = (debut + fin) // 2  # Calcul de l'indice milieu

            if lst[milieu] == e:  # Élément trouvé
                return milieu
            elif lst[milieu] < e:  # Élément est dans la moitié droite
                debut = milieu + 1
            else:  # Élément est dans la moitié gauche
                fin = milieu - 1

        return -1  # Élément non trouvé
    else :
        return -1

lstTEST5 = [1,3,7,10]
print("TEST POS TRI")
print(position_tri(lstTEST5,7))

def a_repetitions(lst: list[int]) -> bool:
    """
    Vérifie si la liste lst comporte des répétitions de valeurs en utilisant une boucle while.

    Paramètres:
    lst (list[int]): Liste des entiers à vérifier.

    Retourne:
    bool: True si la liste comporte des répétitions, False sinon.
    """
    T = []  # Liste temporaire pour stocker les éléments uniques
    i = 0   # Initialisation de l'indice de la boucle

    while i < len(lst):
        if lst[i] in T:
            return True  # Une répétition est trouvée
        else:
            T.append(lst[i])  # Ajout de l'élément unique à la liste T
        i += 1  # Incrémentation de l'indice
    
    return False  # Aucune répétition trouvée
lstTEST6 = [1,2,3,4]
lstTEST7 = [1,4,6,8,8]
print("TEST REPETITION")
print(a_repetitions(lstTEST6))
print(a_repetitions(lstTEST7))
