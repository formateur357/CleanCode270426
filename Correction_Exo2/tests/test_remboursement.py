from remboursement import calculer_remboursement
import pytest

@pytest.mark.parametrize(
    "frais_reels, montant_demande, plafond_annuel, deja_consomme, attendu",
    [
        (100, 80, 200, 50, 80),
        (100, 100, 150, 50, 100),
        (100, 150, 200, 50, 100),
        (100, 80, 200, 50, 80),
        (-100, 80, 200, 50, 0),
        (100, -80, 200, 50, 0),
        (100, 80, 200, 200, 0),
    ]
)
def test_calculer_remboursement(frais_reels, montant_demande, plafond_annuel, deja_consomme, attendu):
    result = calculer_remboursement(
        frais_reels,
        montant_demande,
        plafond_annuel,
        deja_consomme
    )
    
    assert result == attendu

def test_remboursement_est_limite_par_le_plafond_restant():
    result = calculer_remboursement(
        frais_reels=100,
        montant_demande=100,
        plafond_annuel=150,
        deja_consomme=50
    )
    
    assert result == 10
    
def test_remboursement_est_limite_par_les_frais_reels():
    result = calculer_remboursement(
        frais_reels=100,
        montant_demande=150,
        plafond_annuel=200,
        deja_consomme=50
    )
    
    assert result == 100
        
def test_remboursement_est_limite_par_le_montant_demande():
    result = calculer_remboursement(
        frais_reels=100,
        montant_demande=80,
        plafond_annuel=200,
        deja_consomme=50
    )
    
    assert result == 80
    
def test_remboursement_est_zero_si_les_frais_reels_sont_negatifs():
    result = calculer_remboursement(
        frais_reels=-100,
        montant_demande=80,
        plafond_annuel=200,
        deja_consomme=50
    )
    
    assert result == 0
    
def test_remboursement_est_zero_si_le_montant_demande_est_negatif():
    result = calculer_remboursement(
        frais_reels=100,
        montant_demande=-80,
        plafond_annuel=200,
        deja_consomme=50
    )
    
    assert result == 0
    
def test_remboursement_est_zero_si_le_plafond_est_deja_atteint():
    result = calculer_remboursement(
        frais_reels=100,
        montant_demande=80,
        plafond_annuel=200,
        deja_consomme=200
    )
    
    assert result == 0
    
def test_remboursement_vaut_zero_si_le_montant_demande_est_zero():
    result = calculer_remboursement(
        frais_reels=100,
        montant_demande=0,
        plafond_annuel=200,
        deja_consomme=50
    )
    
    assert result == 0
