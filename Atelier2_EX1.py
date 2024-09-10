def somme1(L: list) -> int:
    """
    Calcule la somme des éléments d'une liste en utilisant une boucle for avec des indices.

    Paramètres:
    L (list): Liste des éléments.

    Retourne:
    int: La somme des éléments de la liste.
    """
    s = 0
    for i in range(len(L)):
        s += L[i]
    return s 

def somme2(L: list) -> int:
    """
    Calcule la somme des éléments d'une liste en utilisant une boucle for sur les éléments directement.

    Paramètres:
    L (list): Liste des éléments.

    Retourne:
    int: La somme des éléments de la liste.
    """
    s = 0
    for e in L:
        s += e
    return s 

def somme3(L: list) -> int:
    """
    Calcule la somme des éléments d'une liste en utilisant une boucle while.

    Paramètres:
    L (list): Liste des éléments.

    Retourne:
    int: La somme des éléments de la liste.
    """
    s = 0
    k = 0
    while k < len(L): 
        s += L[k]
        k += 1
    return s 

def moyenne(L: list) -> float:
    """
    Calcule la moyenne des éléments d'une liste.

    Paramètres:
    L (list): Liste des éléments.

    Retourne:
    float: La moyenne des éléments de la liste, ou 0 si la liste est vide.
    """
    return 0 if len(L) == 0 else somme2(L) / len(L)

def nb_sup1(L: list, e: int) -> int:
    """
    Compte le nombre d'éléments dans une liste qui sont supérieurs à une valeur donnée, en utilisant une boucle for avec des indices.

    Paramètres:
    L (list): Liste des éléments.
    e (int): La valeur de référence.

    Retourne:
    int: Le nombre d'éléments supérieurs à e.
    """
    c = 0
    for i in range(len(L)):
        if L[i] > e:
            c += 1 
    return c 

def nb_sup2(L: list, e: int) -> int:
    """
    Compte le nombre d'éléments dans une liste qui sont supérieurs à une valeur donnée, en utilisant une boucle for sur les éléments directement.

    Paramètres:
    L (list): Liste des éléments.
    e (int): La valeur de référence.

    Retourne:
    int: Le nombre d'éléments supérieurs à e.
    """
    c = 0
    for v in L:
        if v > e:
            c += 1 
    return c 

def val_max(L: list) -> int:
    """
    Trouve la valeur maximale dans une liste en vérifiant combien d'éléments sont supérieurs.

    Paramètres:
    L (list): Liste des éléments.

    Retourne:
    int: La valeur maximale de la liste, ou 0 si la liste est vide.
    """
    valmax = 0 
    for e in L:
        if nb_sup2(L, e) == 0:
            valmax = e
    return valmax

def ind_max(L: list) -> int:
    """
    Trouve l'indice de la valeur maximale dans une liste.

    Paramètres:
    L (list): Liste des éléments.

    Retourne:
    int: L'indice de la valeur maximale de la liste, ou -404 si la liste est vide.
    """
    return -404 if val_max(L) == 0 else L.index(val_max(L))

def test_exercice1() -> None:
    """
    Teste toutes les fonctions pour vérifier leur bon fonctionnement.
    """
    print("\nTEST SOMME")
    # Test liste vide
    print("Test liste vide : ", somme2([]))
    # Test somme 11111
    lst2test1 = [1, 10, 100, 1000, 10000]
    print("Test somme 1111 : ", somme2(lst2test1))

    print("\nTEST MOYENNE")
    # Test liste vide
    print("Test liste vide : ", moyenne([]))
    # Test moyenne 12.5
    lst2test2 = [0, 20, 15, 15]
    print("Test moyenne 12.5 : ", moyenne(lst2test2))

    print("\nTEST NB SUP")
    # Test liste vide
    print("Test liste vide : ", nb_sup2([], 3))
    # Test nb_sup 3
    lst2test3 = [0, 1, 2, 3, 4, 4, 5, 9, 3, 10]
    print("Test nb_sup 3 : ", nb_sup2(lst2test3, 4))

    print("\nTEST VALMAX")
    # Test liste vide
    print("Test liste vide : ", val_max([]))
    # Test valmax 12
    lst2test4 = [0, 1, 12, 3, 4, 4, 5, 9, 3, 10]
    print("Test valmax 12 : ", val_max(lst2test4))

    print("\nTEST INDMAX")
    # Test liste vide
    print("Test liste vide : ", ind_max([]))
    # Test ind_max 2
    lst2test4 = [0, 1, 12, 3, 4, 4, 5, 9, 3, 10]
    print("Test indmax 2 : ", ind_max(lst2test4))

# Appel des tests
test_exercice1()
