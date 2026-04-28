import pytest

from calculatrice import additionner, diviser, soustractioner, multiplier

def test_additionner_deux_nombres():
    assert additionner(2, 3) == 5
    
def test_diviser_par_zero():
    with pytest.raises(ValueError):
        diviser(10, 0)
        
def test_diviser_par_zero_declenche_une_erreur_explicite():
    with pytest.raises(ValueError, match="Le dénominateur ne peut pas être zéro."):
        diviser(10, 0)
        
@pytest.mark.parametrize("a, b, resultat_attendu",
    [(5, 3, 2), (10, 4, 6), (7, 2, 5)],)
def test_soustraire_parametrise(a, b, resultat_attendu):
    assert soustractioner(a, b) == resultat_attendu
    
@pytest.fixture
def nombres():
    return (10, 5)

def test_multiplier_avec_fixture(nombres):
    assert multiplier(nombres[0], nombres[1]) == 50