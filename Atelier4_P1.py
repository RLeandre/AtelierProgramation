# Question 1

def somme_recursive(liste: list[float]) -> float:
    """
    Calcule la somme d'une liste de nombres flottants de manière récursive.
    
    Args:
        liste (list[float]): La liste des nombres à sommer.
    
    Returns:
        float: La somme des éléments de la liste.
    """
    if liste == []: 
        return 0 
    else: 
        return liste[0] + somme_recursive(liste[1:])
    
# Test de la fonction
liste1 = [1.0, 2.0, 3.0, 4.0, 5.0]
resultat1 = somme_recursive(liste1)
print("La somme de la liste est :", resultat1)

liste2 = []
resultat2 = somme_recursive(liste2)
print("La somme de la liste est :", resultat2)


# Question 2 

def factorielle_recursive(nombre: int) -> int:
    """
    Calcule la factorielle d'un nombre entier de manière récursive.
    
    Args:
        nombre (int): Le nombre dont on souhaite calculer la factorielle.
    
    Returns:
        int: La factorielle de l'entier donné.
    """
    if nombre == 0:
        return 1 
    else:
        if nombre == 1:
            return 1
        else:
            return nombre * factorielle_recursive(nombre - 1)

# Test de la fonction
nombre = 5
resultat = factorielle_recursive(nombre)
print("Le factoriel de", nombre, "est :", resultat)


# Question 3 

def longueur(lst: list) -> int:
    """
    Calcule la longueur d'une liste de manière récursive.
    
    Args:
        lst (list): La liste dont on souhaite calculer la longueur.
    
    Returns:
        int: La longueur de la liste.
    """
    if lst:
        return 1 + longueur(lst[1:])
    else: 
        return 0

print("La longueur de [1,2,5] est ", longueur([1,2,5]))


# Question 4 

def minimum(lst: list[int]) -> int:
    """
    Trouve le minimum d'une liste d'entiers de manière récursive.
    
    Args:
        lst (list[int]): La liste d'entiers à évaluer.
    
    Returns:
        int: Le plus petit élément de la liste.
    """
    if len(lst) == 1:
        return lst[0]
    else:
        min_val = minimum(lst[1:])
        if lst[0] < min_val:
            return lst[0]
        else:
            return min_val

print("Le minimum dans [12,5,3,6,4] est ", minimum([12,5,3,6,4]))


# Question 5 

def listPairs(lst: list[int]) -> list[int]:
    """
    Extrait les nombres pairs d'une liste d'entiers de manière récursive.
    
    Args:
        lst (list[int]): La liste d'entiers à filtrer.
    
    Returns:
        list[int]: Une nouvelle liste contenant uniquement les nombres pairs.
    """
    if lst == []: 
        return []
    if lst[0] % 2 == 0:
        return [lst[0]] + listPairs(lst[1:])
    else:
        return listPairs(lst[1:])

print("Les pairs de la liste [12,5,3,6,4] sont : ", listPairs([12,5,3,6,4]))


# Question 6 

def concat_list(LL: list[list]) -> list:
    """
    Concatène une liste de listes en une seule liste de manière récursive.
    
    Args:
        LL (list[list]): La liste de listes à concaténer.
    
    Returns:
        list: La liste concaténée.
    """
    if len(LL) == 1:
        return LL[0]
    else:
        return LL[0] + concat_list(LL[1:])

# Test de la fonction
print(concat_list([[0, 1], [2, 3], [4], [6, 7]]))

# Test de la fonction
print(concat_list(["Ceci est ", "un test ", "de la ", "concatenation"]))  # "Ceci est un test de la concatenation"


# Question 7 

def incluse(L1: list, L2: list) -> bool:
    """
    Vérifie si tous les éléments de la liste L1 sont inclus dans la liste L2 de manière récursive.
    
    Args:
        L1 (list): La première liste à vérifier.
        L2 (list): La deuxième liste dans laquelle vérifier les éléments.
    
    Returns:
        bool: True si tous les éléments de L1 sont dans L2, False sinon.
    """
    if not L1:
        return True
    else:
        if len(L1) == 1:
            return L1[0] in L2
        else:
            return L1[0] in L2 and incluse(L1[1:], L2)

# Tests
print("Test incluse : [],[4,3] ")
print(incluse([], [4, 3])) 

print("Test incluse : [],[] ")
print(incluse([], [])) 

print("Test incluse : [1,2,6],[1,2,3,5,6] ")
print(incluse([1, 2, 6], [1, 2, 3, 5, 6]))

print("Test incluse : [1, 2,3],[1,2] ")
print(incluse([1, 2, 3], [1, 2]))

print("Test incluse : [1,2],[] ")
print(incluse([1, 2], []))
