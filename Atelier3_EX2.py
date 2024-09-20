from typing import List

def mots_Nlettres(lst_mot: List[str], n: int) -> List[str]:
    """
    Retourne une liste de mots ayant exactement 'n' lettres.

    :param lst_mot: Liste de mots.
    :param n: Longueur des mots souhaitée.
    :return: Liste de mots de longueur 'n'.
    """
    Lmotsn = []
    for mot in lst_mot:
        if len(mot) == n:
            Lmotsn.append(mot)
    return Lmotsn

def commence_par(mot: str, prefixe: str) -> bool:
    """
    Vérifie si un mot commence par un préfixe donné.

    :param mot: Le mot à vérifier.
    :param prefixe: Le préfixe à rechercher.
    :return: True si le mot commence par le préfixe, sinon False.
    """
    return mot[:len(prefixe)] == prefixe

def finit_par(mot: str, suffixe: str) -> bool:
    """
    Vérifie si un mot finit par un suffixe donné.

    :param mot: Le mot à vérifier.
    :param suffixe: Le suffixe à rechercher.
    :return: True si le mot finit par le suffixe, sinon False.
    """
    return mot[len(mot)-len(suffixe):] == suffixe

def commencent_par(lst_mot: List[str], prefixe: str) -> List[str]:
    """
    Retourne une liste de mots qui commencent par un préfixe donné.

    :param lst_mot: Liste de mots.
    :param prefixe: Le préfixe à rechercher.
    :return: Liste de mots qui commencent par le préfixe.
    """
    L = []
    for mot in lst_mot:
        if commence_par(mot, prefixe):
            L.append(mot)
    return L

def finissent_par(lst_mot: List[str], suffixe: str) -> List[str]:
    """
    Retourne une liste de mots qui finissent par un suffixe donné.

    :param lst_mot: Liste de mots.
    :param suffixe: Le suffixe à rechercher.
    :return: Liste de mots qui finissent par le suffixe.
    """
    L = []
    for mot in lst_mot:
        if finit_par(mot, suffixe):
            L.append(mot)
    return L

def liste_mots(lst_mot: List[str], prefixe: str, suffixe: str, n: int) -> List[str]:
    """
    Retourne une liste de mots qui commencent par un préfixe, finissent par un suffixe et ont une longueur spécifique.

    :param lst_mot: Liste de mots.
    :param prefixe: Le préfixe à rechercher.
    :param suffixe: Le suffixe à rechercher.
    :param n: Longueur des mots souhaitée.
    :return: Liste de mots répondant aux critères.
    """
    Lcom = commencent_par(lst_mot, prefixe)
    Lfin = finissent_par(lst_mot, suffixe)
    Ln = mots_Nlettres(lst_mot, n)

    return list(set(Lcom) & set(Lfin) & set(Ln))

def dictionnaire(fichier: str) -> List[str]:
    """
    Lit un fichier texte contenant un mot par ligne et renvoie une liste des mots.

    :param fichier: Nom du fichier à lire.
    :return: Liste de mots présents dans le fichier.
    """
    mots = []
    try:
        with open(fichier, "r") as f:
            for ligne in f:
                mots.append(ligne.strip())  # Supprime les espaces blancs et \n
    except FileNotFoundError:
        print(f"Erreur : le fichier '{fichier}' n'a pas été trouvé.")
    return mots

lst_mot = ["jouer", "bonjour", "punir", "jour", "aurevoir", "revoir", "pouvoir", "cour", "abajour", "finir", "aimer"]

def test() -> None:
    """
    Teste les différentes fonctions avec des cas de test prédéfinis.
    """
    # Tester la fonction avec un fichier exemple "littre.txt"
    mots_du_dictionnaire = dictionnaire("littre.txt")
    if mots_du_dictionnaire:
        print("Fichier lu")
    print("TEST MOTS N LETTRES")
    print(mots_Nlettres(lst_mot, 5))
    print("TEST COMMENCE / FINIT")
    print("commence_par(jouer,jo)")
    print(commence_par("jouer", "jo"))
    print("commence_par(jouer,ka)")
    print(commence_par("jouer", "ka"))
    print("finit_par(jouer,uer)")
    print(finit_par("jouer", "uer"))
    print("finit_par(jouer,ka)")
    print(finit_par("jouer", "ka"))
    print("finissent_par(lst_mot,jour)")
    print(finissent_par(lst_mot, "jour"))
    print("commencent_par(lst_mot,jour)")
    print(commencent_par(lst_mot, "jo"))

    print("liste_mots(lst_mot,au,revoir,8)")
    print(liste_mots(lst_mot, "au", "revoir", 8))

    print("liste_mots(lst_mot,a,ir,7)")
    print(liste_mots(mots_du_dictionnaire, "a", "ir", 7))
    
   

test()
