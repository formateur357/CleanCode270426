import pytest

from calculCotisationMensuelle import calcul_cotisation_mensuelle


def test_salaire_sous_le_pmss():
    assert calcul_cotisation_mensuelle(3000) == 60.0
    
def test_salaire_au_niveau_du_pmss():
    assert calcul_cotisation_mensuelle(3900) == 78.0
    
def test_salaire_au_dessus_du_pmss():
    assert calcul_cotisation_mensuelle(5000) == 78.0
    
def test_salaire_negatif():
    with pytest.raises(ValueError, match="Le salaire ne peut pas être négatif."):
        calcul_cotisation_mensuelle(-1)