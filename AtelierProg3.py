def calculer_affranchissement(poids: float, type_lettre: str, sticker_suivi: bool = False) -> float:

    tarifs_lettre_verte = {
        20: 1.16,
        100: 2.32,
        250: 4.00,
        500: 6.00,
        1000: 7.50,
        3000: 10.50
    }

    tarifs_lettre_prioritaire = {
        20: 1.43,
        100: 2.86,
        250: 5.26,
        500: 7.89,
        3000: 11.44
    }

    tarifs_lettre_ecopli = {
        20: 1.14,
        100: 2.28,
        250: 3.92,
    }

    tarifs_cecogramme = {
        5000 : 0
    }

    tarifs_eco_outre_mer = {
        500 : 8.35,
        1000 : 11.20,
        2000 : 14.10,
        5000 : 23.65,
        10000 : 37.50,
        15000 : 75.85,
        30000 : 87.40,
    }

    # Déterminer le tarif selon le type de lettre
    if type_lettre == 'verte':
        tarifs = tarifs_lettre_verte
    elif type_lettre == 'prioritaire':
        tarifs = tarifs_lettre_prioritaire
    elif type_lettre == 'ecopli':
        tarifs = tarifs_lettre_ecopli
    elif type_lettre == 'cecogramme':
        tarifs = tarifs_cecogramme
    elif type_lettre == 'eco_outre_mer':
        tarifs = tarifs_eco_outre_mer
    else:
        return "Type de lettre invalide."

    # Trouver le bon tarif selon le poids
    montant = 0
    for limite_poids in tarifs:
        if poids <= limite_poids:
            montant = tarifs[limite_poids]
            break

    if sticker_suivi and type_lettre != 'cecogramme':
        montant += 0.50

    return montant



print("Le montant de l'affranchissement est de : ", calculer_affranchissement(312, 'verte', False))
print("Le montant de l'affranchissement est de : ", calculer_affranchissement(112, 'verte', True))
print("Le montant de l'affranchissement est de : ", calculer_affranchissement(1120, 'eco_outre_mer', True))
print("Le montant de l'affranchissement est de : ", calculer_affranchissement(1120, 'cecogramme', True))
