from typing import List

def separer(L: List[int]) -> List[int]:
    """
    Sépare les éléments de la liste L en trois catégories : négatifs, nuls, et positifs.
    Les négatifs sont placés à gauche, les zéros au centre, et les positifs à droite.
    La liste LSEP a la même taille que L.

    Paramètres:
    L (List[int]): Liste d'entiers à séparer.

    Retourne:
    List[int]: Liste séparée avec les éléments négatifs à gauche, les zéros au centre,
               et les éléments positifs à droite.
    """
    # Initialisation de la liste LSEP
    LSEP = [0] * len(L)

    # Indices pour placer les éléments
    index_neg = 0
    index_zero = 0
    index_pos = len(L) - 1

    # Parcourir les éléments de L
    for e in L:
        if e < 0:
            LSEP[index_neg] = e
            index_neg += 1
        elif e == 0:
            LSEP[index_zero + (index_neg - index_zero)] = e
            index_zero += 1
        else:
            LSEP[index_pos] = e
            index_pos -= 1

    return LSEP

# Exemple d'utilisation
L = [3, -1, 0, 4, -2, 0, 1, -3,2,-10]
print("Liste : ", L)
print("Liste séparée : ", separer(L))
