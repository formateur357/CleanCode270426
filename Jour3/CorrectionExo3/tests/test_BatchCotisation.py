import pytest
from BatchCotisation import ContributionLine, BatchAnomaly, process_batch

def test_batch_continue_apres_une_ligne_invalide():
    report = process_batch([
        ContributionLine(1000),
        ContributionLine(-1),
        ContributionLine(500)
    ])
    
    assert report.total_contribution == 120
    assert report.processed_lines == 2
    assert report.read_lines == 3
    assert report.anomalies == [BatchAnomaly(2, "base negative")]
    
def test_batch_signale_une_base_absente():
    report = process_batch([
        ContributionLine(1000),
        ContributionLine(None),
        ContributionLine(500)
    ])
    
    assert report.total_contribution == 120
    assert report.processed_lines == 2
    assert report.read_lines == 3
    assert report.anomalies == [BatchAnomaly(2, "base missing")]
    
def test_base_zero_est_traitee_comme_valide():
    report = process_batch([
        ContributionLine(1000),
        ContributionLine(0),
        ContributionLine(500)
    ])
    
    assert report.total_contribution == 120
    assert report.processed_lines == 3
    assert report.read_lines == 3
    assert report.anomalies == []
        
def test_lot_sans_anomalie_produit_un_rapport_sans_rejet():
    report = process_batch([
        ContributionLine(1000),
        ContributionLine(2000),
        ContributionLine(500)
    ])
    
    assert report.total_contribution == 240
    assert report.processed_lines == 3
    assert report.read_lines == 3
    assert report.anomalies == []
    
def test_rapport_distingue_lignes_lues_et_lignes_traitees():
    report = process_batch([
        ContributionLine(1000),
        ContributionLine(-1),
        ContributionLine(500),
        ContributionLine(None)
    ])
    
    assert report.total_contribution == 120
    assert report.processed_lines == 2
    assert report.read_lines == 4
    assert report.anomalies == [
        BatchAnomaly(2, "base negative"),
        BatchAnomaly(4, "base missing")
    ]