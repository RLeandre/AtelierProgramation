import random

def build_dict(lst: list) -> dict:
    """
    Construit un dictionnaire basé sur la longueur des mots.
    
    Args:
        lst (list): Liste de mots.
    
    Returns:
        dict: Dictionnaire avec la longueur des mots comme clé et une liste de mots correspondants comme valeur.
    """
    dictionnaire_mots = {}
    
    for mot in lst:
        longueur = len(mot)
        if longueur not in dictionnaire_mots:
            dictionnaire_mots[longueur] = []
        dictionnaire_mots[longueur].append(mot)
    
    return dictionnaire_mots

def select_word(sorted_words: dict, word_len: int) -> str:
    """
    Sélectionne un mot au hasard dans la liste des mots de taille `word_len` du dictionnaire.
    
    Args:
        sorted_words (dict): Dictionnaire des mots triés par longueur.
        word_len (int): Longueur du mot à sélectionner.
    
    Returns:
        str: Un mot choisi au hasard.
    """
    if word_len in sorted_words and sorted_words[word_len]:
        return random.choice(sorted_words[word_len])
    return None

def places_lettre(ch: str, mot: str) -> list:
    """
    Renvoie une liste des indices où la lettre 'ch' apparaît dans le mot 'mot'.
    
    Args:
        ch (str): La lettre à chercher.
        mot (str): Le mot dans lequel on cherche la lettre.
    
    Returns:
        list: Une liste des positions où la lettre 'ch' apparaît dans le mot 'mot'.
    """
    L = []
    for i in range(len(mot)):
        if mot[i] == ch:
            L.append(i)
    return L

def outputStr(mot: str, lpos: list, mot_pendu: str = '') -> str:
    """
    Met à jour le mot pendu en révélant les lettres aux positions indiquées par 'lpos'.
    
    Args:
        mot (str): Le mot à deviner.
        lpos (list): Les positions où les lettres ont été trouvées.
        mot_pendu (str): Le mot pendu actuel avec des lettres trouvées et des '_'.
    
    Returns:
        str: Le mot avec les lettres trouvées et des '_' pour les lettres non trouvées.
    """
    if mot_pendu:
        liste_mot_modif = list(mot_pendu)
    else:
        liste_mot_modif = ['_'] * len(mot)

    for p in lpos:
        liste_mot_modif[p] = mot[p]
    
    mot_modif = ''.join(liste_mot_modif)
    return mot_modif

def build_list(fileName: str) -> list:
    """
    Lit un fichier et renvoie une liste des mots.
    
    Args:
        fileName (str): Nom du fichier à lire.
    
    Returns:
        list: Liste des mots extraits du fichier.
    """
    with open(fileName, "r") as file:
        content = file.readlines()
    
    capitales_list = []
    for line in content:
        words = line.strip().split("\t")
        for word in words:
            capitales_list.append(word.lower())
    
    return capitales_list

def choisir_difficulte() -> int:
    """
    Demande à l'utilisateur de choisir un niveau de difficulté et renvoie la longueur du mot correspondante.
    
    Returns:
        int: Longueur du mot correspondant au niveau de difficulté.
    """
    print("Choisissez un niveau de difficulté :")
    print("1. Easy (taille < 7)")
    print("2. Normal (6 < taille < 9)")
    print("3. Hard (taille > 8)")
    
    choix = input("Votre choix (1/2/3) : ")
    
    if choix == "1":
        return random.randint(1, 6)
    elif choix == "2":
        return random.randint(7, 8)
    elif choix == "3":
        return random.randint(9, 20)
    else:
        print("Choix invalide. Par défaut, difficulté 'Normal' sera sélectionnée.")
        return random.randint(7, 8)

def runGame():
    """
    Lance le jeu du pendu avec un mot aléatoire tiré en fonction du niveau de difficulté sélectionné par le joueur.
    """
    # Charger les capitales depuis un fichier texte
    lst = build_list("capitales.txt")
    dictionnaire_mots = build_dict(lst)
    
    # Demander à l'utilisateur de choisir un niveau de difficulté
    word_len = choisir_difficulte()
    
    # Sélectionner un mot basé sur le niveau de difficulté
    mot = select_word(dictionnaire_mots, word_len)
    
    if not mot:
        print(f"Aucun mot trouvé pour la taille {word_len}.")
        return
    
    nb_erreur = 0
    pendu = ["|---] ", "| O ", "| T ", "|/ \\ ", "|______"]
    
    print("Voici le mot : ")
    mot_pendu = outputStr(mot, [])
    print(mot_pendu)

    while nb_erreur < 5:
        if mot_pendu == mot:
            print("Gagné !")
            break

        print('Choisissez une lettre : ')
        l = input().strip().lower()
        p_l = places_lettre(l, mot)

        if not p_l:
            print("Cette lettre n'est pas dans le mot.")
            nb_erreur += 1
            print(mot_pendu)
            for i in range(nb_erreur):
                print(pendu[i])
            print(f"Plus que {5 - nb_erreur} chances")
        else:
            print('La lettre est dans le mot !')
            mot_pendu = outputStr(mot, p_l, mot_pendu)
            print(mot_pendu)

    if nb_erreur >= 5:
        print("Perdu ! Le mot était :", mot)

# Lancer le jeu
runGame()
