from typing import List

# Question 1 

def valMax(lst: list) -> int:
    """
    Trouve la valeur maximale dans une liste.
    
    Paramètres:
        lst (list): Une liste d'entiers.
    
    Retourne:
        int: La valeur maximale dans la liste.
    """
    maxi = 0
    for elt in lst:
      if maxi < elt:
        maxi = elt
    return maxi

def histo(liste: List[int]) -> List[int]:
    """
    Calcule l'histogramme des fréquences des valeurs dans la liste.
    
    Paramètres:
    liste (List[int]): Liste représentant les valeurs de la fonction.
    
    Retourne:
    List[int]: Liste des fréquences des valeurs.
    """
    # Initialiser l'histogramme avec des zéros
    valeurMax = valMax(liste)
    histo = [0] * (valeurMax + 1)
    
    # Remplir l'histogramme avec les fréquences
    for e in liste:
        if 0 <= e <= valeurMax:
            histo[e] += 1
    
    return histo


def est_injective(liste: List[int]) -> bool:
    """
    Vérifie si la fonction définie par la liste est injective.
    
    Paramètres:
    liste (List[int]): Liste représentant les valeurs de la fonction.
    
    Retourne:
    bool: True si la fonction est injective, False sinon.
    """

    histogramme = histo(liste)
    for e in histogramme :
        if e > 1 :
            return False
    return True


def est_surjective(liste: List[int]) -> bool:
    """
    Vérifie si la fonction définie par la liste est surjective.
    
    Paramètres:
    liste (List[int]): Liste représentant les valeurs de la fonction.
    
    Retourne:
    bool: True si la fonction est surjective, False sinon.
    """
    histogramme = histo(liste)
    for e in histogramme :
        if e < 1 :
            return False
    return True

def est_bijective(liste: List[int]) -> bool:
    """
    Vérifie si la fonction définie par la liste est bijective.
    
    Paramètres:
    liste (List[int]): Liste représentant les valeurs de la fonction.
    
    Retourne:
    bool: True si la fonction est bijective, False sinon.
    """
    return est_injective(liste) and est_surjective(liste)


def test_fonctions():
    # Test 1
    F1 = [6, 5, 6, 7, 4, 2, 1, 5]
    print("Test 1:")
    print("Histogramme:", histo(F1))
    print("Injective:", est_injective(F1))
    print("Surjective:", est_surjective(F1))
    print("Bijective:", est_bijective(F1))

    # Test 2
    F2 = [3, 0, 6, 7, 4, 2, 1, 5]
    print("\nTest 2:")
    print("Histogramme:", histo(F2))
    print("Injective:", est_injective(F2))
    print("Surjective:", est_surjective(F2))
    print("Bijective:", est_bijective(F2))

    # Test 3
    F3 = [0, 1, 2, 3]
    print("\nTest 3:")
    print("Histogramme:", histo(F3))
    print("Injective:", est_injective(F3))
    print("Surjective:", est_surjective(F3))
    print("Bijective:", est_bijective(F3))

    # Test 4
    F4 = [1, 1, 1]
    print("\nTest 4:")
    print("Histogramme:", histo(F4))
    print("Injective:", est_injective(F4))
    print("Surjective:", est_surjective(F4))
    print("Bijective:", est_bijective(F4))

# Lancer les tests
test_fonctions()

# Question 2

def afficheHisto(F: List[int]) -> None:
    """
    Affiche un histogramme basé sur une liste d'entiers.

    Paramètres:
        F (List[int]): Liste d'entiers représentant les fréquences à afficher dans l'histogramme.

    Retourne:
        None
    """
    # Générer l'histogramme des fréquences
    histogramme = histo(F)
    # Trouver la valeur maximale dans l'histogramme
    maxOcc = valMax(histogramme)
    
    # Initialiser la chaîne de caractères pour le résultat
    strResultat = "HISTOGRAMME\n"

    # Construire l'histogramme ligne par ligne
    for niveau in range(maxOcc, 0, -1):
        for freq in histogramme:
            if freq >= niveau:
                strResultat += " # "  # Affiche un symbole pour la fréquence
            else:
                strResultat += "   "  # Affiche un espace vide
        strResultat += '\n'

    # Afficher les indices des valeurs
    for i in range(len(histogramme)):
        strResultat += f' {i} '

    print(strResultat)

# Exemple d'utilisation
lstFreq = [2, 3, 1, 8, 9, 4, 2, 3, 2, 10, 11, 11, 8, 9, 7, 4, 2, 1, 5, 6, 8, 9, 0, 8, 7, 6, 6, 3, 4, 4, 4, 2, 5]
print("Histogramme des fréquences:")
afficheHisto(lstFreq)
