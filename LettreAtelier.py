def calculer_affranchissement(poids: float, type_lettre: str, sticker_suivi: bool = False) -> float:
    """
    Calcule le montant d'affranchissement pour une lettre en fonction du poids, du type de lettre et de la présence d'un sticker de suivi.
    
    :param poids: Poids de la lettre en grammes.
    :param type_lettre: Type de lettre, qui peut être 'verte', 'prioritaire', 'ecopli', 'cecogramme', ou 'eco_outre_mer'.
    :param sticker_suivi: Booléen indiquant si un sticker de suivi est demandé (par défaut: False).
    :return: Montant de l'affranchissement en euros, ou -1 si le type de lettre est invalide ou le poids non couvert.
    """
    
    TARIFS_LETTRE_VERTE = {
        20: 1.16,
        100: 2.32,
        250: 4.00,
        500: 6.00,
        1000: 7.50,
        3000: 10.50,
        'TARIF_STICKER_SUIVI': True
    }

    TARIFS_LETTRE_PRIORITAIRE = {
        20: 1.43,
        100: 2.86,
        250: 5.26,
        500: 7.89,
        3000: 11.44,
        'TARIF_STICKER_SUIVI': True
    }

    TARIFS_LETTRE_ECOPLI = {
        20: 1.14,
        100: 2.28,
        250: 3.92,
        'TARIF_STICKER_SUIVI': True
    }

    TARIFS_LETTRE_CECOGRAME = {
        5000: 0,
        'TARIF_STICKER_SUIVI': False
    }

    TARIFS_LETTRE_ECO_OUTRE_MER = {
        500: 8.35,
        1000: 11.20,
        2000: 14.10,
        5000: 23.65,
        10000: 37.50,
        15000: 75.85,
        30000: 87.40,
        'TARIF_STICKER_SUIVI': False
    }

    # Déterminer le tarif selon le type de lettre
    TYPE_TARIF = {
        'verte': TARIFS_LETTRE_VERTE,
        'prioritaire': TARIFS_LETTRE_PRIORITAIRE,
        'ecopli': TARIFS_LETTRE_ECOPLI,
        'cecogramme': TARIFS_LETTRE_CECOGRAME,
        'eco_outre_mer': TARIFS_LETTRE_ECO_OUTRE_MER
    }
    
    tarifs = TYPE_TARIF.get(type_lettre)

    if tarifs:
        # Trouver le bon tarif selon le poids
        montant = 0
        for limite_poids in sorted(tarifs.keys()):
            if poids <= limite_poids:
                montant = tarifs[limite_poids]
                break

        if sticker_suivi and tarifs.get('TARIF_STICKER_SUIVI', False):
            montant += 0.50
        
        return montant 
    
    else:
        return -1

# Exemples d'utilisation
print("Le montant de l'affranchissement est de : ", calculer_affranchissement(312, 'verte', False))
print("Le montant de l'affranchissement est de : ", calculer_affranchissement(112, 'verte', True))
print("Le montant de l'affranchissement est de : ", calculer_affranchissement(1120, 'eco_outre_mer', True))
print("Le montant de l'affranchissement est de : ", calculer_affranchissement(1120, 'cecogramme', True))
print("Le montant de l'affranchissement est de : ", calculer_affranchissement(1120, 'cogramme', True))
