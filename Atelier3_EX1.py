def full_name(str_arg: str) -> str:
    """
    Prend une chaîne de caractères au format 'nom prenom' et retourne 
    une nouvelle chaîne avec le nom en majuscules et le prénom avec 
    seulement la première lettre en majuscule.

    Args:
        str_arg (str): Une chaîne de caractères contenant le nom et le prénom.

    Returns:
        str: Une nouvelle chaîne avec le nom en majuscules et le prénom 
        avec seulement la première lettre en majuscule.
    """
    # Séparer la chaîne en nom et prénom
    nom, prenom = str_arg.split()
    
    # Transformer le nom en majuscules et le prénom avec la première lettre en majuscule
    nom = nom.upper()
    prenom = prenom.capitalize()
    
    # Retourner la chaîne formatée
    return f"{nom} {prenom}"

# Exemple d'utilisation
print(full_name("raeth léandre")) 


def is_mail(str_arg: str) -> (int, int):
    """
    Vérifie la validité d'une adresse e-mail et retourne un tuple 
    représentant la validité et le code d'erreur correspondant.

    Args:
        str_arg (str): Une chaîne de caractères représentant une adresse e-mail.

    Returns:
        (int, int): Un tuple où le premier élément est 1 si le mail est valide, 
        sinon 0. Le deuxième élément est le code d'erreur correspondant.
    """
    validite = 0 
    erreur = 0
    corps, at_symbole, domaine = str_arg.partition('@')

    # Vérifie s'il manque le symbole '@'
    if at_symbole == '':
        erreur = 2
    # Vérifie si le corps de l'email est vide ou invalide
    elif corps == '' or corps[0] == '.' or corps[-1] == '.' or '..' in corps or not all(c.isalnum() or c in "-_." for c in corps):
        erreur = 1
    # Vérifie si le domaine est vide ou invalide
    elif domaine == '' or domaine[0] == '.' or domaine[-1] == '.' or '..' in domaine or not all(c.isalnum() or c in "-." for c in domaine):
        erreur = 3
    # Vérifie s'il manque le point dans le domaine
    elif '.' not in domaine:
        erreur = 4
    else:
        validite = 1  # Si aucune erreur n'a été trouvée, le mail est valide

    return (validite, erreur)




def test_mail(str_variable2test: str):
    """
    Teste la validité d'une adresse e-mail et affiche le résultat avec un message d'erreur explicite.

    Args:
        str_variable2test (str): Une chaîne de caractères représentant une adresse e-mail à tester.
    """
    # Dictionnaire pour mapper les codes d'erreur à des messages explicites
    error_messages = {
        0: "Le mail est valide.",
        1: "Le mail n'est pas valide: le corps de l'adresse est incorrect.",
        2: "Le mail n'est pas valide: il manque le symbole '@'.",
        3: "Le mail n'est pas valide: le domaine est incorrect.",
        4: "Le mail n'est pas valide: il manque le point dans le domaine."
    }
    
    validite, code_erreur = is_mail(str_variable2test)
    if validite == 1:
        print(f"L'adresse '{str_variable2test}' est valide: {error_messages[0]} {validite, code_erreur}")
    else:
        print(f"L'adresse '{str_variable2test}' n'est pas valide: {error_messages[code_erreur]} {validite, code_erreur}")

# Exemples de test
test_mail('bisgambiglia_paul@univ-corse.fr')    # Doit renvoyer : Le mail est valide.
test_mail('bisgambiglia_paulOuniv-corse.fr')    # Doit renvoyer : Le mail n'est pas valide: il manque le symbole '@'.
test_mail('bisgambiglia_paul@univ-corsePOINTfr')# Doit renvoyer : Le mail n'est pas valide: il manque le point dans le domaine.
test_mail('@univ-corse.fr')                     # Doit renvoyer : Le mail n'est pas valide: le corps de l'adresse est incorrect.




