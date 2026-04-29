import pytest

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