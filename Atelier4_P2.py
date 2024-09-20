import numpy as np

def my_searchsorted(table: np.ndarray, element: int) -> int:
    """
    Recherche l'indice où insérer un élément dans un tableau trié.

    Args:
        table (np.ndarray): Le tableau trié dans lequel l'élément doit être inséré.
        element (int): L'élément à insérer.

    Returns:
        int: L'indice où l'élément doit être inséré dans le tableau.
    """
    for i in range(len(table)):
        if element <= table[i]:
            return i
    return len(table)


def my_where(table: np.ndarray, valeur: int) -> tuple[np.ndarray, np.ndarray]:
    """
    Retourne les indices des occurrences d'une valeur donnée dans un tableau 1D ou 2D.

    Args:
        table (np.ndarray): Tableau 1D ou 2D dans lequel rechercher la valeur.
        valeur (int): La valeur à rechercher.

    Returns:
        tuple: Indices des lignes et colonnes où la valeur est trouvée. 
               Pour un tableau 1D, un seul tableau d'indices est retourné.
    """
    L1 = []
    L2 = []
    
    if table.ndim == 1:
        for i in range(len(table)):
            if table[i] == valeur:
                L1.append(i)
        return (np.array(L1),)  # Retourné sous forme de tuple avec un seul élément
    
    else:
        for i in range(len(table)):
            for j in range(len(table[i])):
                if table[i][j] == valeur:
                    L1.append(i)
                    L2.append(j)
        return (np.array(L1), np.array(L2))


def my_add1(tableA: np.ndarray, tableB: np.ndarray) -> np.ndarray:
    """
    Effectue l'addition élément par élément de deux matrices 2D.

    Args:
        tableA (np.ndarray): La première matrice 2D.
        tableB (np.ndarray): La deuxième matrice 2D.

    Returns:
        np.ndarray: La matrice résultante de l'addition.
                    Retourne une matrice vide si les dimensions ne correspondent pas.
    """
    tableSum = []
    lenA = len(tableA)
    if lenA != len(tableB):
        return np.array([])
    else:
        for i in range(lenA):
            tableSum.append([])
            for j in range(lenA):
                tableSum[i].append(tableA[i][j] + tableB[i][j])
        return np.array(tableSum)


def my_add2(tableA: np.ndarray, tableB: np.ndarray) -> np.ndarray:
    """
    Effectue l'addition élément par élément de deux matrices 2D en utilisant np.ndenumerate.

    Args:
        tableA (np.ndarray): La première matrice 2D.
        tableB (np.ndarray): La deuxième matrice 2D.

    Returns:
        np.ndarray: La matrice résultante de l'addition.
                    Retourne une matrice vide si les dimensions ne correspondent pas.
    """
    tableSum = []

    if np.shape(tableA) != np.shape(tableB):
        return np.array([])

    for index, _ in np.ndenumerate(tableA):
        i, j = index
        if i == len(tableSum):
            tableSum.append([])

        tableSum[i].append(tableA[i][j] + tableB[i][j])

    return np.array(tableSum)


def matrice_trace(matrice: np.ndarray) -> int:
    """
    Calcule la trace d'une matrice carrée (somme des éléments de la diagonale principale).

    Args:
        matrice (np.ndarray): La matrice carrée.

    Returns:
        int: La trace de la matrice.
    """
    T = 0
    for i in range(len(matrice)):
        T += matrice[i][i]
    return T


def est_symetrique(matrice: np.ndarray) -> bool:
    """
    Vérifie si une matrice est symétrique.

    Args:
        matrice (np.ndarray): La matrice carrée à vérifier.

    Returns:
        bool: True si la matrice est symétrique, False sinon.
    """
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            if matrice[i][j] != matrice[j][i]:
                return False
    return True


def produit_diagonale(matrice: np.ndarray) -> int:
    """
    Calcule le produit des éléments de la diagonale principale d'une matrice carrée.

    Args:
        matrice (np.ndarray): La matrice carrée.

    Returns:
        int: Le produit des éléments de la diagonale.
    """
    T = 1
    for i in range(len(matrice)):
        T *= matrice[i][i]
    return T


# Exemple d'utilisation des fonctions

# Matrice aléatoire 4x4 et matrice identité
A = np.random.randint(0, 10, size=(4, 4))
I = np.eye(4)

# Trace de la matrice
TraceA = matrice_trace(A)
print("A : \n", A)
print("Trace A : ", TraceA)

# Symétrie de (A + A.T) / 2
print("Symétrie de (A + A.T)/2 :\n", (A + A.T)/2, " : ", est_symetrique((A + A.T)/2))

# Produit de la diagonale de la matrice identité
print("I :\n", I)
print("Produit Diagonale I : ", produit_diagonale(I))

# Test si A^(-1) * A = I
print("Test A^(-1) * A = I ? \n", A @ np.linalg.inv(A))
