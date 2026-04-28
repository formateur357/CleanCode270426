def calculer_remboursement(frais_reels, montant_demande, plafond_annuel, deja_consomme):
    if frais_reels <= 0:
        return 0
    
    if montant_demande <= 0:
        return 0
    
    plafond_restant = max(0, plafond_annuel - deja_consomme)
    
    return min(frais_reels, montant_demande, plafond_restant)