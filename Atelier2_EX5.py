from typing import List, Optional

def nb_occurence(lst: List[int], e: int) -> int:
    """
    Compte le nombre d'occurrences d'un élément `e` dans une liste `lst`.

    Args:
        lst (List[int]): La liste d'éléments.
        e (int): L'élément dont le nombre d'occurrences doit être compté.

    Returns:
        int: Le nombre d'occurrences de `e` dans `lst`.
    """
    c = 0
    for elt in lst:
        if elt == e:
            c += 1
    return c

def agencement(Lobj: List[int], nbEmplacements: int) -> Optional[List[List[int]]]:
    """
    Tente de répartir les éléments de `Lobj` dans deux sous-listes `V1` et `V2` 
    de taille `nbEmplacements` chacune, de sorte que chaque élément apparaisse 
    au maximum une fois dans chaque sous-liste.

    Args:
        Lobj (List[int]): La liste d'objets à répartir.
        nbEmplacements (int): Le nombre maximum d'emplacements dans chaque sous-liste.

    Returns:
        Optional[List[List[int]]]: Une liste contenant deux sous-listes [V1, V2] si la répartition est possible, 
        sinon None si la répartition ne peut pas être faite selon les contraintes.
    """
    # Trier la liste d'entrée
    L = sorted(Lobj)
    V1 = []
    V2 = []
    Popped = []
    j = 0
    LRepetition = [0] * len(L)
    
    # Calculer les occurrences de chaque élément dans L
    for i in range(len(L)):
        LRepetition[i] = nb_occurence(L, L[i])
  
    # Répartir les éléments en tenant compte des répétitions
    while j < len(L):
        if LRepetition[j] > 2:
            print("1")
            return None
        elif LRepetition[j] == 2 and len(V1) < nbEmplacements and len(V2) < nbEmplacements:
            V1.append(L[j])
            V2.append(L[j])
            Popped.append(L.pop(j))
            LRepetition.pop(j) 
        j += 1    

    # Retirer les éléments déjà ajoutés dans Popped
    for e in Popped: 
        L.remove(e)

    # Ajouter les éléments restants dans L aux listes V1 et V2
    for k in range(len(L)):
        if len(V1) < nbEmplacements:
            V1.append(L[k])
        elif len(V2) < nbEmplacements:
            V2.append(L[k])
        else:
            print("2")
            return None

    # Trier les listes résultantes pour un affichage ordonné
    V1.sort()
    V2.sort()
    return [V1, V2]

# Exemple d'utilisation
nbEmplacements = 4
lObjets = [1, 2, 2, 3, 4, 5, 5]

print(agencement(lObjets, nbEmplacements))
