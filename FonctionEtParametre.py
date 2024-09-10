import random 
import math
from datetime import date

""" EXERCICE 1 """

def message_imc(imc: float) -> str:
    """
    Retourne un message en fonction de l'indice de masse corporelle (IMC).

    Paramètres:
    imc (float): L'indice de masse corporelle (IMC) à interpréter.

    Retourne:
    str: Un message interprétant la catégorie de l'IMC.
    """
    if imc > 0:
        IMC = {
            (0, 16.5): "dénutrition ou famine",
            (16.5, 18.5): "maigreur",
            (18.5, 25): "corpulence normale",
            (25, 30): "surpoids",
            (30, 35): "obésité modérée",
            (35, 40): "obésité sévère",
            (40, math.inf): "obésité morbide",
        }
        imc_range = ()
        for l in list(IMC.keys()):
            if imc > l[0] and imc <= l[1]:
                imc_range = l
        return IMC.get(imc_range)
    else:
        return "Entrez un imc conforme"

def test_imc():
    """
    Teste la fonction message_imc avec différents cas, y compris des valeurs aléatoires,
    des valeurs limites et des cas de test connus.
    """
    print("aléatoire : ")
    for _ in range(10):
        rand_imc = random.randint(0, 40)
        print("imc de la personne : ", rand_imc , "interpétation", message_imc(rand_imc))
    print("test cas : ")
    for i in range(13, 44, 5):
        print("imc de la personne : ", i , "interpétation", message_imc(i))
    print("test limites : ")
    print("imc de la personne : ", 40 , "interpétation", message_imc(40)) 
    print("imc de la personne : ", 999, "interpétation", message_imc(999))    
    print("imc de la personne : ", -1, "interpétation", message_imc(-1)) 


""" EXERCICE 2 """

def est_bissextile(an: int) -> bool:
    """
    Vérifie si une année est bissextile.

    Paramètres:
    an (int): L'année à vérifier.

    Retourne:
    bool: True si l'année est bissextile, False sinon.
    """
    return (an % 4 == 0 and an % 100 != 0) or (an % 400) == 0

def test_bissextile():
    """
    Teste la fonction est_bissextile avec des années aléatoires et des cas spécifiques.
    """
    print("aléatoire : ")
    for _ in range(10):
        rand_an = random.randint(0, 3000)
        print("rand_an : ", rand_an, " : ", est_bissextile(rand_an))
    print("cas : 2024 ", est_bissextile(2024), "2023", est_bissextile(2023) ) 


""" EXERCICE 3 """

def discriminant(a: float, b: float, c: float) -> float:
    """
    Calcule le discriminant d'une équation quadratique.

    Paramètres:
    a (float): Coefficient de x^2.
    b (float): Coefficient de x.
    c (float): Terme constant.

    Retourne:
    float: La valeur du discriminant.
    """
    return pow(b, 2) - 4 * a * c

def racine_unique(a: float, b: float) -> float:
    """
    Calcule la racine unique d'une équation quadratique lorsque le discriminant est nul.

    Paramètres:
    a (float): Coefficient de x^2.
    b (float): Coefficient de x.

    Retourne:
    float: La racine unique de l'équation.
    """
    return -b / (2 * a)

def racine_double(a: float, b: float, delta: float, num: int) -> float:
    """
    Calcule les racines d'une équation quadratique lorsque le discriminant est positif.

    Paramètres:
    a (float): Coefficient de x^2.
    b (float): Coefficient de x.
    delta (float): Le discriminant de l'équation.
    num (int): Indique quelle racine calculer (1 ou 2).

    Retourne:
    float: La valeur de la racine calculée.
    """
    if num == 1: 
        return (-b + math.sqrt(delta)) / (2 * a)
    else: 
        return (-b - math.sqrt(delta)) / (2 * a)

def str_equation(a: float, b: float, c: float) -> str:
    """
    Formate une équation quadratique sous forme de chaîne de caractères.

    Paramètres:
    a (float): Coefficient de x^2.
    b (float): Coefficient de x.
    c (float): Terme constant.

    Retourne:
    str: L'équation quadratique sous forme de chaîne.
    """
    return str(a) + "x^2 + " + str(b) + "x + " + str(c) + " = 0"

