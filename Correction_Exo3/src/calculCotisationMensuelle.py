PMSS_MENSUEL = 3900.00  # Plafond Mensuel de la Sécurité Sociale en euros
TAUX_COTISATION = 0.02  # Taux de cotisation de 2%

def calcul_cotisation_mensuelle(salaire_brut_mensuel):
    if salaire_brut_mensuel < 0:
        raise ValueError("Le salaire brut mensuel ne peut pas être négatif.")
    
    assiette_plaffonnee = min(salaire_brut_mensuel, PMSS_MENSUEL)
    
    cotisation_due = assiette_plaffonnee * TAUX_COTISATION
    
    return cotisation_due