class HealthReimbursementCalculator:
    TAUX_REMBOURSEMENT = 1.50
    
    def calculer_remboursement(self, frais_reels, est_actif, plafond_restant):
        if not est_actif:
            return 0.0

        remboursement = frais_reels * self.TAUX_REMBOURSEMENT   
        
        return min(remboursement, plafond_restant)
    
import pytest

def test_remboursement_est_nul_si_la_garantie_est_inactive():
    #GIVEN
    calculator = HealthReimbursementCalculator()
    frais_reels = 100.0
    garantie_active = False
    plafond_restant = 200.0
    
    #WHEN
    remboursement = calculator.calculer_remboursement(frais_reels, garantie_active, plafond_restant)
    
    #THEN
    assert remboursement == 0.0
    
def test_remboursement_est_calculé_correctement_pour_une_garantie_active():
    #GIVEN
    calculator = HealthReimbursementCalculator()
    frais_reels = 100.0
    garantie_active = True
    plafond_restant = 200.0
    
    #WHEN
    remboursement = calculator.calculer_remboursement(frais_reels, garantie_active, plafond_restant)
    
    #THEN
    assert remboursement == 150.0
    
def test_remboursement_ne_dépasse_pas_le_plafond_restant():
    #GIVEN
    calculator = HealthReimbursementCalculator()
    frais_reels = 200.0
    garantie_active = True
    plafond_restant = 250.0
    
    #WHEN
    remboursement = calculator.calculer_remboursement(frais_reels, garantie_active, plafond_restant)
    
    #THEN
    assert remboursement == 250.0
    
def test_remboursement_est_calculé_correctement_avec_un_plafond_restant_inférieur():
    #GIVEN
    calculator = HealthReimbursementCalculator()
    frais_reels = 100.0
    garantie_active = True
    plafond_restant = 120.0
    
    #WHEN
    remboursement = calculator.calculer_remboursement(frais_reels, garantie_active, plafond_restant)
    
    #THEN
    assert remboursement == 120.0
    
def test_remboursement_est_calculé_correctement_avec_des_frais_reels_inférieurs():
    #GIVEN
    calculator = HealthReimbursementCalculator()
    frais_reels = 50.0
    garantie_active = True
    plafond_restant = 200.0
    
    #WHEN
    remboursement = calculator.calculer_remboursement(frais_reels, garantie_active, plafond_restant)
    
    #THEN
    assert remboursement == 75.0
    
def test_remboursement_est_calculé_correctement_avec_des_frais_reels_supérieurs():
    #GIVEN
    calculator = HealthReimbursementCalculator()
    frais_reels = 300.0
    garantie_active = True
    plafond_restant = 400.0
    
    #WHEN
    remboursement = calculator.calculer_remboursement(frais_reels, garantie_active, plafond_restant)
    
    #THEN
    assert remboursement == 350.0