def solution_equation(a: float, b: float, c: float) -> str:
    """
    Résout une équation quadratique et retourne les solutions sous forme de chaîne de caractères.

    Paramètres:
    a (float): Coefficient de x^2.
    b (float): Coefficient de x.
    c (float): Terme constant.

    Retourne:
    str: La solution de l'équation quadratique.
    """
    if discriminant(a, b, c) < 0: 
        return "Solution de l'équation " + str_equation(a, b, c) + ": Pas de racine réelle"
    elif discriminant(a, b, c) == 0:
        return "Solution de l'équation " + str_equation(a, b, c) + ": Racine unique : x = " + str(racine_unique(a, b))
    else: 
        return "Solution de l'équation " + str_equation(a, b, c) + ": Deux racines : \n x1 =  " + str(racine_double(a, b, discriminant(a, b, c), 1)) + "\n x2 = " + str(racine_double(a, b, discriminant(a, b, c), 2))

def equation(a: float, b: float, c: float) -> None:
    """
    Affiche la solution d'une équation quadratique.

    Paramètres:
    a (float): Coefficient de x^2.
    b (float): Coefficient de x.
    c (float): Terme constant.
    """
    print(solution_equation(a, b, c))

def test_equation():
    """
    Teste la fonction de résolution d'équation quadratique avec différents cas.
    """
    equation(2, 1, 3)
    equation(1, 5, 2)
    equation(2, 4, 2)


""" EXERCICE 4 """

def date_est_valide(jour: int, mois: int, annee: int) -> bool:
    """
    Vérifie si une date donnée est valide.

    Paramètres:
    jour (int): Le jour de la date.
    mois (int): Le mois de la date.
    annee (int): L'année de la date.

    Retourne:
    bool: True si la date est valide, False sinon.
    """
    jour_valide = False 
    mois_valide = False 
    liste_mois_30 = [4, 6, 9, 11]
    liste_mois_31 = [1, 3, 5, 7, 8, 10, 12]
    if mois in liste_mois_30 and 0 <= jour <= 30: 
        jour_valide = True
        mois_valide = True
    elif mois in liste_mois_31 and 0 <= jour <= 31: 
        jour_valide = True
        mois_valide = True
    else:
        if mois == 2:
            if 0 <= jour <= (29 if est_bissextile(annee) else 28):
                jour_valide = True
                mois_valide = True 
         
    return jour_valide and mois_valide 

def saisie_date_naissance() -> date: 
    """
    Demande à l'utilisateur de saisir sa date de naissance et vérifie si elle est valide.

    Retourne:
    date: La date de naissance saisie si elle est valide, sinon une date par défaut.
    """
    print("Rentrez votre date de naissance :")
    print("Rentrez d'abord votre jour de naissance : ")
    jour = int(input().lstrip('0'))
    print("Votre mois de naissance : ")
    mois = int(input().lstrip('0'))
    print("Et votre année de naissance : ")
    an = int(input())
    if date_est_valide(jour, mois, an): 
        return date(an, mois, jour)
    else: 
        print("Rentrez une date valide")
        return date(1000, 0, 0)

def age(date_naissance: date) -> int:
    """
    Calcule l'âge d'une personne à partir de sa date de naissance.

    Paramètres:
    date_naissance (date): La date de naissance de la personne.

    Retourne:
    int: L'âge de la personne.
    """
    today = date.today()
    age = today.year - date_naissance.year
    if (today.month, today.day) < (date_naissance.month, date_naissance.day):
        age -= 1 

    return age

def est_majeur(date_naissance: date) -> bool:
    """
    Vérifie si une personne est majeure en fonction de sa date de naissance.

    Paramètres:
    date_naissance (date): La date de naissance de la personne.

    Retourne:
    bool: True si la personne est majeure (18 ans ou plus), False sinon.
    """
    return age(date_naissance) >= 18

def test_acess():
    """
    Teste l'accès d'une personne en fonction de son âge et de sa date de naissance.
    """
    date_naissance = saisie_date_naissance()
    if est_majeur(date_naissance):
        print("Bonjour, vous avez ", age(date_naissance), " ans, Accès autorisé")
    else:
        print("Désolé, vous avez ", age(date_naissance), " ans, Accès interdit")

def test_age():
    """
    Teste la validité des dates et l'âge des utilisateurs pour vérifier s'ils sont majeurs.
    """
    print("Date : ")
    print(date_est_valide(2, 12, 2004))
    print(date_est_valide(29, 2, 2024))
    print(date_est_valide(29, 2, 2023))
    print(date_est_valide(28, 2, 2023))
    print(date_est_valide(31, 6, 2021))
    print("Majeur : Tester 4 types ")
    for i in range(4):
        test_acess()

""" TESTS """

print("Quel exercice ? (1,2,3,4): ")
ex = int(input())
if ex == 1: 
    print("EXERCICE 1")
    test_imc()
elif ex == 2:
    print("EXERCICE 2")
    test_bissextile()
elif ex == 3:
    print("EXERCICE 3")
    test_equation()
elif ex == 4:
    print("EXERCICE 4")
    test_age()
